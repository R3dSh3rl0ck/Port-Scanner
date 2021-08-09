import concurrent.futures
import re
import socket
# for time of execution
import threading
import time
from datetime import timedelta
#  pip install IPy (Convert domain-TLD --> IPv4)
from IPy import IP
from colorama import Fore
# for regula expressions
# Reset the Color after use
from colorama import init

init(autoreset=True)


# scan_all function Output of the operation
def scan_all(target):
    # converted ip
    converted_target = ip_domain(target)
    # Target with Red color
    print('\n' + Fore.RED + '[+] Scanning Target : ' + str(target))
    # enter a valid port range. check!
    while True:
        port_range = input('[+] Enter the port range(1 - 65535) you want to scan ( format [int]-[int] ) : ')
        port_range_valid = port_valid.search(port_range.replace(" ", ""))
        if port_range_valid:
            port_min = int(port_range_valid.group(1))
            port_max = int(port_range_valid.group(2))
            break
    # scan every port
    # Multithreading programming for speed. (100 threads very fast results) (change it to your needs)
    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        for port in range(port_min, port_max + 1):
            executor.submit(scan, converted_target, port)


# Function to convert domain-TLD to IPv4
def ip_domain(target):
    try:
        IP(target)
        return (target)
    except ValueError:
        return socket.gethostbyname(target)


# Create socket for connection!
def scan(target, port):
    lock = threading.Lock
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # it take 0.5 secs to connect to a port !
        s.settimeout(0.5)
        s.connect((target, port))
        try:
            # banner
            banner = get_banner(s)
            # Add lock. Because when multiple threads are running make sure they do not print the same result
            with lock:
                print(Fore.GREEN + f'[+] Open port {port} : ' + str(banner.decode().strip('\n')))
        except:
            with lock:
                print(Fore.GREEN + f'[+] Open port {port}')
    except:
        pass


# function for the banner
def get_banner(s):
    data = s.recv(1024)
    return data


# Main!
if __name__ == '__main__':
    print(r"""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~          
*             _____   ____     ____     ____                  #
*            /       |    \     /|     /    \                 #
*           |        |     |   / |     \    /                 #
*             \      |    /      |      \__/                  #
*               |    |  /        |     /    \                 #   
*                /   |  \        |     \    /                 #
*          _____/    |    \    __|__    \__/                  #
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~""")
    print('\n***************************************************************')
    print('* ShadowRoot18                                                *')
    print('* Simple Port Scanner                                         *')
    print('* Operation : scan single or Multiple targets for open ports! *')
    print('***************************************************************\n')
    # threading lock . Not different threads prints same stuff! lock = threading.Lock()
    # special format for ports.
    port_valid = re.compile("([0-9]+)-([0-9]+)")
    # Minimum port number
    port_min = 0
    # Maximum port number
    port_max = 65535
    # Run forever except exit!
    while True:
        # IP
        choice = input('[+] For Domain-TLD name or IPv4 addresses  press [1] ('
                       'Multiple '
                       'targets + IPs)\n[+] For Exit press [0]\n[+] Input : ')
        if choice == '1':
            while True:
                targets = input(
                    '[+] Enter Target/s . Ex --> google.com,10.10.0.2 . '
                    '(Enter '
                    'multiple targets by '
                    'splitting them with '
                    ', ) : ')

                if targets == '':
                    print('[-] This field can not be blank! \n')
                else:
                    break
            # Start point of operation
            start_time = time.monotonic()
            if ',' in targets:
                for ip in targets.split(','):
                    scan_all(ip.strip(' '))
            else:
                scan_all(targets)
            # End point of operation
            end_time = time.monotonic()
            print('\n' + Fore.RESET + 'Time of execution : ' + str(timedelta(seconds=end_time - start_time)) + '\n')
        elif choice == '0':
            print('Exiting..')
            break
        else:
            # Check for valid values 0 or 1 !

            print(Fore.RED + '[-] Please enter a valid value!\n')
