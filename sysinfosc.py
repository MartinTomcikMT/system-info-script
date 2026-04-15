from colorama import Fore, init
import psutil
import platform
import datetime

init(autoreset=True)

def get_system_info():
    print(Fore.RED + "=== SYSTEM INFORMATION ===")
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

    print(f"Usage: {memory.percent}%")
    print(f"Swap usage: {swap.percent}%")

def get_disk_info():
    print(Fore.GREEN + "\n=== DISK INFO ===")
    disk = psutil.disk_usage('/')

    print(f"Usage: {disk.percent}%")
    print(f"Partitions: {psutil.disk_partitions()}")

def main():
    get_system_info()
    get_cpu_info()
    get_memory_info()
    get_disk_info()

if __name__ == "__main__":
    main()
