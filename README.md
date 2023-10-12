# Setup

# 1. create and activate virtualenv

```sh
python -m venv venv
source venv/bin/activate
# source venv/Scripts/activate for windows; you may have to run "Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope LocalMachine" in PowerShell as admin first (due to Windows security policy)
```

# 2. install dependencies

```sh
pip install -r requirements-dev.txt -r requirements.txt
```

# 3. install pre-commit hooks

```sh
pre-commit install
```
