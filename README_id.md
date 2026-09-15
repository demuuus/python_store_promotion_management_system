<div align="center">

🌐 [English](README.md) | [Indonesia](README_id.md)

[![Python](https://img.shields.io/badge/python-3.14%2B-blue)]()

</div>

# Aplikasi CRUD Python untuk Sistem Manajemen Event Promosi Kasir

Aplikasi Python untuk mengelola data promosi minimarket dengan operasi Create, Read, Update, dan Delete (CRUD).

## Business Understanding

Proyek ini ditujukan untuk industri minimarket/retail, khususnya untuk mengelola data promosi secara efisien. Data promosi berperan penting dalam membantu minimarket membuat event diskon untuk menarik pelanggan.

**Benefits:**

* Meningkatkan akurasi dan konsistensi data promosi
* Mempermudah proses pengelolaan promosi
* Mempermudah pengelolaan periode dan aturan diskon
* Mendukung kasir dalam melakukan transaksi menggunakan promosi yang aktif

**Target Users:**

Aplikasi ini ditujukan untuk owner dan kasir minimarket untuk mengelola promosi serta menerapkan promosi yang tersedia saat melakukan transaksi pelanggan.

## Features

* **Create:**
    * Menambahkan data promosi baru seperti nama promosi, tipe promosi, tanggal mulai, tanggal selesai, dan diskon.
    * Menerapkan validasi untuk nama promosi, tipe promosi, tanggal, dan nilai diskon.
* **Read:**
    * Mencari dan menampilkan data promosi berdasarkan nama promosi, tipe, atau diskon.
    * Mencari dan menampilkan data produk berdasarkan ID produk, nama, atau kategori.
* **Update:**
    * Mengubah data promosi seperti nama, tipe, tanggal, dan diskon.
    * Memberikan pesan konfirmasi dan pesan error berdasarkan hasil update.
* **Delete:**
    * Menghapus data promosi yang sudah tidak diperlukan.
    * Memberikan konfirmasi sebelum menghapus data promosi.
* **Reporting:**
    * Menampilkan informasi promosi, produk, dan transaksi melalui command-line interface.

## Installation

1. **Prerequisites:**
    * Python 3.x
    * Tidak memerlukan package tambahan.

2. **Installation:**
    ```bash
    git clone https://github.com/demuuus/python_store_promotion_management_system.git
    cd python_store_promotion_management_system
    ```

3. **Database Setup:**
    Tidak memerlukan database. Aplikasi menggunakan list dan dictionary Python untuk menyimpan data di dalam memori.

## Usage

1. **Run the application:**
    ```bash
    python main.py
    ```

2. **CRUD Operations:**
    * **Create:** Menambahkan promosi baru dengan memasukkan nama, tipe promosi, periode promosi, dan diskon.
    * **Read:** Melihat dan mencari informasi promosi atau produk.
    * **Update:** Mengubah data promosi yang sudah tersedia.
    * **Delete:** Menghapus data promosi dari sistem.
    * **Transaction:** Memproses pembelian pelanggan dan menerapkan promosi aktif seperti persentase, B2G1, atau fixed discount.

## Data Model
Proyek ini menggunakan list dan dictionary Python untuk merepresentasikan data promosi dan produk. Field yang disimpan antara lain:

   * `id_promotion`: (Integer) - ID unik untuk sebuah promosi.
   * `name_promotion`: (String) - Nama promosi.
   * `type_promotion`: (String) - Tipe promosi: persentase, B2G1, atau fixed.
   * `start_date`: (Date) - Tanggal mulai promosi.
   * `end_date`: (Date) - Tanggal selesai promosi.
   * `discount`: (Integer) - Nilai diskon berdasarkan tipe promosi.
   * `id_product`: (Integer) - ID unik untuk sebuah produk.
   * `name_product`: (String) - Nama produk.
   * `price_product`: (Integer) - Harga produk.
   * `stock_product`: (Integer) - Jumlah stok produk yang tersedia.
   * `category_product`: (String) - Kategori produk.

## Contributing
Kami menerima kontribusi untuk proyek ini. Silakan membuat pull request, mengirim ke demas.anggara04@gmail.com, atau membuat issue jika menemukan masalah atau memiliki saran untuk pengembangan.
