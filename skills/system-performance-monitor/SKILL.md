---
name: system-performance-monitor
description: Diagnose local system performance using safe read-only commands for CPU, memory, disk, battery, process, and network checks, then summarize likely bottlenecks and next actions.
---

# System Performance Monitor

Use this skill when the user asks to monitor, diagnose, inspect, troubleshoot, or summarize local system performance.

## Goals

Help Codex:
- identify current system load and likely bottlenecks
- inspect CPU, memory, disk, battery, process, and network health
- produce a concise performance summary with severity and next steps
- keep diagnostics read-only unless the user explicitly approves a change

## Safety Rules

- Use read-only commands by default.
- Do not kill processes unless the user explicitly approves the exact process or PID.
- Do not delete files unless the user explicitly approves the exact path or cleanup plan.
- Do not restart services unless the user explicitly approves the service and command.
- Do not install packages unless the user explicitly asks for installation and approves any required network or privilege escalation.
- Do not print secrets from environment variables, config files, command arguments, tokens, keys, or credentials.
- If command output includes sensitive values, summarize the relevant performance signal instead of repeating the sensitive text.

## Workflow

### 1. Identify Environment

Check the operating system and available tools before choosing commands.

Preferred commands:
- `uname -a`
- `sw_vers` on macOS
- `lsb_release -a` or `cat /etc/os-release` on Linux
- `command -v top vm_stat ps df du netstat lsof iostat uptime`

### 2. Check Overall Load

Use uptime and process tools to understand whether the system is busy.

Preferred commands:
- `uptime`
- `top -l 1 -n 15` on macOS
- `top -b -n 1 -o %CPU | head -40` on Linux
- `ps aux | sort -nrk 3 | head -15`

Summarize:
- load average
- CPU-heavy processes
- whether the load seems sustained or momentary
- process names, not sensitive command arguments

### 3. Check Memory Pressure

Inspect free memory, swap, and memory-heavy processes.

Preferred commands:
- `vm_stat` on macOS
- `memory_pressure` on macOS when available
- `free -h` on Linux
- `ps aux | sort -nrk 4 | head -15`

Summarize:
- available memory
- swap usage or paging pressure
- memory-heavy processes
- whether memory pressure is likely affecting responsiveness

### 4. Check Disk Usage

Inspect filesystem capacity and obvious pressure points.

Preferred commands:
- `df -h`
- `du -sh ~/* 2>/dev/null | sort -h | tail -20` only when the user asks where space is going
- `iostat 1 3` when available

Summarize:
- filesystems over 80 percent usage
- filesystems over 90 percent usage as high severity
- possible disk I/O pressure
- cleanup candidates only at directory level unless the user asks for details

### 5. Check Battery and Power

When on a laptop, inspect power and battery status.

Preferred commands:
- `pmset -g batt` on macOS
- `pmset -g therm` on macOS
- `upower -i` on Linux when available

Summarize:
- battery percentage
- charging status
- thermal pressure
- power-related throttling indicators

### 6. Check Network Basics

Use lightweight network checks only when performance symptoms involve connectivity.

Preferred commands:
- `netstat -ib` on macOS
- `netstat -i` on Linux
- `lsof -i -P -n | head -40` only when the user asks which apps are using network connections
- `ping -c 4 1.1.1.1` only when connectivity testing is needed

Summarize:
- interface status
- packet errors if visible
- latency or packet loss from ping
- likely local versus external network issue

### 7. Produce Final Report

Use this structure:

- Overall status: healthy, watch, degraded, or critical
- Main bottleneck: CPU, memory, disk, network, power, or unclear
- Evidence: 3 to 6 concise observations
- Top contributors: process or subsystem names
- Recommended next actions: safe steps first
- Actions requiring approval: process kill, cleanup, restart, install, or privilege escalation

## Severity Guidance

Use `healthy` when there is no obvious pressure.

Use `watch` when:
- CPU load is elevated but not clearly harmful
- disk usage is above 80 percent
- memory pressure is present but swap is limited

Use `degraded` when:
- CPU is saturated by one or more processes
- memory pressure is high or swap is active
- disk usage is above 90 percent
- disk or network errors are visible

Use `critical` when:
- root or main filesystem is nearly full
- the system is heavily swapping and barely responsive
- thermal or power throttling is severe
- repeated command failures suggest system instability

## Remediation Rules

When recommending remediation:
- Start with non-destructive actions.
- Explain why each action would help.
- Ask for approval before destructive or privileged actions.
- Prefer targeted commands over broad cleanup.
- Preserve user data and current work.
