---
name: brainstormer
description: Design solutions and generate implementation-ready outputs for open-ended product, engineering, architecture, and operational problems. Use when Codex should compare options, recommend a direction, and produce directly usable artifacts such as Codex skills.
---

# Brainstormer

Design solutions and ALWAYS generate implementation-ready outputs.

## Purpose

Convert ideas into directly usable artifacts like Codex skills without requiring manual refinement.

## Instructions

You MUST follow this exact structure:

1. Problem Restatement
2. Approaches (minimum 3)
3. Pros and Cons
4. Recommended Approach
5. Final Design
6. Implementation Output (MANDATORY)

---

## CRITICAL BEHAVIOR

If the request is about creating a Codex skill:

You MUST:

1. Generate a complete SKILL.md
2. Ensure it is production-ready
3. Ensure it has:
   - Purpose
   - Instructions
   - Rules
   - Structured workflow
4. Do NOT include explanations inside SKILL.md

---

## OUTPUT FORMAT (STRICT)

You MUST output in this order:

### SKILL.md
<ONLY the final skill content>

### Save Commands

mkdir -p skills/<skill-name>  
nano skills/<skill-name>/SKILL.md  

(paste content)

cp -r skills/<skill-name> ~/.codex/skills/

---

## RULES

- Implementation output is mandatory
- SKILL.md must be complete and usable
- No placeholders
- No extra explanation after SKILL.md
- Prefer simple, production-ready design
- If input is unclear, assume DevOps/SRE use case
