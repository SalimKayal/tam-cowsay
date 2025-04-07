import cowsay
import sys

def say_python():
    with open('/etc/os-release', 'r') as os:
        text = f"OS: {os.read()}\n\rPython: {sys.version}\n\rModules in : [{', '.join(sys.path)}]"
    print(cowsay.cowsay(text, width=80))
