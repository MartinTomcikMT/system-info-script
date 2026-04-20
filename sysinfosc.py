# Import required libraries
from colorama import Fore, Style, init
import psutil
import platform
import datetime
import os

# Initialize colorama (auto reset colors after each print)
init(autoreset=True)

# Width of the UI box
WIDTH = 90

# ASCII banner displayed at the top
ASCII_ART = r"""
   _____           _                   _____        __         _____           _       _
  / ____|         | |                 |_   _|      / _|       / ____|         (_)     | |
 | (___  _   _ ___| |_ ___ _ __ ___     | |  _ __ | |_ ___   | (___   ___ _ __ _ _ __ | |_
  \___ \| | | / __| __/ _ \ '_ ` _ \    | | | '_ \|  _/ _ \   \___ \ / __| '__| | '_ \| __|
  ____) | |_| \__ \ ||  __/ | | | | |  _| |_| | | | || (_) |  ____) | (__| |  | | |_) | |_
 |_____/ \__, |___/\__\___|_| |_| |_| |_____|_| |_|_| \___/  |_____/ \___|_|  |_| .__/ \__|
          __/ |                                                                 | |
         |___/                                                                  |_|
"""

# Print ASCII art in red color
def print_ascii_art():
    print(Fore.RED + ASCII_ART + Style.RESET_ALL)

# Print full horizontal line
def print_line():
    print("=" * WIDTH)

# Print empty line with borders
def print_empty():
    print("=" + " " * (WIDTH - 2) + "=")

# Print centered text inside a bordered line
def print_center(text, color):
    visible_text = text.center(WIDTH - 4)
    print("=" + f" {color}{visible_text}{Style.RESET_ALL} " + "=")

# Print left-aligned label and value inside a bordered line
def print_left(label, value, color):
    raw_text = f"{label}: {value}"

    # Trim text if it's too long
    if len(raw_text) > WIDTH - 4:
        raw_text = raw_text[:WIDTH - 7] + "..."

    visible_text = raw_text.ljust(WIDTH - 4)

    # Color only the label
    colored_label = f"{color}{label}{Style.RESET_ALL}"
    colored_text = visible_text.replace(label, colored_label, 1)

    print("=" + f" {colored_text} " + "=")

# Display system information
def get_system_info():
    section_color = Fore.RED
    clear_screen()
    print_ascii_art()

    print_line()
    print_center("SYSTEM INFORMATION", section_color)
    print_empty()

    # Basic system details
    print_left("System", platform.system(), section_color)
    print_left("Node Name", platform.node(), section_color)
    print_left("Release", platform.release(), section_color)
    print_left("Version", platform.version(), section_color)
    print_left("Machine", platform.machine(), section_color)
    print_left("Processor", platform.processor(), section_color)

    # System boot time
    boot_time = datetime.datetime.fromtimestamp(psutil.boot_time())
    print_left("Boot Time", boot_time, section_color)

    print_empty()
    print_line()

# Display CPU information
def get_cpu_info():
    section_color = Fore.GREEN
    clear_screen()
    print_ascii_art()

    print_line()
    print_center("CPU INFO", section_color)
    print_empty()

    # CPU usage and number of cores
    print_left("CPU Usage", f"{psutil.cpu_percent(interval=1)}%", section_color)
    print_left("CPU Count", psutil.cpu_count(), section_color)

    print_empty()
    print_line()

# Display memory (RAM and swap) information
def get_memory_info():
    section_color = Fore.BLUE
    clear_screen()
    print_ascii_art()

    print_line()
    print_center("MEMORY INFO", section_color)
    print_empty()

    memory = psutil.virtual_memory()
    swap = psutil.swap_memory()

    # Memory usage statistics
    print_left("Memory Usage", f"{memory.percent}%", section_color)
    print_left("Swap Usage", f"{swap.percent}%", section_color)

    print_empty()
    print_line()

# Display disk usage information
def get_disk_info():
    section_color = Fore.YELLOW
    clear_screen()
    print_ascii_art()

    print_line()
    print_center("DISK INFO", section_color)
    print_empty()

    # Disk usage for root directory
    disk = psutil.disk_usage('/')
    print_left("Disk Usage", f"{disk.percent}%", section_color)

    print_empty()
    print_line()

# Show main menu
def show_menu():
    clear_screen()
    print_ascii_art()
    print("\nChoose what information you want to see:")
    print("s - System information")
    print("c - CPU information")
    print("m - Memory information")
    print("d - Disk information")
    print("e - Exit")

# Clear terminal screen (Windows/Linux/Mac)
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Main program loop
def main():
    while True:
        show_menu()
        choice = input("\nYour choice: ").strip().lower()

        # Handle user input
        if choice == "s":
            get_system_info()
            input("\nPress Enter to continue...")
        elif choice == "c":
            get_cpu_info()
            input("\nPress Enter to continue...")
        elif choice == "m":
            get_memory_info()
            input("\nPress Enter to continue...")
        elif choice == "d":
            get_disk_info()
            input("\nPress Enter to continue...")
        elif choice == "e":
            clear_screen()
            print_ascii_art()
            print("Exiting program...")
            break
        else:
            clear_screen()
            print_ascii_art()
            print("Invalid choice. Please try again.")
            input("\nPress Enter to continue...")

# Run the program
if __name__ == "__main__":
    main()
