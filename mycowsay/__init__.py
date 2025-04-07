import cowsay
import sys

def say_python():
    text = f"{sys.version} \r Modules in : [{', '.join(sys.path)}]"
    print(cowsay.cowsay(text, width=80))
