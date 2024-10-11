# TKScanner
![TKScanner](https://github.com/user-attachments/assets/86f8e257-315c-4cf3-94ad-1986cacec9ad)

**TKScanner** adalah alat Python untuk memindai dan menemukan tautan Dana Kaget di Threads. Program ini otomatis mencari tautan berdasarkan kata kunci, membuka tautan yang ditemukan, serta menyediakan opsi pengaturan jeda waktu antar tautan.

## Fitur
- **Pencarian Otomatis**: Memindai dan menemukan link Dana Kaget berdasarkan kata kunci yang dimasukkan.
- **Pengaturan Waktu**: Pengguna dapat menentukan jeda antar pencarian untuk membuka link secara otomatis.
- **Custom Query**: Mendukung berbagai kata kunci pencarian yang relevan dengan giveaway Dana Kaget.
- **Pengaturan Pencarian**: Memungkinkan pencarian di satu halaman atau seluruh halaman Threads.

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
- **Error `CTRL + C` Tidak Berfungsi**: Jika `CTRL + C` tidak menghentikan program, pastikan terminal Anda mendukung penghentian sinyal interupsi dengan benar.
- **Link Tidak Ditemukan**: Jika tidak ada link yang ditemukan, kemungkinan kata kunci tidak tepat. Coba masukkan query yang lebih relevan atau cek kembali kesalahan pengetikan.

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
