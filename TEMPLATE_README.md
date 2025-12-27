# Copier Template: Python Project

This repository is a Copier template for Python libraries, CLIs, GUIs, and TUIs.

## Usage

```bash
pipx install copier
# or
pip install copier
```

```bash
copier copy <path-or-git-url> <dest>
```

Example:

```bash
copier copy . ../my-new-project
```

## Template Self-Test

```bash
python tools/test_template_generation.py
```

## Quick Sanity Check

```bash
mkdir -p _renders
copier copy . _renders/demo_lib --defaults -d project_name=demo_lib -d package_name=demo_lib -d project_slug=demo-lib -d project_kind=library -d author_name="Demo Author" -d author_email=demo@example.com
copier copy . _renders/demo_cli --defaults -d project_name=demo_cli -d package_name=demo_cli -d project_slug=demo-cli -d project_kind=cli -d author_name="Demo Author" -d author_email=demo@example.com
copier copy . _renders/demo_tui --defaults -d project_name=demo_tui -d package_name=demo_tui -d project_slug=demo-tui -d project_kind=tui -d author_name="Demo Author" -d author_email=demo@example.com

cd _renders/demo_lib
python -m pip install -U pip
python -m pip install -e ".[dev]"
python -m pytest
python -m ruff check .
python -m mypy src
python -m build
```

## Common Failures & Fixes

- Missing optional dependencies: run `python -m pip install -e ".[dev]"` before pytest/ruff/mypy.
- Entry point not found: confirm `[project.scripts]` in `pyproject.toml` matches the module path.
- Build failures: ensure `python -m pip install build` is available and `python -m build` runs.
- Typecheck errors: start with `mypy src` and fix or adjust `tool.mypy` config.

## Updating a Project

```bash
cd ../my-new-project
copier update
```

## Template Compatibility

- Keep changes backward compatible when possible.
- Avoid renaming variables unless necessary.
- Document breaking template changes in the template changelog.
