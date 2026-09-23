# ===================================
# Cashier Promotion Event Management System
# ===================================
# Developed by. Demas Fadel Anggara
# JCDS - 34

# /************************************/
# Tujuan:
# Untuk membantu owner/kasir membuat event diskon bulanan/mingguan/barang pada minimarket untuk menarik pelanggan

# /===== Data Model =====/
# Create your data model here
from datetime import datetime, date

# Example data model
products = [
    {
        "id_product": 1,
        "name_product": "Air Mineral",
        "price_product": 6500,
        "stock_product": 15,
        "category_product": "minuman"
    },
    {
        "id_product": 2,
        "name_product": "Mie Instan",
        "price_product": 3500,
        "stock_product": 20,
        "category_product": "makanan"
    },
    {
        "id_product": 3,
        "name_product": "Roti Tawar",
        "price_product": 5500,
        "stock_product": 10,
        "category_product": "makanan"
    },
    {
        "id_product": 4,
        "name_product": "Sabun Mandi",
        "price_product": 18000,
        "stock_product": 5,
        "category_product": "kosmetik"
    },
    {
        "id_product": 5,
        "name_product": "Susu Murni",
        "price_product": 2500,
        "stock_product": 25,
        "category_product": "minuman"
    },
]

promotions = [
    {
        "id_promotion": 1,
        "name_promotion": "Promosi Bulanan",
        "type_promotion": "persentase",
        "start_date": datetime.strptime("01-09-2026", "%d-%m-%Y").date(),
        "end_date": datetime.strptime("30-09-2026", "%d-%m-%Y").date(),
        "discount": 10
    },
    {
        "id_promotion": 2,
        "name_promotion": "Promosi Mingguan",
        "type_promotion": "b2g1",
        "start_date": datetime.strptime("1-09-2026", "%d-%m-%Y").date(),
        "end_date": datetime.strptime("28-09-2026", "%d-%m-%Y").date(),
        "discount": 1    
    },
    {
        "id_promotion": 3,
        "name_promotion": "Promosi Barang",
        "type_promotion": "fixed",
        "start_date": datetime.strptime("01-09-2026", "%d-%m-%Y").date(),
        "end_date": datetime.strptime("30-09-2026", "%d-%m-%Y").date(),
        "discount": 1000
    }
]

# /===== CREATE Program =====/
def create_promotion():                                                                          # CREATE
    """Create a promotion"""
    while True:
        print("Membuat promosi baru\n\n" + "=" * 50)
        print("\nApa yang ingin anda lakukan?\n"
                "[1] Lanjutkan\n"
                "[2] Back\n")

        pilihan_awal = input("Masukkan angka: ").strip()
        if pilihan_awal == "1":
            break

        elif pilihan_awal == "2":
            return

        else:
            print("[X] Input tidak valid! Masukkan angka 1 atau 2.")

    nama_promosi = name_promotion()
    tipe_promosi, tipe_promosi_angka = type_promotion()
    mulai_tanggal = start_date()
    selesai_tanggal = end_date(mulai_tanggal)
    diskon = discount(tipe_promosi_angka)

    new_promotion = {
        "id_promotion": len(promotions) + 1,
        "name_promotion": nama_promosi,
        "type_promotion": tipe_promosi,
        "start_date": mulai_tanggal,
        "end_date": selesai_tanggal,
        "discount": diskon
    }

    while True:
        print("\n" + "=" * 50)
        print("\nData promosi baru:")

        for key, value in new_promotion.items():
            print(f"{key}: {value}")

        print("\nApa yang ingin anda lakukan?\n"
            "[1] Edit\n"
            "[2] Save\n"
            "[3] Cancel\n")
        pilihan = input("Masukkan angka: ").strip()
        
        if pilihan == "1":
            print("\nApa yang ingin anda edit?\n"
                "[1] Nama promosi\n"
                "[2] Tipe promosi\n"
                "[3] Tanggal mulai\n"
                "[4] Tanggal akhir\n"
                "[5] Diskon\n")
            edit_input = input("Masukkan angka: ").strip()
            
            if edit_input == "1":
                new_promotion["name_promotion"] = name_promotion()

            elif edit_input == "2":
                tipe_promosi, tipe_promosi_angka = type_promotion()
                new_promotion["type_promotion"] = tipe_promosi
                if tipe_promosi == "b2g1":
                    new_promotion["discount"] = 1
                else:
                    new_promotion["discount"] = discount(tipe_promosi_angka)

            elif edit_input == "3":
                new_promotion["start_date"] = start_date()
                if new_promotion["end_date"] < new_promotion["start_date"]:
                    print("[!] Tanggal akhir sebelumnya tidak valid "
                        "karena tanggal mulai berubah.")
                    new_promotion["end_date"] = end_date(new_promotion["start_date"])

            elif edit_input == "4":
                new_promotion["end_date"] = end_date(new_promotion["start_date"])

            elif edit_input == "5":
                tipe_promosi_angka = {"persentase": 1, "b2g1": 2,"fixed": 3}[new_promotion["type_promotion"]]
                new_promotion["discount"] = discount(tipe_promosi_angka)

            else:
                print("[X] Input tidak valid! Masukkan angka 1-5.")

        elif pilihan == "2":
            print(f"\nApakah anda yakin ingin menyimpan "
                f"promosi '{new_promotion['name_promotion']}'?")

            if konfirmasi():
                promotions.append(new_promotion)
                print(f"\n[+] Sukses menambahkan promosi {new_promotion['name_promotion']}\n")
                for key, value in new_promotion.items():
                    print(f"{key}: {value}")
                return
            else:
                print("\n[!] Promosi belum disimpan.")
                
        elif pilihan == "3":
            print(f"\n[X] Pembuatan promosi "
                f"'{new_promotion['name_promotion']}' dibatalkan.")
            return
        else:
            print("[X] Input tidak valid! Masukkan angka 1-3.")

