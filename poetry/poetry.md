![Python Tinitiate Image](../../python_tinitiate.png)

# Python Tutorial
&copy; TINITIATE.COM

##### [Back To Contents](../../README.md)

# Poetry
* Poetry is a modern tool for managing Python **dependencies, environments, and packaging**.  
* It replaces traditional tools like `pip`, `requirements.txt`, and `setup.py` with a **single unified workflow**.
* It simplifies project setup, library publishing, and virtual environment management.
```bash
# To install 'poetry' run the following command
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -

# Verify
poetry --version
```

## Why Poetry?
* **Traditional Pain Points**:  
  - `pip` installs dependencies, but doesn’t manage project metadata.  
  - `virtualenv` must be created manually.  
  - `requirements.txt` isn’t enough for packaging libraries.  
  - `setup.py` is verbose and hard to maintain.  
* **Poetry’s Solution**:  
  - One tool for **dependency management + packaging**.  
  - Handles **virtual environments automatically**.  
  - Standardized on `pyproject.toml` (PEP 518/621).  
  - Provides reproducible builds with **lock files**.

## Creating a New Project
* Quickly bootstrap a Python project with a clean structure.
```bash
poetry new myproject
```
* Creates:
  - `pyproject.toml`: Project metadata + dependencies.  
  - `README.md`: Documentation scaffold.  
  - `tests/`: Ready-made test suite.  
```text
myproject/
├── pyproject.toml
├── README.md
├── myproject/
│   └── __init__.py
└── tests/
    └── test_myproject.py
```

## The `pyproject.toml` File
* Core configuration lives in `pyproject.toml`.
* This replaces `setup.py`, `setup.cfg` and `requirements.txt` files as in the traditional workflow.
* **Sections**:  
  - `[tool.poetry]`: Project metadata (name, version, description, authors).  
  - `[tool.poetry.dependencies]`: Runtime dependencies.  
  - `[tool.poetry.dev-dependencies]`: Development tools (linters, testing).  
  - `[build-system]`: Defines how the project is built.  
```toml
[tool.poetry]
name = "myproject"
version = "0.1.0"
description = "My awesome package"
authors = ["Alice <alice@example.com>"]

[tool.poetry.dependencies]
python = "^3.11"
requests = "^2.31"

[tool.poetry.dev-dependencies]
pytest = "^7.0"

[build-system]
requires = ["poetry-core>=1.0.0"]
build-backend = "poetry.core.masonry.api"
```

## Adding & Removing Dependencies
* **Why Important?**  
  - Dependencies define what your project needs to run.  
  - Poetry automatically updates `pyproject.toml` and `poetry.lock`.  
* **Version Management**: Poetry enforces semantic versioning rules (`^`, `~`, ranges).  
* **Safe Removal**: Keeps the dependency graph clean.  
```bash
# Install a dependency:
poetry add requests

# Add with version constraint:
poetry add "django>=4.2,<5.0"

# Remove:
poetry remove requests
```

## Virtual Environments with Poetry
* **Problem Without Poetry**: Developers had to manually create/activate virtual envs.  
* **Poetry’s Advantage**: Creates and manages project-specific venvs automatically.  
* **Consistency**: Everyone working on the project uses the same environment.
```bash
# Activate it:
poetry shell

# Run commands without activating:
poetry run python main.py
```

## Running Scripts & Commands
* Define scripts in `pyproject.toml`
* Define shortcuts for repetitive commands (like `flask run` or `pytest`).  
* Keeps command execution consistent across dev machines.  
```toml
[tool.poetry.scripts]
start = "myproject.main:run"
```
**Run:**
```bash
poetry run start
```

## Dependency Resolution & Lock Files
* **Dependency Resolution**: Poetry ensures installed packages don’t conflict.  
* **Lock File (`poetry.lock`)**:  
  - Records **exact versions** used.  
  - Guarantees reproducibility across machines/CI.  
* **Updating**: When new versions are available, Poetry can upgrade while respecting constraints.  
```bash
poetry update
```

## Development Dependencies
* **Separation of Concerns**:  
  - Runtime deps (used by users).  
  - Dev deps (used only during development/testing).  
* **Examples**: `pytest`, `black`, `flake8`.  
* **Benefit**: Keeps production environment lean.  
```bash
poetry add --dev black flake8
# These go under `[tool.poetry.dev-dependencies]`.
```

## Managing Multiple Environments
* **Problem**: Different projects require different Python versions.  
* **Poetry Solution**: Bind each project to a specific Python interpreter.  
* **Flexibility**: Switch interpreters easily. 
```bash
poetry env use python3.11
poetry env use /usr/bin/python3.9
```
**List environments:**
```bash
poetry env list
```

## Publishing Packages to PyPI
- Share your libraries with the community or internal teams.  
- **Build Process**: Creates wheel (`.whl`) and source (`.tar.gz`) distributions.  
- **Repositories**: Can publish to PyPI or TestPyPI.  
```bash
poetry build
```
**Publish:**
```bash
poetry publish --username <user> --password <pass>
```
**For test PyPI:**
```bash
poetry config repositories.testpypi https://test.pypi.org/legacy/
poetry publish -r testpypi -u <user> -p <pass>
```

## Using Poetry in Existing Projects

- When Migrating you already have `requirements.txt` or `setup.py`.
- Use `poetry init` to create `pyproject.toml` interactively.  
- This will gradual adopt without rewriting everything.  
```bash
poetry init
# It will interactively build `pyproject.toml` from your current setup.
```

## Exporting Dependencies
* Some tools (like Docker or cloud providers) still expect `requirements.txt`.
* Poetry can export to pip-compatible format.
```bash
poetry export -f requirements.txt --output requirements.txt
```

## Integrating with Editors & IDEs
* **VS Code**: Select Poetry’s venv as the interpreter.  
* **PyCharm**: Supports Poetry environments directly.  
* Your editor runs code in the exact same environment as Poetry.
* Poetry manages paths automatically; IDEs detect them if properly configured.  

## CI/CD with Poetry
* Automated testing and deployments depend on consistent environments.  
* Poetry installs deps exactly as defined in the lock file.  
* **Sample workflow:** `.github/workflows/python-tests.yml`
```yaml
name: Python CI
on: [push, pull_request]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: "3.11"
      - run: curl -sSL https://install.python-poetry.org | python3 -
      - run: poetry install
      - run: poetry run pytest
```

## Best Practices
- Commit both `pyproject.toml` **and** `poetry.lock`.
- Use semantic versioning in dependencies (`^1.2` means compatible updates).
- Separate dev and prod dependencies.
- Export `requirements.txt` for Docker/cloud if needed.
- Use `poetry export` when targeting Docker/cloud or legacy systems.
- Stick to **`poetry run`** for commands to ensure correct environment.

##### [Back To Contents](../../README.md)
***
| &copy; TINITIATE.COM |
|----------------------|
