# TKScanner
![TKScanner](https://github.com/user-attachments/assets/86f8e257-315c-4cf3-94ad-1986cacec9ad)

**TKScanner** adalah alat berbasis Python yang dirancang untuk memindai dan menemukan tautan Dana Kaget melalui platform Threads. Program ini memudahkan pengguna untuk secara otomatis mencari link Dana Kaget menggunakan kata kunci yang ditentukan. TKScanner juga dapat secara otomatis membuka tautan yang ditemukan dan menyediakan opsi untuk menentukan jeda waktu antar link.

## Fitur
- **Pencarian Kustom**: Pengguna dapat memasukkan kata kunci pencarian atau menggunakan daftar kata kunci yang telah disediakan untuk menemukan tautan Dana Kaget.
- **Pembukaan Tautan Otomatis**: Pilih apakah ingin membuka tautan Dana Kaget secara otomatis atau tidak, dengan pengaturan jeda waktu yang fleksibel.
- **Pencarian Multi-Halaman**: Pilih untuk menelusuri lebih dari satu halaman atau hanya satu halaman hasil pencarian.
- **Antarmuka Pengguna Sederhana**: Program ini menggunakan antarmuka berbasis teks yang interaktif dan mudah diikuti.
- **Penanganan Kesalahan**: Program otomatis menangani kesalahan jaringan dan terus mencoba kembali.
- **Pelacakan Tautan**: TKScanner mencatat tautan yang telah diproses untuk menghindari pengulangan.

## Prasyarat
- Python 3.x (Python3.12 Recommended)
- Library Python:
    - `requests`
    - `rich`

## Instalasi
1. Clone repositori ini ke mesin lokal Anda:
    ```bash
    git clone https://github.com/RozhakXD/TKScanner.git
    ```
2. Pindah ke direktori proyek:
    ```bash
    cd TKScanner
    ```
3. Instal dependensi yang dibutuhkan:
    ```bash
    pip install -r requirements.txt
    ```
4. Jalankan program dengan perintah berikut:
    ```bash
    python Run.py
    ```

## Penanganan Error
- **Kesalahan Jaringan (RequestException)**: Jika terjadi masalah koneksi atau kesalahan HTTP, seperti _timeout_ atau _request failed_, program akan secara otomatis menangani kesalahan ini dengan menunggu beberapa detik (default 10 detik) sebelum mencoba kembali. Ini memastikan bahwa gangguan jaringan sementara tidak menghentikan operasi pencarian.
- **Kata Kunci Tidak Valid atau Tautan Tidak Ditemukan**: Jika tidak ada tautan yang ditemukan selama pencarian, program akan menampilkan pesan yang menunjukkan bahwa kata kunci yang digunakan mungkin tidak valid atau tidak relevan. Pengguna akan diberi opsi untuk mencoba kata kunci lain atau melanjutkan dengan kata kunci yang sama.
- **Kesalahan Cookie**: Jika cookie yang disediakan tidak valid atau tidak lengkap, program akan meminta pengguna untuk memastikan bahwa sesi autentikasi sudah benar.
- **Interupsi Pengguna (KeyboardInterrupt)**: Jika pengguna ingin menghentikan program saat sedang berjalan, mereka dapat menekan CTRL + C untuk memuat ulang atau CTRL + Z untuk menghentikan program sepenuhnya tanpa menyebabkan kerusakan pada proses yang sedang berjalan.

## Tangkapan Layar
![FunPic_20241009](https://github.com/user-attachments/assets/5344debd-c0fe-4b81-89fd-6f8766ee1b3f)

## Dukungan
Jika Anda ingin mendukung pengembangan proyek ini, Anda dapat memberikan dukungan melalui platform berikut:

- [Trakteer](https://trakteer.id/rozhak_official/tip)
- [PayPal](https://paypal.me/rozhak9)
- [Saweria](https://saweria.co/rozhak9)

## Demo Fitur Utama
![Video]()

## Kontribusi
Jika Anda ingin berkontribusi pada proyek ini, silakan fork repositori ini dan kirim pull request. Anda juga dapat melaporkan masalah atau permintaan fitur melalui tab Issues.

## Lisensi
Proyek ini dilisensikan di bawah MIT License - lihat file [LICENSE](https://github.com/RozhakXD/TKScanner/blob/main/LICENSE) untuk detail lebih lanjut.
