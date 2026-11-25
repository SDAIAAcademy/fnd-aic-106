"""Helper of the solution scripts: run a kit tool from labs/ and return its exit code and output."""
from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

LABS = Path(__file__).resolve().parents[1]


def kit(tool: str, *args: str) -> tuple[int, str]:
    env = dict(os.environ, PYTHONIOENCODING="utf-8")
    p = subprocess.run([sys.executable, "-X", "utf8", str(LABS / "kit" / tool), *args], cwd=LABS, env=env,
                       capture_output=True, text=True, encoding="utf-8")
    return p.returncode, p.stdout + p.stderr


def expect(label: str, ok: bool, detail: str = "") -> None:
    if not ok:
        print(f"FAIL: {label}\n{detail}")
        sys.exit(1)
    print(f"ok   {label}")
