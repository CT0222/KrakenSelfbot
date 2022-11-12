from os import system, name
from requests import get

def clear():
    if name in ("nt", "dos"):
      system("cls")
    else:
      system("clear")
