from tools.system_tools import *

from tools.registry import listar

print()

print("Herramientas registradas:")

for herramienta in listar():
    print("-", herramienta)