def name_promotion():
    while True:
        name_input = input("\nNama promosi yang ingin di buat: ").strip().title()
        if not name_input:
            print("[!] Input tidak valid! Nama promosi tidak boleh kosong!")
            continue
        
        check_name = name_input.replace(" ", "").replace(".", "").replace("/", "").replace(",", "")
        if not check_name.isalnum():
            print("[X] Input tidak valid! Hanya boleh berisi huruf, angka, spasi, titik, garis miring, dan koma!")
            continue
        return name_input

def type_promotion():
    while True:
        try:      
            type_input = int(input("\nMasukan tipe promosi:\n"
                                    "[1] Persentase\n"
                                    "[2] Buy 2 Get 1\n"
                                    "[3] Fixed\n"
                                    "Masukkan angka: "))
            result = type_valid(type_input)
            if result:
                return result
        except ValueError:
            print("[X] Input tidak valid! Masukkan angka!")

def type_valid(type_input):
    if type_input not in (1, 2, 3):
        print("[X] Input tidak valid! Tipe promosi harus antara 1 (Persentase), 2 (B2G1), atau 3 (fixed)!")
        return None
    elif type_input == 1:
        type_value = "persentase"
    elif type_input == 2:
        type_value = "b2g1"
    else:
        type_value = "fixed"
    return type_value, type_input

def start_date():
    while True:
        start_input = input("\nMasukkan tanggal mulai promosi (DD-MM-YYYY): ").strip()
        try:
            start_promotion = datetime.strptime(start_input, "%d-%m-%Y").date()
            break
        except ValueError:
            print("Eror: Format tanggal salah atau kosong! Gunakan DD-MM-YYYY (Contoh: 09-11-2026).")
    return start_promotion

def end_date(start_promotion):
    while True:
        end_input = input("\nMasukkan tanggal akhir promosi (DD-MM-YYYY): ").strip()
        try:
            end_promotion = datetime.strptime(end_input, "%d-%m-%Y").date()
            if end_promotion < start_promotion:
                print("Eror: Tanggal akhir promosi tidak boleh lebih dulu dari tanggal mulai!")
                continue
            return end_promotion
        except ValueError:
            print("Eror: Format tanggal salah atau kosong! Gunakan DD-MM-YYYY (Contoh: 09-11-2026).")

