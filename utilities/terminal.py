from os import system, name
from colorama import init, Fore, Back

init()

def clear():
    if name == "nt":
        system('cls')
    else:
        system('clear')

def print_color(text:str, color:str) -> None:
  print(eval(f"Fore.{color}"),text)
  print(Fore.WHITE)

def banner():
    with open("helpers/ascii.txt","r", encoding="utf-8") as ascii:
        print(ascii.read())
