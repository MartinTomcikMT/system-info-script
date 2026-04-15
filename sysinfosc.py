# library for work with system information data (CPU, RAM, disk)
import psutil 

# library for work with OS infarmations
import platform 

# function to get system info
def get_system_info():
  print("=== SYSTEM INFORMATION ===") 
  print(f"System: {platform.system()}") 
  print(f"Node Name: {platform.node()}") 
  print(f"Release: {platform.release()}") 
  print(f"Version: {platform.version()}") 
  print(f"Machine: {platform.machine()}") 
  print(f"Processor: {platform.processor()}") 

# function to get cpu
def get_cpu_info():
  print("\n=== CPU INFO ===") 
  print(f"CPU usage: {psutil.cpu_percent()}%") 

# function to get memory info
def get_memory_info():
  print("\n=== MEMORY INFO ===") 
  memory = psutil.virtual_memory() 
  print(f"Total: {round(memory.total / (10243), 2)} GB") 
  print(f"Used: {round(memory.used / (10243), 2)} GB") 
  print(f"Usage: {memory.percent}%") 

# function to get disk info
def get_disk_info():
  print("\n=== DISK INFO ===") 
  disk = psutil.disk_usage('/') 
  print(f"Total: {round(disk.total / (10243), 2)} GB") 
  print(f"Used: {round(disk.used / (10243), 2)} GB") 
  print(f"Usage: {disk.percent}%")

# main function to collect all data
def main():
  get_system_info() 
  get_cpu_info()
  get_memory_info()
  get_disk_info() 

if name == "main": 

# run main function
main() 
