# TKScanner
![TKScanner](https://github.com/user-attachments/assets/86f8e257-315c-4cf3-94ad-1986cacec9ad)

**TKScanner** adalah alat Python untuk memindai dan menemukan tautan Dana Kaget di Threads. Program ini otomatis mencari tautan berdasarkan kata kunci, membuka tautan yang ditemukan, serta menyediakan opsi pengaturan jeda waktu antar tautan.

## Fitur
- **Pencarian Kustom**: Pengguna dapat memasukkan kata kunci pencarian atau menggunakan daftar kata kunci yang telah disediakan untuk menemukan tautan Dana Kaget.
- **Pencarian Multi-Halaman**: Opsi untuk menelusuri satu atau beberapa halaman hasil pencarian.
- **Penanganan Kesalahan**: Program otomatis menangani kesalahan jaringan dan terus mencoba kembali.
- **Pelacakan Tautan**: TKScanner mencatat tautan yang telah diproses untuk menghindari pengulangan.
- **Pembukaan Tautan Otomatis**: Pilih apakah ingin membuka tautan Dana Kaget secara otomatis atau tidak, dengan pengaturan jeda waktu yang fleksibel.

## Prasyarat
- Library Python:
    - `requests`
    - `rich`
- Python 3.12

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

## Tangkapan Layar
![FunPic_20241009](https://github.com/user-attachments/assets/5344debd-c0fe-4b81-89fd-6f8766ee1b3f)

## Troubleshooting
- **Masalah RequestException**: Jika Anda mengalami kesalahan `RequestException`, periksa koneksi internet Anda. Tunggu beberapa detik, dan program akan mencoba kembali secara otomatis.
- **Error** `CTRL + C` **Tidak Berfungsi**: Jika kombinasi `CTRL + C` tidak menghentikan program, pastikan Anda menjalankan terminal di lingkungan yang mendukung penanganan sinyal interupsi.
- **Link Tidak Ditemukan**: Jika program tidak menemukan link setelah pencarian selesai, kemungkinan besar kata kunci atau query yang Anda masukkan tidak sesuai. Coba gunakan kata kunci lain yang lebih relevan atau periksa apakah query yang dimasukkan sudah benar.

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
