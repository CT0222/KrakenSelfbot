from os import system
from requests import get
from krk import *

clear()
print("Instalando...")
system("pip install -r requirements.txt")
clear()
print("Instalado")