def discount(type_value):
    while True:
        try:
            if type_value == 1:
                amount_input = int(input("\nMasukkan persentase diskon (1-20): "))
                if not (1 <= amount_input <= 20):
                    print("[X] Persentase diskon harus di antara 1 sampai 20!")
                    continue
            elif type_value == 3:
                amount_input = int(input("\nMasukkan berapa banyak potongan (Rupiah): "))
                if amount_input <= 0:
                    print("[X] Potongan harga harus lebih besar dari 0!")
                    continue
            else:
                amount_input = 1
            return amount_input
        except ValueError:
            print("[X] Input tidak valid! Harap masukkan angka bulat!")

# /===== READ Program =====/
def get_product():                                                                          # READ
    """View + Search promotions"""
    while True:
        try:
            get_input = int(input("Apa yang ingin anda lihat?\n"
                                "[1] Promosi\n"
                                "[2] Produk\n"
                                "[3] Back\n"
                                "Masukkan angka: "))
            
            if get_input not in (1, 2, 3):
                print("[X] Input tidak valid! Masukkan angka 1 atau 2!")
                continue
            if get_input == 3:
                return
            break
        except ValueError:
            print("[X] Input tidak valid! Masukkan angka!")
        
    while True:
        try:
            action_input = int(input("\nApa yang ingin anda lakukan?\n"
                                    "[1] Lihat\n"
                                    "[2] Cari\n"
                                    "Masukkan angka: "))
            if action_input not in (1, 2):
                print("[X] Input tidak valid! Masukkan angka 1 atau 2!")
                continue
            break
        except ValueError:
            print("[X] Input tidak valid! Masukkan angka!")
        
    print("\n" + "=" * 50)
    
    if get_input == 1:
        if action_input == 1:
            print("\nList promosi saat ini: ")
            view_promotion()
        else:
            print("\nSearch promosi: ")
            search_promotion()
            
    elif get_input == 2:
        if action_input == 1:
            print("\nList promosi saat ini: ")
            view_product()
        else:
            print("\nSearch promosi: ")
            search_product()
    return

def view_promotion():
    print("")
    for i in promotions:
        for key, value in i.items():
            print(f"{key}: {value}", end = "\n")
        print()
    return

def search_promotion():
    search_input = input("Masukkan keyword yang ada di promosi: ").strip().casefold()
    if not search_input:
        print("[!] Keyword pencarian tidak boleh kosong!")
        return
    
    found = False
    for i in promotions:
        id_str = str(i["id_promotion"]).lower()
        nama_str = str(i["name_promotion"]).lower()
        tipe_str = str(i["type_promotion"]).lower()
        disc_str = str(i["discount"]).lower()
        if search_input in nama_str or search_input in tipe_str or search_input in disc_str:
            print(f"\n[+] Data Ditemukan:")
            for key, val in i.items():
                print(f"{key}: {val}", end = "\n")
            print()
            found = True
    if not found:
        print(f"[X] Keyword '{search_input}' tidak ditemukan di dalam daftar promosi.")
    return

def view_product():
    print()

    for i in products:
        print(f"ID Produk: {i['id_product']}\n"
            f"Nama Produk: {i['name_product']}\n"
            f"Stok: {i['stock_product']}\n"
            f"Harga: Rp{i['price_product']:,.0f}\n"
            f"Kategori: {i['category_product']}\n")
    return

def search_product():
    search_input = input("Masukkan keyword yang ada di produk: ").strip().casefold()
    if not search_input:
        print("[!] Keyword pencarian tidak boleh kosong!")
        return

    found = False
    for i in products:
        id_str = str(i["id_product"])
        nama_str = i["name_product"].casefold()
        kategori_str = i["category_product"].casefold()
        
        if (search_input in id_str or search_input in nama_str or search_input in kategori_str):
            print("\n[+] Data Ditemukan:")
            for key, value in i.items():
                print(f"{key}: {value}")
            print()
            found = True

    if not found:
        print(f"[X] Keyword '{search_input}' "
            "tidak ditemukan di dalam daftar produk.")
    return

