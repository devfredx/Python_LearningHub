import subprocess
import sys
import importlib.metadata

def get_pip_version():
    return subprocess.check_output([sys.executable, "-m", "pip", "--version"]).decode()

print(get_pip_version())

installed_packages = importlib.metadata.distributions()
for dist in installed_packages:
    print(f"{dist.metadata['Name']} == {dist.version}")

def install_package(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def uninstall_package(package):
    subprocess.check_call([sys.executable, "-m", "pip", "uninstall", "-y", package])

pip_commands = {
    "install": "pip install requests",
    "upgrade": "pip install --upgrade pip",
    "list": "pip list",
    "freeze": "pip freeze > requirements.txt",
    "install_req": "pip install -r requirements.txt",
    "show": "pip show requests",
    "search": "pip search flask",
    "check": "pip check"
}

for cmd_name, cmd_syntax in pip_commands.items():
    print(f"{cmd_name}: {cmd_syntax}")

try:
    import requests
    print("Requests version:", requests.__version__)
except ImportError:
    print("Requests is not installed.")

def check_outdated():
    return subprocess.check_output([sys.executable, "-m", "pip", "list", "--outdated"]).decode()

print(get_pip_version())