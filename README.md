# python-template

This repository is a personal Python project template and backup.
It exists so I always have a known-good starting point for new projects
and a copy of my preferred tooling, layout, and defaults in case I lose
local files or need to start fresh on a new system.

## When to use this

Use this repository when:

- Starting a new Python project from scratch
- I want a known-good baseline with my usual tooling
- I don’t want to think about setup details
- I need something stable and boring that already works

Do NOT use this when:

- Experimenting with a one-off script
- Testing a new framework or unusual project layout
- Copying code into an existing project

## Typical workflow

### Option A: Use GitHub’s template button (simplest)

1. On GitHub, click **Use this template**
2. Create a new repository
3. Clone the new repo locally

### Option B: Use Copier locally (recommended when customizing)

1. Install Copier (once):
   pipx install copier
2. Generate a new project:
   copier copy gh:taggedzi/python-project-template path/to/new-project
3. Follow the prompts
4. `cd` into the new project

### After generation

1. Create and activate a virtual environment
2. Install dependencies
3. Start coding

Note: The template includes additional Copier options used for testing;
normal usage does not require any arguments beyond `copier copy`.

## After creating a new project

Update these immediately:

- Project name and description
- `pyproject.toml` metadata (name, version, description)
- README title and purpose
- Any placeholder values or TODO comments

Optional (depending on project):

- Adjust Python version support
- Review CI configuration
- Enable or disable tooling as needed

## What this template includes

- Standard Python project layout
- `pyproject.toml`-based configuration
- Linting and formatting tooling
- Type checking
- Unit testing setup
- GitHub Actions CI
- Preconfigured `.gitignore`

## What this template intentionally avoids

- Any specific application framework
- Opinionated runtime or deployment behavior
- Project-specific directory structures
- Bundled services or external dependencies
- Assumptions about how the code will be used

## Notes to future me

- This repo is mainly a personal template + off-site backup.
- If Copier looks “complicated” in tests, that’s normal: tests/CI may pass extra flags.
  Normal usage is just `copier copy ...` and answer prompts.
- Keep this template boring. If a future project needs a framework-heavy setup, make a new template instead.

## Quick commands (copy/paste)

### Setup

```bash
python -m venv .venv

# Windows:
.\.venv\Scripts\Activate.ps1

# macOS/Linux:
source .venv/bin/activate

python -m pip install -U pip
python -m pip install -e ".[dev]"

### Run checks
python -m pytest
# or
nox

### Lint / format / type-check (if installed)
ruff check .
ruff format .
mypy .

### Build
python -m build
```
