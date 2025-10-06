# Python virtual environment for jaclang

This folder contains a minimal Python virtual environment setup.

Files added

- `requirements.txt` — list your pip dependencies here.
- `verify_env.py` — tiny script that prints "ok" and Python info.

Activate and use (PowerShell on Windows):

1. Create the venv (from the `jaclang` directory):

```powershell
python -m venv .venv
```

2. Activate the venv:

```powershell
# PowerShell (recommended)
.\.venv\Scripts\Activate.ps1

# Legacy cmd.exe
.\.venv\Scripts\activate.bat
```

3. Install dependencies:

```powershell
pip install -r requirements.txt
```

4. Verify:

```powershell
python verify_env.py
```

If you want a specific Python version (e.g., 3.11), ensure `python` points to that interpreter before creating the venv.
