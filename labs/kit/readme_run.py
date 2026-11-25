# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Clean-run test of a README: follow its commands on a fresh copy of the project, as a stranger would.

From labs/:
    uv run kit/readme_run.py work/README.md
    uv run kit/readme_run.py work/README.md --project files/urgency-tagger --log work/runlog.md

It copies the project to work/clean-run/ (deleted first), leaving out any config.toml, out/ or
virtual environment, then runs, in order, every command in the README's shell code blocks
(```sh, ```bash, ```shell, ```console or ```powershell). Only two kinds of command run: `uv ...`
and a file copy (`cp a b` or `copy a b`); anything else is listed and refused, so a README cannot
make this tool do harm. A block marked ```text right after a command block holds the output the
README promises: each of its lines must appear in that command's output. The run log records
every command, its exit code and its first output lines. A partner following the README by hand
writes the same log; this tool is the stand-in for a partner who types exactly what is written.
"""
from __future__ import annotations

import argparse
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

import common as C

SHELL = {"sh", "bash", "shell", "console", "powershell", "ps", "pwsh"}
BLOCK = re.compile(r"```([\w-]*)\n(.*?)```", re.S)


def blocks(text: str) -> list[tuple[str, list[str]]]:
    out = []
    for lang, body in BLOCK.findall(text):
        out.append((lang.lower(), [l.rstrip() for l in body.splitlines()]))
    return out


def commands(lines: list[str]) -> list[str]:
    cmds = []
    for line in lines:
        s = line.strip()
        if not s or s.startswith("#"):
            continue
        for prompt in ("$ ", "> ", "PS> "):
            if s.startswith(prompt):
                s = s[len(prompt):].strip()
        cmds.append(s)
    return cmds


def fresh_copy(src: Path, dst: Path) -> None:
    if dst.exists():
        shutil.rmtree(dst)
    shutil.copytree(src, dst, ignore=shutil.ignore_patterns("config.toml", "out", ".venv", "__pycache__", "uv.lock"))


def run(cmd: str, cwd: Path) -> tuple[int, str]:
    parts = cmd.split()
    if parts[0] in ("cp", "copy") and len(parts) == 3:
        try:
            shutil.copyfile(cwd / parts[1], cwd / parts[2])
            return 0, f"copied {parts[1]} to {parts[2]}"
        except OSError as e:
            return 1, f"copy failed: {e.strerror}"
    if parts[0] != "uv":
        return 126, "refused: only uv commands and a file copy run in the clean-run test"
    env = {k: v for k, v in os.environ.items() if k not in ("UV_PROJECT_ENVIRONMENT", "VIRTUAL_ENV")}
    env["PYTHONIOENCODING"] = "utf-8"
    p = subprocess.run(parts, cwd=cwd, env=env, capture_output=True, text=True, encoding="utf-8", errors="replace")
    out = (p.stdout + p.stderr).replace(str(cwd), "<project>")
    lines = [l for l in out.splitlines() if not re.match(r"\s*(Using CPython|Creating virtual environment|Resolved|Prepared|Installed|Audited|Built|Uninstalled|warning: `VIRTUAL_ENV`)", l)]
    return p.returncode, "\n".join(lines)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("readme")
    ap.add_argument("--project", default=str(C.FILES / "urgency-tagger"))
    ap.add_argument("--log", default=None)
    a = ap.parse_args()
    text = C.read(a.readme)
    work = C.LABS / "work" / "clean-run"
    fresh_copy(Path(a.project), work)
    rep = C.Report(f"clean run of {a.readme}")
    log = ["# Run log", "", f"README: {Path(a.readme).name}. Project copied fresh, without config.toml or an environment.", ""]
    bl = blocks(text)
    ran, last_out = 0, ""
    for i, (lang, lines) in enumerate(bl):
        if lang in SHELL:
            for cmd in commands(lines):
                code, out = run(cmd, work)
                ran += 1
                last_out = out
                first = out.strip().splitlines()[:4]
                log += [f"## {ran}. `{cmd}`", "", f"exit code {code}", ""] + [f"    {l}" for l in first] + [""]
                rep.need(code == 0, f"`{cmd}` ended with exit code {code}: {first[-1] if first else 'no output'}")
        elif lang == "text" and i > 0 and bl[i - 1][0] in SHELL:
            for want in [l.strip() for l in lines if l.strip()]:
                ok = want in last_out
                log += [f"expected `{want}`: {'seen' if ok else 'NOT seen'}", ""]
                rep.need(ok, f"the README promises '{want}' but the command printed something else")
    rep.need(ran > 0, "no shell code block found: put the commands in ```sh blocks")
    low = text.lower()
    rep.need(re.search(r"python[^\n]{0,20}3\.1[1-9]", low) is not None, "say which Python version the project needs (uv can install it)")
    for need, words in (("install", ("install", "setup", "set up")), ("run", ("run", "usage", "use")), ("check", ("check", "test", "verify"))):
        rep.need(C.find_section(C.sections(text), *words) is not None, f"no section heading for {need}")
    rep.note(f"{ran} commands run")
    log += ["Result: " + ("PASS" if not rep.problems else f"{len(rep.problems)} to fix"), ""]
    log_path = Path(a.log) if a.log else C.LABS / "work" / "runlog.md"
    log_path.parent.mkdir(parents=True, exist_ok=True)
    log_path.write_text("\n".join(log), encoding="utf-8")
    rep.note(f"run log written to {log_path.relative_to(C.LABS).as_posix() if log_path.is_relative_to(C.LABS) else log_path.name}")
    shutil.rmtree(work, ignore_errors=True)
    return rep.finish()


if __name__ == "__main__":
    sys.exit(main())
