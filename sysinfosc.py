from colorama import Fore, Style, init
import psutil
import platform
import datetime
import os

init(autoreset=True)


def get_system_info():
    print("========================= " + Fore.RED + "SYSTEM INFORMATION" + Style.RESET_ALL + " =========================")
    print(f"System: {platform.system()}")
    print(f"Node Name: {platform.node()}")

    boot_time = datetime.datetime.fromtimestamp(psutil.boot_time())
    print(f"Boot time: {boot_time}")


def get_cpu_info():
    print(Fore.YELLOW + "\n=== CPU INFO ===")
    print(f"CPU usage: {psutil.cpu_percent(interval=1)}%")
    print(f"CPU count: {psutil.cpu_count()}")


def get_memory_info():
    print(Fore.BLUE + "\n=== MEMORY INFO ===")
    memory = psutil.virtual_memory()
    swap = psutil.swap_memory()

    print(f"Memory usage: {memory.percent}%")
    print(f"Swap usage: {swap.percent}%")


def get_disk_info():
    print(Fore.GREEN + "\n=== DISK INFO ===")
    disk = psutil.disk_usage('/')

    print(f"Disk usage: {disk.percent}%")
    print(f"Partitions: {psutil.disk_partitions()}")


def show_menu():
    print("\nChoose what information you want to see:")
    print("s - System information")
    print("c - CPU information")
    print("m - Memory information")
    print("d - Disk information")
    print("e - Exit")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    while True:
        show_menu()
        choice = input("\nYour choice: ").strip().lower()

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

if __name__ == "__main__":
    main()