# /===== UPDATE Program =====/
def update_promotion():                                                                     # UPDATE
    """Function for update the sale"""
    for i in promotions:
            for key, value in i.items():
                print(f"{key}: {value}", end = "\n")
            print()
        
    while True:
        print("Apa yang ingin anda lakukan?\n"
              "[1] Lanjutkan\n"
              "[2] Back\n")

        pilihan_awal = input("Masukkan angka: ").strip()

        if pilihan_awal == "1":
            break

        elif pilihan_awal == "2":
            return

        else:
            print("[X] Input tidak valid! Masukkan angka 1 atau 2.")
            
    update_input = input("\nMasukkan ID Promosi yang ingin diubah: ").strip()
    print("\n" + "=" * 50 + "\n")
    
    found = False
    for i in promotions:
        if str(i["id_promotion"]) == update_input:
            found = True
            print(f"[+] Data ditemukan: {i['name_promotion']}\nSilakan masukkan data baru:\n")
            
            tipe_baru_angka = {"persentase": 1,
                                "b2g1": 2,
                                "fixed": 3} [i["type_promotion"]]
            
            if isinstance(i["start_date"], str):
                start_lama = datetime.strptime(i["start_date"], "%d-%m-%Y").date()
            else:
                start_lama = i["start_date"]
            
            while True:
                try:
                    print("Apakah anda ingin mengubah nama promosi?")
                    if konfirmasi():
                        print()
                        nama_baru = name_promotion()
                        i["name_promotion"] = nama_baru
                        print()
                    print()
                    break
                except ValueError:
                    print("[X] Input tidak valid!")
            
            while True:
                try:
                    print("Apakah anda ingin mengubah tipe promosi?")
                    if konfirmasi():
                        tipe_baru, tipe_baru_angka = type_promotion()
                        i["type_promotion"] = tipe_baru
                        print()
                    print()
                    break
                except ValueError:
                    print("[X] Input tidak valid!")
                    
            ubah_tanggal_akhir = False

            while True:
                try:
                    print("Apakah anda ingin mengubah tanggal mulai?")
                    if konfirmasi():
                        start_baru = start_date()
                        i["start_date"] = start_baru
                        print()

                        if i["end_date"] < i["start_date"]:
                            print("[!] Tanggal akhir sebelumnya tidak valid "
                                "karena tanggal mulai berubah.")
                            i["end_date"] = end_date(i["start_date"])
                            ubah_tanggal_akhir = True

                    print()
                    break
                except ValueError:
                    print("[X] Input tidak valid!")

            if not ubah_tanggal_akhir:
                while True:
                    try:
                        print("Apakah anda ingin mengubah tanggal akhir?")
                        if konfirmasi():
                            end_baru = end_date(i["start_date"])
                            i["end_date"] = end_baru
                            print()
                        print()
                        break
                    except ValueError:
                        print("[X] Input tidak valid!")
            
            if i["type_promotion"] == "b2g1":
                i["discount"] = 1
            else:
                while True:
                    try:
                        print("Apakah anda ingin mengubah diskon?")
                        if konfirmasi():
                            diskon_baru = discount(tipe_baru_angka)
                            i["discount"] = diskon_baru
                        break
                    except ValueError:
                        print("[X] Input tidak valid!")
            
            print("\n" + "=" * 50)
            print("\n[+] Promosi berhasil diperbarui")
            for key, val in i.items():
                print(f"{key}: {val}")
            return
        
    if not found:
        print(f"[X] ID Promosi '{update_input}' tidak ditemukan!")
    return

# /===== DELETE Program =====/
def delete():                                                                               # DELETE
    """Function for delete the sale"""
    for i in promotions:
            for key, value in i.items():
                print(f"{key}: {value}", end = "\n")
            print()

    while True:
            print("\nApa yang ingin anda lakukan?\n"
                "[1] Lanjutkan\n"
                "[2] Delete All\n"
                "[3] Back\n")

            pilihan_awal = input("Masukkan angka: ").strip()

            if pilihan_awal == "1":
                break

            elif pilihan_awal == "2":
                if not promotions:
                    print("\n[!] Tidak ada promosi yang dapat dihapus.")
                    return False

                print(f"\n[!] Apakah anda yakin ingin menghapus "
                    f"semua {len(promotions)} promosi?")

                if konfirmasi():
                    promotions.clear()
                    print("\n[+] Semua promosi berhasil dihapus.")
                    return True
                else:
                    print("\n[!] Penghapusan dibatalkan.")
                    return False

            elif pilihan_awal == "3":
                return False

            else:
                print("[X] Input tidak valid! Masukkan angka 1, 2, atau 3.")

    try:
        delete_input = int(input("Masukkan ID yang ingin di hapus: "))
    except ValueError:
        print("[X] Input tidak valid! Masukkan angka!")
        return False

    for i in promotions:
        if delete_input == i["id_promotion"]:
            print("\n[!] Apakah anda yakin untuk menghapus promosi tersebut?")
            if konfirmasi():
                promotions.remove(i)
                print(f"[+] Promosi ID: {i['id_promotion']} berhasil dihapus!")
                return True
            else:
                print("[!] Penghapusan dibatalkan.")
                return False

    print(f"[X] Promosi dengan ID {delete_input} tidak ada, Masukkan kembali Promosi ID antara 1-{len(promotions)}")
    return False

