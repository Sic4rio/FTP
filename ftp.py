import ftplib
import argparse
import threading
import requests
import sys
import os
from colorama import Fore, Style
import signal

parser = argparse.ArgumentParser(description='FTP Anonymous Login Checker')
parser.add_argument('-u', '--url', help='URL of the file containing target IP addresses')
args = parser.parse_args()
target_list_url = args.url

welcome_message = f"""
{Fore.CYAN}
 █████╗ ███╗   ██╗ ██████╗ ███╗   ██╗███████╗████████╗██████╗ 
██╔══██╗████╗  ██║██╔═══██╗████╗  ██║██╔════╝╚══██╔══╝██╔══██╗
███████║██╔██╗ ██║██║   ██║██╔██╗ ██║█████╗     ██║   ██████╔╝
██╔══██║██║╚██╗██║██║   ██║██║╚██╗██║██╔══╝     ██║   ██╔═══╝ 
██║  ██║██║ ╚████║╚██████╔╝██║ ╚████║██║        ██║   ██║     
╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝        ╚═╝   ╚═╝ 
    FTP Anonymous Login Checker by SICARIO | 2023
{Style.RESET_ALL}
"""

def print_success(hostname):
    print(f"{Fore.GREEN}FTP Anonymous Logon Succeeded for Host: {hostname}{Style.RESET_ALL}")
    write_to_success_file(hostname)

def print_failure(hostname):
    print(f"{Fore.RED}FTP Anonymous Logon Failed for Host: {hostname}{Style.RESET_ALL}")

def anonlogin(hostname):
    try:
        ftp = ftplib.FTP(hostname)
        ftp.login()
        ftp.quit()
        print_success(hostname)
    except:
        print_failure(hostname)

def process_target(hostname):
    print(f"Processing target: {hostname}")
    anonlogin(hostname)

def read_targets_from_file(file_path):
    with open(file_path, 'r') as file:
        targets = file.read().splitlines()
    return targets

def read_targets_from_url(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            targets = response.text.splitlines()
            return targets
        else:
            print(f"{Fore.RED}Failed to retrieve target list from URL.{Style.RESET_ALL}")
            sys.exit(1)
    except requests.exceptions.RequestException:
        print(f"{Fore.RED}Failed to connect to the URL.{Style.RESET_ALL}")
        sys.exit(1)

def create_success_file():
    file_number = 0
    while True:
        file_name = f"success{file_number}.txt"
        if not os.path.isfile(file_name):
            return file_name
        file_number += 1

def write_to_success_file(hostname):
    success_file = create_success_file()
    with open(success_file, 'a') as file:
        file.write(f"{hostname}\n")

# Print the welcome message and banner
print(welcome_message)

# Keyboard interruption handling
def keyboard_interrupt_handler(signal, frame):
    print("\nKeyboardInterrupt")
    sys.exit(0)

signal.signal(signal.SIGINT, keyboard_interrupt_handler)

if target_list_url:
    # Read targets from URL
    targets = read_targets_from_url(target_list_url)
    for target in targets:
        threading.Thread(target=process_target, args=(target,)).start()
else:
    # Prompt the user for the file location or single target IP address
    file_location = input(f"{Fore.YELLOW}Enter the file location containing target IP addresses (or enter a single IP address): {Style.RESET_ALL}")
    if os.path.isfile(file_location):
        targets = read_targets_from_file(file_location)
        for target in targets:
            threading.Thread(target=process_target, args=(target,)).start()
    else:
        threading.Thread(target=process_target, args=(file_location,)).start()
