import os

# Dictionary untuk menyimpan data buku
DataBuku = {}

# Fungsi untuk membaca data buku
def baca_data_buku():
    global DataBuku
    try:
        with open('dataBuku.txt', 'r') as file:
            for line in file:
                kode, judul, harga, qty = line.strip().split('|')
                DataBuku[kode] = {"judul": judul, "harga": int(harga), "qty": int(qty)}
        print("Data Buku berhasil dimuat dari  file.")
    except FileNotFoundError:
        print("File dataBuku.txt tidak ditemukan. Memulai dengan data kosong.")

# Fungsi untuk menyimpan data buku
def simpan_data_buku():
    with open('dataBuku.txt', 'w') as file:
        for kode, buku in DataBuku.items():
            file.write(f"{kode}|{buku['judul']}|{buku['harga']}|{buku['qty']}\n")
        print("Data Buku berhasil disimpan ke file")

def clear_os():
    os.system("CLS")