def konfirmasi():
    while True:
        try:
            pilihan = int(input("[1] Iya\n"
                                "[2] Tidak\n"
                                "Masukkan angka: "))
            if pilihan == 1:
                return True
            elif pilihan == 2:
                return False
            else:
                print("[X] Input tidak valid! Masukkan 1 atau 2\n")
        except ValueError:
            print("[X] Input tidak valid! Masukkan angka!")

# /===== TRANSACTION Program =====/
def transaksi():
    """Customer purchase"""
    while True:
        print("Apa yang ingin anda lakukan?\n"
              "[1] Lanjutkan\n"
              "[2] Back\n")

        pilihan_awal = input("Masukkan angka: ").strip()

        if pilihan_awal == "1":
            break

        elif pilihan_awal == "2":
            return

        else:
            print("[X] Input tidak valid! Masukkan angka 1 atau 2.")
            
    print("Berikut barang yang tersedia\n")
    for i in products:
        print(f"ID: {i['id_product']} | "
            f"Nama: {i['name_product']} | "
            f"Stok: {i['stock_product']} | "
            f"Harga (Rp): {i['price_product']:,.0f} ")
    found = False
    while True:
        try:
            user_input = int(input("\nMasukkan ID produk: "))
            for i in products:
                if user_input == i["id_product"]:
                    found = True
                    jumlah_input = int(input("\nBerapa banyak yang dibeli: "))
                    
                    if jumlah_input > i["stock_product"]:
                        print(f"Jumlah barang tersisa hanya {i['stock_product']}")
                    elif jumlah_input <= 0:
                        print("[!] Input tidak valid! Masukkan angka positif")
                    else:
                        harga, promo_berhasil, barang_keluar = diskon(i, jumlah_input)
                        if promo_berhasil:
                            i["stock_product"] -= barang_keluar
                            print("\n[+] Transaksi berhasil!"
                                f"\nTotal bayar: Rp{harga:,.0f}"
                                f"\nSisa stok {i['name_product']}: "
                                f"{i['stock_product']}")
                        else:
                            print("[X] Transaksi gagal!")
                    return
                
            if not found:
                print(f"\n[!] ID produk tidak ditemukan, masukkan ID produk antara angka 1-{len(products)}")
        except ValueError:
            print("[X] Input tidak valid!")

