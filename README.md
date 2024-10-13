Disusun Oleh

Aditya Eka Nanda 320220401001

I Made Aditya Pradana Putra 320220401007

Nisrina Labiba Sarwoko 320220401020

# Client-Server-Communication-Model

# Gambaran Proyek
Proyek ini mengimplementasikan arsitektur client-server dengan load balancer untuk mendistribusikan permintaan ke beberapa server. Proyek ini terdiri dari beberapa komponen:

**Client** : Client terhubung ke load balancer, mengirim pesan, dan menerima respons. Client menghitung latensi, waktu respons, dan throughput untuk komunikasi.

**Load Balancer** : Load balancer mendengarkan koneksi dari client dan meneruskan permintaan ke salah satu server yang tersedia. Load balancer mendistribusikan beban berdasarkan logika yang sudah ditentukan.

**Server** : Beberapa server mendengarkan koneksi dari load balancer dan merespons pesan client. Setiap server mencatat pesan yang diterima dan membalas dengan konfirmasi.

# Deskripsi File

## client2.py

Script yang mensimulasikan beberapa client yang terhubung ke load balancer.
Setiap client mengirim pesan, menerima respons, dan menghitung metrik kinerja seperti latensi, waktu respons, dan throughput.
Jalankan script client dengan menentukan jumlah client yang akan dimulai.

## load_balancer.py

Load balancer yang meneruskan permintaan client ke server yang tersedia pada port yang berbeda (9991, 9992, dan 9993).
Mendengarkan pada port 9990 untuk koneksi dari client dan mendistribusikannya ke server.

## server2.py

Script server yang mendengarkan koneksi dari load balancer pada port 9991, 9992, atau 9993.
Menangani beberapa client menggunakan thread, mencatat pesan, dan merespons dengan konfirmasi.

# Instruksi Penggunaan

## 1. Menjalankan Server
Jalankan server pada port 9991, 9992, dan 9993. Setiap server harus dijalankan di terminal atau proses yang berbeda:
``` Phyton
python server2.py 9991
python server2.py 9992
python server2.py 9993
```
## 2. Menjalankan Load Balancer
Jalankan load balancer, yang akan mendengarkan pada port 9990:
``` Phyton
python load_balancer.py
```
## 3. Menjalankan Client
Terakhir, jalankan script client dan tentukan jumlah client:
``` Phyton
python client2.py <jumlah_client>
```
# Metrik Kinerja
Client menghitung metrik kinerja berikut untuk setiap komunikasi dengan server:

**Latensi** : Waktu yang dibutuhkan untuk pesan mencapai server dan menerima balasan.

**Waktu Respons** : Total waktu yang dibutuhkan untuk mengirim pesan dan menerima balasan.

**Throughput** : Jumlah data yang ditransfer per detik, berdasarkan ukuran pesan dan respons.

# Logging
Setiap server mencatat detail koneksi, pesan yang diterima, dan balasan dalam file bernama server_log.txt.






