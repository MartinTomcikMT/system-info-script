# First I need to import appropriate libraries to get desired data, platform is already part of Python standard library, others must be installed (pip install psutil colorama)

from colorama import Fore, Style, init
import psutil
import platform
import datetime
import os

# Initialize colorama
init(autoreset=True)

# Box width for formatting
WIDTH = 80

# Helper functions for nice formatting
def print_line():
print("=" * WIDTH)

def print_empty():
print("=" + " " * (WIDTH - 2) + "=")

def print_center(text):
print("=" + text.center(WIDTH - 2) + "=")

def print_left(label, value):
text = f"{label}: {value}"
print("=" + f" {text:<{WIDTH - 3}}" + "=")

# SYSTEM INFO
def get_system_info():
print_line()
print_center(Fore.RED + "SYSTEM INFORMATION" + Style.RESET_ALL)
print_empty()

```
print_left("System", platform.system())
print_left("Node Name", platform.node())
print_left("Release", platform.release())
print_left("Version", platform.version())
print_left("Machine", platform.machine())
print_left("Processor", platform.processor())

boot_time = datetime.datetime.fromtimestamp(psutil.boot_time())
print_left("Boot Time", boot_time)

print_empty()
print_line()
```

# CPU INFO
def get_cpu_info():
print_line()
print_center(Fore.YELLOW + "CPU INFO" + Style.RESET_ALL)
print_empty()

```
print_left("CPU Usage", f"{psutil.cpu_percent(interval=1)}%")
print_left("CPU Count", psutil.cpu_count())

print_empty()
print_line()
```

# MEMORY INFO

def get_memory_info():
print_line()
print_center(Fore.BLUE + "MEMORY INFO" + Style.RESET_ALL)
print_empty()

```
memory = psutil.virtual_memory()
swap = psutil.swap_memory()

print_left("Memory Usage", f"{memory.percent}%")
print_left("Swap Usage", f"{swap.percent}%")

print_empty()
print_line()
```

# DISK INFO

def get_disk_info():
print_line()
print_center(Fore.GREEN + "DISK INFO" + Style.RESET_ALL)
print_empty()

```
disk = psutil.disk_usage('/')
print_left("Disk Usage", f"{disk.percent}%")

print_empty()
print_line()
```

# MENU

def show_menu():
print("\nChoose what information you want to see:")
print("s - System information")
print("c - CPU information")
print("m - Memory information")
print("d - Disk information")
print("e - Exit")

def clear_screen():
os.system('cls' if os.name == 'nt' else 'clear')

# MAIN LOOP

def main():
while True:
show_menu()
choice = input("\nYour choice: ").strip().lower()

```
    if choice == "s":
        clear_screen()
        get_system_info()
    elif choice == "c":
        clear_screen()
        get_cpu_info()
    elif choice == "m":
        clear_screen()
        get_memory_info()
    elif choice == "d":
        clear_screen()
        get_disk_info()
    elif choice == "e":
        print("Exiting program...")
        break
    else:
        clear_screen()
        print("Invalid choice. Please try again.")
```

if **name** == "**main**":
main()