def diskon(product, jumlah_input):
    harga_awal = product["price_product"] * jumlah_input
    harga = harga_awal
    barang_diterima = jumlah_input
    promo_berhasil = False
    today = date.today()
    
    print("\nApakah anda memiliki voucher?")
    if not konfirmasi():
        print(f"\nHarga yang harus dibayar: Rp{harga_awal:,.0f}")
        return harga_awal, False, barang_diterima
    
    diskon_input = input("Masukkan kode voucher yang anda miliki saat ini: ").title()
    promotion = None
    for i in promotions:
        if i["name_promotion"] == diskon_input:
            promotion = i
            break
    
    if promotion is None:
        print("[!] Voucher tidak ditemukan!")
        return harga_awal, False, barang_diterima
    
    if not (promotion["start_date"] <= today <= promotion["end_date"]):
        print("[!] Voucher sudah tidak aktif!")
        return harga_awal, False, barang_diterima
        
    tipe = promotion["type_promotion"]
    
    if tipe == "b2g1":
        if jumlah_input % 2 != 0 or jumlah_input > 6:
            print("\n[!] Promosi B2G1 tidak sesuai kriteria."
                "\nSyarat: jumlah pembelian harus genap dan maksimal 6.")
            return harga_awal, False, barang_diterima

    elif tipe == "persentase":
        if jumlah_input < 5:
            print("\n[!] Promosi persentase tidak sesuai kriteria."
                "\nSyarat: minimal pembelian 5 barang.")
            return harga_awal, False, barang_diterima

    elif tipe == "fixed":
        if jumlah_input > 4:
            print("\n[!] Promosi fixed tidak sesuai kriteria."
                "\nSyarat: maksimal pembelian 4 barang.")
            return harga_awal, False, barang_diterima

    print(f"\nVoucher '{promotion['name_promotion']}' ditemukan dan aktif.\n")
    print("Apakah anda yakin ingin menggunakan promo ini?")

    if not konfirmasi():
        print(f"\nPromo tidak digunakan.")
        print(f"Harga yang harus dibayar: Rp{harga_awal:,.0f}")
        return harga_awal, False, barang_diterima

    harga = harga_awal

    if tipe == "b2g1":
        promo_berhasil = True
        barang_diterima, barang_gratis = diskon_b2g1(jumlah_input)
        potongan = product["price_product"] * barang_gratis
        harga = harga_awal - potongan

        print("\nPromosi B2G1 Aktif!"
            f"\nBarang gratis: {barang_gratis}"
            f"\nBarang diterima: {barang_diterima}"
            f"\nPotongan harga: Rp{potongan:,.0f}\n")

    elif tipe == "persentase":
        promo_berhasil = True
        harga = diskon_persentase(product, promotion, jumlah_input)
        potongan = harga_awal - harga
        print(f"\nPotongan harga {promotion['discount']}%: Rp{potongan:,.0f}")

    elif tipe == "fixed":
        harga = diskon_fixed(harga, promotion, jumlah_input)
        
        if harga is None:
            promo_berhasil = False
            print(f"\n[!] Promosi {promotion['name_promotion']} tidak dapat digunakan.\n"
                "Syarat: harga setelah diskon tidak boleh kurang dari Rp 0\n"
                f"Harga yang harus dibayar: Rp{harga_awal}")
            return harga_awal, False, barang_diterima
        else:
            promo_berhasil = True
            potongan = harga_awal - harga
            print(f"\nPotongan harga: Rp{potongan:,.0f}")

    print(f"Harga sebelum diskon: Rp{harga_awal:,.0f}")
    print(f"Harga setelah diskon: Rp{harga:,.0f}")
    return harga, promo_berhasil, barang_diterima

def diskon_persentase(product, i, jumlah_input):
    jumlah = (product["price_product"] * jumlah_input)
    diskon = jumlah * i["discount"] / 100
    harga = jumlah - diskon
    return harga

def diskon_b2g1(jumlah_input):
    barang_gratis = 0
    barang_diterima = jumlah_input
    if jumlah_input % 2 == 0:
        barang_gratis = jumlah_input // 2
        barang_diterima += barang_gratis
    return barang_diterima, barang_gratis

def diskon_fixed(harga, i, jumlah_input):
    fixed_diskon = i["discount"] * jumlah_input
    harga_setelah_diskon = harga - fixed_diskon
    
    if harga_setelah_diskon < 0:
        return None
    
    return harga_setelah_diskon

# /===== Main Program =====/
def main():
    """Function for main program"""
    while True:
        print("\n" + "=" * 4 + " Cashier Promotion Event Managemet System " + "=" * 4)
        print("\n[1] Membuat Promosi Baru\n"
                "[2] Lihat Promosi atau Produk yang tersedia\n"
                "[3] Perbarui Promosi\n"
                "[4] Hapus Promosi\n"
                "[5] Transaksi\n"
                "[6] Keluar\n")    
        print("=" * 50 + "\n")

        input_user = input("Masukkan angka: ")
        print("\n" + "=" * 50 + "\n")

        if input_user == "1":
            create_promotion()
        elif input_user == "2":
            get_product()
        elif input_user == "3":
            update_promotion()
        elif input_user == "4":
            delete()
        elif input_user == "5":
            transaksi()
        elif input_user == "6":
            break
        else:
            print("[X] Input tidak valid! Masukkan angka antara 1-6")

if __name__ == "__main__":
    main()