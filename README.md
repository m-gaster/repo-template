# Template Project

This is a template project set up with Poetry.

## Instructions (remove this after setup)

1. **Clone this project** (or a project that used this as a template):

2. **Install Poetry** if you haven't already. You can do this by running either:
    ```bash
    curl -sSL https://install.python-poetry.org | python3 -
    ```
    or
    ```bash
    pip install poetry
    # or
    pip3 install poetry
    ```

3. **Navigate to this repository in a terminal**:

4. **Rename the `src/template` directory to your desired package name**:

5. **Update the `pyproject.toml` file**:
    - Update the authors, description, etc.
    - Change the `name` field under `[tool.poetry]` to your project name.
    - Update the `packages` section to reflect the new package name. For example, if you rename `template` to `my_project`, update it as follows:
    ```toml
    packages = [
        { include = "my_project", from = "src" }
    ]
    ```

6. **Create and activate a virtual environment** (optional; poetry will use a pre-existing environment if allowed & possible):
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```

6. **Run `poetry install` to install the dependencies**:
    ```bash
    poetry install --sync
    ```

***

# Your readme


## Setup Instructions
1. **Clone this project** (or a project that used this as a template):

2. **Install Poetry** if you haven't already. You can do this by running either:
    ```bash
    curl -sSL https://install.python-poetry.org | python3 -
    ```
    or
    ```bash
    pip install poetry
    # or
    pip3 install poetry
    ```

3. **Navigate to this repository in a terminal**:

4. **Create and activate a virtual environment** (optional; poetry will ):
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```

6. **Run `poetry install` to install the dependencies**:
    ```bash
    poetry install --sync
    ```

7. **Run _________________**:
    ```bash
    ```
