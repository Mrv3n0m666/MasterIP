import os
import socket
import requests
from concurrent.futures import ThreadPoolExecutor
from colorama import init, Fore, Style

init(autoreset=True)

def display_colored_banner():
    banner = '''
    {}
       • ▌ ▄ ·.  ▄▄▄· .▄▄ · ▄▄▄▄▄▄▄▄ .▄▄▄      ▪   ▄▄▄·
       ·██ ▐███▪▐█ ▀█ ▐█ ▀. •██  ▀▄.▀·▀▄ █·    ██ ▐█ ▄█
       ▐█ ▌▐▌▐█·▄█▀▀█ ▄▀▀▀█▄ ▐█.▪▐▀▀▪▄▐▀▀▄     ▐█· ██▀·
       ██ ██▌▐█▌▐█ ▪▐▌▐█▄▪▐█ ▐█▌·▐█▄▄▌▐█•█▌    ▐█▌▐█▪·•
       ▀▀  █▪▀▀▀ ▀  ▀  ▀▀▀▀  ▀▀▀  ▀▀▀ .▀  ▀    ▀▀▀.▀ 

{}     ▂▃▄▅▆▇▓▒░IP and Domain Validator by Mr.D░▒▓▇▆▅▄▃▂ 
    {}'''.format(Fore.RED, Fore.GREEN, Style.RESET_ALL)

    print(banner)

# Membuat folder "result" jika belum ada
if not os.path.exists("result"):
    os.makedirs("result")

# Panggil fungsi untuk menampilkan banner
display_colored_banner()

# Mulai skrip Anda di sini...

def is_ip_live(ip, port):
    try:
        with socket.create_connection((ip, port), timeout=2):
            return True
    except (socket.timeout, ConnectionRefusedError):
        return False

def is_domain_live(domain, port):
    try:
        response = requests.get(f"http://{domain}", timeout=2)
        return response.status_code == 200
    except requests.RequestException:
        return False

def validate_item(item, port):
    # Cek apakah item adalah alamat IP atau nama domain
    if ":" in item:
        ip = item.split(":")[0]
        is_valid = is_ip_live(ip, port)
        status = f"{Fore.RED}[\u2717]{Fore.RESET} {item} {Fore.RED}INVALID{Fore.RESET}" if not is_valid else f"{Fore.GREEN}[{Fore.RESET}\u2713{Fore.GREEN}]{Fore.RESET} {item} {Fore.GREEN}VALID{Fore.RESET}"
        return is_valid, status
    else:
        is_valid = is_domain_live(item, port)
        status = f"{Fore.RED}[\u2717]{Fore.RESET} {item} {Fore.RED}INVALID{Fore.RESET}" if not is_valid else f"{Fore.GREEN}[{Fore.RESET}\u2713{Fore.GREEN}]{Fore.RESET} {item} {Fore.GREEN}VALID{Fore.RESET}"
        return is_valid, status

def validate_ips_and_domains(items_list, port, num_threads):
    live_results = []

    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        # Mengeksekusi fungsi validate_item secara bersamaan
        futures = [executor.submit(validate_item, item, port) for item in items_list]

        try:
            for future in futures:
                is_valid, status = future.result()
                print(status)

                # Menyimpan hasil validasi ke dalam file
                with open(os.path.join("result", "live_results.txt"), "a") as output_file:
                    output_file.write(status.split()[1] + "\n")

        except KeyboardInterrupt:
            print("Proses validasi dihentikan dengan paksa. Menyimpan hasil yang telah divalidasi sejauh ini...")

    return live_results

# Meminta input nama file dari pengguna
file_name = input("Mana list na (contoh: resultip.txt): ")

# Baca daftar alamat IP dan nama domain dari file
with open(file_name, "r") as file:
    items_list = [line.strip() for line in file]

# Meminta input port yang ingin divalidasi
port_to_check = int(input("Rek ngvalid di port Braha?: "))

# Meminta input jumlah thread yang diinginkan
num_threads = int(input("Masukkan jumlah thread yang diinginkan: "))

# Validasi alamat IP dan nama domain pada port yang dimasukkan
live_results = validate_ips_and_domains(items_list, port_to_check, num_threads)

print("Hasil validasi nama domain dan alamat IP yang hidup telah disimpan di file 'live_results.txt' di folder 'result'.")
