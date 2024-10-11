# TKScanner
![TKScanner](https://github.com/user-attachments/assets/77a15160-481f-43aa-ab23-684db5539ad0)

**TKScanner** adalah alat Python untuk memindai dan menemukan tautan Dana Kaget di Threads. Program ini otomatis mencari tautan berdasarkan kata kunci, membuka tautan yang ditemukan, serta menyediakan opsi pengaturan jeda waktu antar tautan.

## Fitur
- **Pengaturan Waktu**: Pengguna dapat menentukan jeda antar pencarian untuk membuka link secara otomatis.
- **Pencarian Otomatis**: Memindai dan menemukan link Dana Kaget berdasarkan kata kunci yang dimasukkan.
- **Pengaturan Pencarian**: Memungkinkan pencarian di satu halaman atau seluruh halaman Threads.
- **Custom Query**: Mendukung berbagai kata kunci pencarian yang relevan dengan giveaway Dana Kaget.

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
- **Link Tidak Ditemukan**: Jika tidak ada link yang ditemukan, kemungkinan kata kunci tidak tepat. Coba masukkan query yang lebih relevan atau cek kembali kesalahan pengetikan.
- **Error `CTRL + C` Tidak Berfungsi**: Jika `CTRL + C` tidak menghentikan program, pastikan terminal Anda mendukung penghentian sinyal interupsi dengan benar.
- **Masalah RequestException**: Jika Anda mengalami kesalahan `RequestException`, periksa koneksi internet Anda. Tunggu beberapa detik, dan program akan mencoba kembali secara otomatis.

## Dukungan
Bantu kami mengembangkan TKScanner menjadi lebih baik! Anda bisa mendukung kami dengan cara berikut:

- **Dukung Pengembangan**: Setiap dukungan Anda sangat berarti! Bisa sekecil satu cangkir kopi untuk mendukung pengembangan alat yang memudahkan pencarian Dana Kaget di Threads.
    - ☕ [Trakteer](https://trakteer.id/rozhak_official/tip) | 💸 [PayPal](https://paypal.me/rozhak9) | 💰 [Saweria](https://saweria.co/rozhak9)
- **Bergabunglah dalam Diskusi**: Bagikan ide, saran, atau bug yang Anda temui di halaman Issues GitHub kami! Komunitas berkembang dari kontribusi Anda.
    - 💬 [Diskusi GitHub](https://github.com/RozhakXD/TKScanner/issues)
- **Bagikan ke Teman**: Sebarkan kata tentang TKScanner ke teman atau komunitas Anda. Setiap penyebaran membantu kami tumbuh!

Terima kasih sudah mendukung kami! 🙏

## Demo Fitur Utama
![Video]()

## Kontribusi
Jika Anda ingin berkontribusi pada proyek ini, silakan fork repositori ini dan kirim pull request. Anda juga dapat melaporkan masalah atau permintaan fitur melalui tab Issues.

## Lisensi
Proyek ini dilisensikan di bawah MIT License - lihat file [LICENSE](https://github.com/RozhakXD/TKScanner/blob/main/LICENSE) untuk detail lebih lanjut.
