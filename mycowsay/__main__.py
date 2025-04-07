import cowsay
import sys

print(cowsay.cowsay(sys.version + "\n" + "\n".join(sys.path), width=80))
