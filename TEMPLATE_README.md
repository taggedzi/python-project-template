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

## Updating a Project

```bash
cd ../my-new-project
copier update
```

## Template Compatibility

- Keep changes backward compatible when possible.
- Avoid renaming variables unless necessary.
- Document breaking template changes in the template changelog.
