#!/usr/bin/env python3

import argparse
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


REQUIRED_DOC_FIELDS = ("summary", "usage", "update_notes")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Sync upstream source files into local Codex skill scripts folders."
    )
    parser.add_argument(
        "--manifest",
        default="sources.json",
        help="Path to the source manifest file.",
    )
    parser.add_argument(
        "--target",
        default="all",
        help='Skill name to sync, or "all".',
    )
    return parser.parse_args()


def load_manifest(path: Path) -> dict:
    if not path.exists():
        raise SystemExit(f"Manifest not found: {path}")
    data = json.loads(path.read_text())
    if not isinstance(data, dict) or "skills" not in data or not isinstance(data["skills"], list):
        raise SystemExit("Manifest must contain a top-level 'skills' list.")
    return data


def run_git(args: list[str], cwd: Path) -> str:
    result = subprocess.run(
        ["git", *args],
        cwd=cwd,
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout.strip()


def ensure_relative_path(path_text: str) -> Path:
    path = Path(path_text)
    if path.is_absolute() or ".." in path.parts:
        raise ValueError(f"Unsafe path: {path_text}")
    return path


def validate_entry(entry: dict) -> None:
    required_fields = ("skill", "repo_url", "branch", "source_paths", "docs")
    for field in required_fields:
        if field not in entry:
            raise ValueError(f"Missing required field: {field}")

    ensure_relative_path(entry["skill"])

    if not isinstance(entry["source_paths"], list) or not entry["source_paths"]:
        raise ValueError("source_paths must be a non-empty list.")

    for path_text in entry["source_paths"]:
        ensure_relative_path(path_text)

    docs = entry["docs"]
    if not isinstance(docs, dict):
        raise ValueError("docs must be a mapping.")

    for field in REQUIRED_DOC_FIELDS:
        if not docs.get(field):
            raise ValueError(f"Missing docs field: {field}")


def copy_source_path(source_root: Path, relative_path: Path, destination_root: Path) -> list[str]:
    source_path = source_root / relative_path
    if not source_path.exists():
        raise ValueError(f"Source path does not exist in upstream repo: {relative_path}")

    copied = []
    if source_path.is_dir():
        for file_path in source_path.rglob("*"):
            if file_path.is_dir():
                continue
            rel_file = file_path.relative_to(source_root)
            target_path = destination_root / rel_file
            target_path.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(file_path, target_path)
            copied.append(str(rel_file))
    else:
        target_path = destination_root / relative_path
        target_path.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source_path, target_path)
        copied.append(str(relative_path))

    return copied


def write_skill_readme(
    skill_dir: Path,
    entry: dict,
    commit_sha: str,
    copied_paths: list[str],
    manifest_path: Path,
) -> None:
    docs = entry["docs"]
    refresh_cmd = (
        f"python3 skills/skill-source-sync/scripts/sync-skill-sources.py "
        f"--manifest {manifest_path.name} --target {entry['skill']}"
    )
    content = "\n".join(
        [
            f"# {entry['skill']}",
            "",
            "## Purpose",
            "",
            docs["summary"],
            "",
            "## Upstream Source",
            "",
            f"- Repository: {entry['repo_url']}",
            f"- Branch: {entry['branch']}",
            f"- Last synced commit: {commit_sha}",
            "",
            "## Copied Paths",
            "",
            *[f"- {path}" for path in copied_paths],
            "",
            "## Usage",
            "",
            docs["usage"],
            "",
            "## Refresh",
            "",
            f"`{refresh_cmd}`",
            "",
            "## Update Notes",
            "",
            docs["update_notes"],
            "",
        ]
    )
    (skill_dir / "README.md").write_text(content)


def write_provenance(skill_dir: Path, entry: dict, commit_sha: str, copied_paths: list[str]) -> None:
    metadata = {
        "skill": entry["skill"],
        "repo_url": entry["repo_url"],
        "branch": entry["branch"],
        "commit_sha": commit_sha,
        "copied_paths": copied_paths,
    }
    provenance_path = skill_dir / ".source-sync.json"
    provenance_path.write_text(json.dumps(metadata, indent=2) + "\n")


def sync_entry(repo_root: Path, manifest_path: Path, entry: dict) -> dict:
    validate_entry(entry)

    skill_name = entry["skill"]
    skill_dir = repo_root / "skills" / skill_name
    scripts_dir = skill_dir / "scripts"
    scripts_dir.mkdir(parents=True, exist_ok=True)

    with tempfile.TemporaryDirectory(prefix=f"sync-{skill_name}-") as tmp_dir:
        tmp_path = Path(tmp_dir)
        clone_dir = tmp_path / "upstream"
        subprocess.run(
            ["git", "clone", "--depth", "1", "--branch", entry["branch"], entry["repo_url"], str(clone_dir)],
            check=True,
            capture_output=True,
            text=True,
        )
        commit_sha = run_git(["rev-parse", "HEAD"], clone_dir)

        copied_paths: list[str] = []
        for path_text in entry["source_paths"]:
            rel_path = ensure_relative_path(path_text)
            copied_paths.extend(copy_source_path(clone_dir, rel_path, scripts_dir))

    write_provenance(skill_dir, entry, commit_sha, copied_paths)
    write_skill_readme(skill_dir, entry, commit_sha, copied_paths, manifest_path)

    return {
        "skill": skill_name,
        "commit_sha": commit_sha,
        "copied_paths": copied_paths,
    }


def main() -> int:
    args = parse_args()
    repo_root = Path(__file__).resolve().parents[3]
    manifest_path = (repo_root / args.manifest).resolve()
    manifest = load_manifest(manifest_path)

    entries = manifest["skills"]
    if args.target != "all":
        entries = [entry for entry in entries if entry.get("skill") == args.target]
        if not entries:
            raise SystemExit(f"No manifest entry found for skill: {args.target}")

    results = []
    for entry in entries:
        try:
            results.append(sync_entry(repo_root, manifest_path, entry))
        except Exception as exc:  # noqa: BLE001
            print(f"[error] {entry.get('skill', '<unknown>')}: {exc}", file=sys.stderr)
            return 1

    for result in results:
        print(f"[synced] {result['skill']} @ {result['commit_sha']}")
        for path in result["copied_paths"]:
            print(f"  - {path}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
