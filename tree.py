from colorama import init
init()
from colorama import Fore, Back, Style

# print(Fore.RED + "test")
# print(Back.GREEN + 'with green background')
# print(Style.DIM + "in dim text")
# print(Style.RESET_ALL)

size = 30

for i in range(0, size):
    if i==0:
        print(Fore.YELLOW + "★".center(size, " "))
    print(Fore.GREEN + ("*"*i).center(size, " "))

init(autoreset=True)
print(Fore.WHITE)
print(Back.RED + "Merry Christmas".center(size, " "))
print()
for i in range(5):
    print(Fore.WHITE + ("■".center(size, " ")))