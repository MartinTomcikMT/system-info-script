from colorama import Fore, Style, init
import psutil
import platform

init(autoreset=True)  # automaticky resetuje farby

def get_system_info():
    print(Fore.RED + "=== SYSTEM INFORMATION ===")
    print(f"System: {platform.system()}")
    print(f"Node Name: {platform.node()}")

def get_cpu_info():
    print(Fore.YELLOW + "\n=== CPU INFO ===")
    print(f"CPU usage: {psutil.cpu_percent(interval=1)}%")

def get_memory_info():
    print(Fore.BLUE + "\n=== MEMORY INFO ===")
    memory = psutil.virtual_memory()
    print(f"Usage: {memory.percent}%")

def get_disk_info():
    print(Fore.GREEN + "\n=== DISK INFO ===")
    disk = psutil.disk_usage('/')
    print(f"Usage: {disk.percent}%")

def main():
    get_system_info()
    get_cpu_info()
    get_memory_info()
    get_disk_info()

if __name__ == "__main__":
    main()
