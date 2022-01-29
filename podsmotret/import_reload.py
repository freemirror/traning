import importlib
import modul1
from modul1 import a
input()
importlib.reload(modul1)
print(modul1.c)
print(a)
print(dir(modul1))
