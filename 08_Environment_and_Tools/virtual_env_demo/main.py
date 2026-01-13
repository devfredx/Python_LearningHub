import os
import sys
import subprocess

def check_venv():
    is_venv = sys.prefix != sys.base_prefix
    print(f"Is Virtual Environment Active: {is_venv}")
    print(f"Current Python Path: {sys.executable}")
    print(f"System Prefix: {sys.prefix}")

check_venv()

venv_commands = {
    "create_windows": "python -m venv venv",
    "create_mac_linux": "python3 -m venv venv",
    "activate_windows": ".\venv\Scripts\activate",
    "activate_bash": "source venv/bin/activate",
    "deactivate": "deactivate",
    "save_requirements": "pip freeze > requirements.txt",
    "install_requirements": "pip install -r requirements.txt"
}

for action, command in venv_commands.items():
    print(f"{action.upper()}: {command}")

def create_environment(name="test_env"):
    subprocess.run([sys.executable, "-m", "venv", name])

print(os.environ.get('VIRTUAL_ENV', 'No active virtual environment detected in env vars'))

site_packages = [p for p in sys.path if 'site-packages' in p]
print(site_packages)

if hasattr(sys, 'real_prefix') or (sys.base_prefix != sys.prefix):
    print("Running inside a virtual environment context.")
else:
    print("Running in global Python environment.")