"""Generate projects from the template and run smoke tests."""

from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Iterable

PROJECT_KINDS = ["library", "cli", "gui", "tui"]


def run(cmd: Iterable[str], cwd: Path | None = None) -> None:
    cmd_list = list(cmd)
    print("+", " ".join(cmd_list))
    subprocess.run(cmd_list, cwd=cwd, check=True)


def venv_python(venv_dir: Path) -> Path:
    if os.name == "nt":
        return venv_dir / "Scripts" / "python.exe"
    return venv_dir / "bin" / "python"


def venv_entrypoint(venv_dir: Path, name: str) -> Path:
    if os.name == "nt":
        return venv_dir / "Scripts" / f"{name}.exe"
    return venv_dir / "bin" / name


def generate_project(template_root: Path, dest: Path, project_kind: str) -> None:
    data_args = [
        "-d",
        f"project_name=Sample {project_kind.title()}",
        "-d",
        f"package_name=sample_{project_kind}",
        "-d",
        f"project_slug=sample-{project_kind}",
        "-d",
        "author_name=Template Author",
        "-d",
        "author_email=template@example.com",
        "-d",
        "description=Template smoke test project",
        "-d",
        "license=MIT",
        "-d",
        f"project_kind={project_kind}",
        "-d",
        "include_nox=true",
        "-d",
        "include_precommit=true",
        "-d",
        "include_mypy=true",
        "-d",
        "include_github_actions=true",
        "-d",
        "include_docs=true",
        "-d",
        "include_release_drafting=false",
    ]
    run([sys.executable, "-m", "copier", "copy", str(template_root), str(dest), "--quiet"] + data_args)


def validate_expected_files(dest: Path, package_name: str, project_kind: str) -> None:
    expected = [
        dest / "README.md",
        dest / "LICENSE",
        dest / "SECURITY.md",
        dest / "PRODUCTION_READY_CHECKLIST.md",
        dest / "pyproject.toml",
        dest / "tests" / "test_smoke.py",
        dest / "src" / package_name / "__init__.py",
    ]
    if project_kind == "cli":
        expected.append(dest / "src" / package_name / "cli.py")
    if project_kind == "tui":
        expected.append(dest / "src" / package_name / "app.py")
    if project_kind == "gui":
        expected.append(dest / "src" / package_name / "gui.py")

    missing = [path for path in expected if not path.exists()]
    if missing:
        raise RuntimeError(f"Missing expected files: {missing}")


def run_project_checks(dest: Path, package_name: str, project_slug: str, project_kind: str) -> None:
    venv_dir = dest / ".venv"
    run([sys.executable, "-m", "venv", str(venv_dir)])
    py = venv_python(venv_dir)
    run([str(py), "-m", "pip", "install", "--upgrade", "pip"], cwd=dest)
    run([str(py), "-m", "pip", "install", "-e", ".[dev]"], cwd=dest)
    run([str(py), "-m", "pytest"], cwd=dest)

    if project_kind == "cli":
        entry = venv_entrypoint(venv_dir, project_slug)
        if entry.exists():
            run([str(entry), "--help"], cwd=dest)
        else:
            run([str(py), "-m", f"{package_name}.cli", "--help"], cwd=dest)
    else:
        run([str(py), "-c", f"import {package_name}"])


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--kinds", nargs="*", default=PROJECT_KINDS)
    args = parser.parse_args()

    template_root = Path(__file__).resolve().parents[1]
    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = Path(tmp)
        for project_kind in args.kinds:
            dest = tmp_path / f"sample-{project_kind}"
            generate_project(template_root, dest, project_kind)
            package_name = f"sample_{project_kind}"
            project_slug = f"sample-{project_kind}"
            validate_expected_files(dest, package_name, project_kind)
            run_project_checks(dest, package_name, project_slug, project_kind)
            shutil.rmtree(dest, ignore_errors=True)

    print("Template generation smoke tests completed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
