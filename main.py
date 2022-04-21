import os
import time
import colorama
from colorama import Fore

logo = """
______           ______          _ 
| ___ \          | ___ \        | |
| |_/ /__ _ _   _| |_/ /___   __| |
|    // _` | | | |    // _ \ / _` |
| |\ \ (_| | |_| | |\ \ (_) | (_| |
\_| \_\__,_|\__, \_| \_\___/ \__,_|
             __/ |                 
            |___/              
"""


def menu():
  print(Fore.BLUE + logo)
  print('[1] Uncompile Pyinstaller / Pyarmor Executable File')
  print('[2] Uncompile .pyc file')
  var = int(input('\n>> '))
  if var == 1:
    T = input(f'{Fore.GREEN}\n[~] Enter the directory of the .exe (e.g: /Desktop/app.exe/): ')
    if os.path.exists(T):
      print('')
      os.system(f"python3 modules/pyinstxtractor.py {T}")
    #print('')
    else:
      print(f'{Fore.RED}\n[!] Directory does not exist')
      time.sleep(2)
      menu()
  elif var == 2:
    T = input(f'{Fore.GREEN}\n[~] Enter the directory of the .exe (e.g: /Desktop/compile.pyc/): ')
    if os.path.exists(T):
      print('')
      os.system(f"uncompyle6 {T}")
    else:
      print(f'{Fore.RED}\n[!] Directory does not exist')
      time.sleep(2)
      menu()
  else:
    print(f'{Fore.RED}\n[!] Wrong Option.')
    time.sleep(2)
    menu()

menu()
