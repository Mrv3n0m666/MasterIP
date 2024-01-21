# MasterIP Valdiator
===========================

Script ini adalah alat validasi IP dan domain yang memungkinkan Anda untuk memeriksa keberlanjutan IP dan nama domain pada suatu port tertentu. Dengan menggunakan multithreading, script ini dapat memproses daftar IP dan domain secara bersamaan, meningkatkan efisiensi proses validasi.

## Installation
```
pip install -r requirements.txt
 ```
## USAGE
 ```
python3 MasterIP.py
 ```

 ![image](https://github.com/Mrv3n0m666/MasterIP/assets/157101186/5c85800d-1014-4aa9-8868-401b99a110c1)

 ## Fitur:
- Validasi IP dan Domain : Menentukan apakah suatu IP atau domain aktif pada port tertentu.
- Multithreading: Mempercepat proses validasi dengan menjalankan beberapa thread secara bersamaan.
- Output yang Diformat: Menyajikan hasil validasi dengan warna untuk memudahkan interpretasi.
- Simpan Hasil: Hasil validasi IP dan domain yang hidup disimpan dalam file "live_results.txt".

## Cara Menggunakan:

- Jalankan script.
- Masukkan nama file yang berisi daftar IP dan domain yang akan divalidasi.
- Tentukan port yang ingin Anda validasi.
- Pilih jumlah thread yang ingin Anda gunakan untuk mempercepat proses.
- Hasil validasi akan ditampilkan secara langsung dan disimpan dalam file "live_results.txt" di folder 'result'.

## Catatan:

Jangan lupa untuk menyiapkan daftar IP dan domain yang akan divalidasi sebelum menjalankan script.
Pastikan bahwa modul-modul yang dibutuhkan seperti socket, requests, concurrent.futures, dan colorama sudah terinstal.
Dengan menggunakan script ini, Anda dapat dengan cepat memverifikasi status keberlanjutan IP dan domain yang terdaftar dalam file, sambil menyimpan hasilnya untuk referensi selanjutnya.
