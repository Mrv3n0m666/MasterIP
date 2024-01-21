import ipaddress

def cidr_to_ips(cidr):
    ip_list = [str(ip) for ip in ipaddress.IPv4Network(cidr, strict=False)]
    return ip_list

def process_cidr_file(input_file, output_file):
    with open(input_file, 'r') as file:
        cidr_lines = file.readlines()

    with open(output_file, 'w') as output:
        for cidr_line in cidr_lines:
            cidr = cidr_line.strip()
            ip_list_result = cidr_to_ips(cidr)
            output.write(f"\nDaftar Alamat IP untuk {cidr}:\n")
            for ip in ip_list_result:
                output.write(ip + '\n')

# Input dan Output file
input_file_name = input("Masukkan nama file yang berisi CIDR (contoh: input.txt): ")
output_file_name = input("Masukkan nama file untuk menyimpan hasil (contoh: output.txt): ")

# Proses konversi CIDR
process_cidr_file(input_file_name, output_file_name)

print(f"\nHasil konversi CIDR telah disimpan di {output_file_name}")
