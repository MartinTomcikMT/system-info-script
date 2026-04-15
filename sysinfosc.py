import psutil
import platform

def get_system_info():
    print("=== SYSTEM INFORMATION ===")
    print(f"System: {platform.system()}")
    print(f"Node Name: {platform.node()}")
    print(f"Release: {platform.release()}")
    print(f"Version: {platform.version()}")
    print(f"Machine: {platform.machine()}")
    # print(f"Processor: {platform.processor()}")  # dočasne vypnuté

def get_cpu_info():
    print("\n=== CPU INFO ===")
    print(f"CPU usage: {psutil.cpu_percent(interval=1)}%")

def get_memory_info():
    print("\n=== MEMORY INFO ===")
    memory = psutil.virtual_memory()
    print(f"Total: {round(memory.total / (1024**3), 2)} GB")
    print(f"Used: {round(memory.used / (1024**3), 2)} GB")
    print(f"Usage: {memory.percent}%")

def get_disk_info():
    print("\n=== DISK INFO ===")
    disk = psutil.disk_usage('/')
    print(f"Total: {round(disk.total / (1024**3), 2)} GB")
    print(f"Used: {round(disk.used / (1024**3), 2)} GB")
    print(f"Usage: {disk.percent}%")

def main():
    print("Starting script...")
    get_system_info()
    get_cpu_info()
    get_memory_info()
    get_disk_info()
    print("\nDone.")

if __name__ == "__main__":
    main()
