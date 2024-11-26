# transaksi.py
import datetime
import os
from kelompok import WARNA

# Fungsi untuk menangani rincian pembelian
def tampilkan_rincian():
    keranjang1 = []  # Menyimpan jenis buku
    keranjang2 = []  # Menyimpan harga buku
    keranjang3 = []  # Menyimpan jumlah buku

    # Meminta jumlah jenis buku yang akan dibeli
    banyak_jenis = int(input("\n Banyak jenis buku yang dibeli: "))
    
    # Loop untuk meminta informasi buku yang akan dibeli
    for i in range(banyak_jenis):
        print(f"\n Jenis Buku ke- {i + 1}")
        while True:
            # Meminta kode buku untuk memilih jenis buku
            kode_buku = int(input(" Kode Buku: "))
            if kode_buku == 1:
                jenis = "Buku Fisik"
                harga = 100000
                break
            elif kode_buku == 2:
                jenis = "Buku Digital"
                harga = 150000
                break
            elif kode_buku == 3:
                jenis = "Buku Kimia"
                harga = 200000
                break
            else:
                # Jika kode salah, tampilkan pesan error
                print(WARNA.RED, "Kode Buku Tidak Tersedia.", WARNA.RESET)
        
        # Meminta jumlah buku yang dibeli
        banyak_buku = int(input(" Banyak Buku yang Dibeli: "))
        keranjang1.append(jenis)
        keranjang2.append(harga)
        keranjang3.append(banyak_buku)
        print(WARNA.CYAN, "=================================", WARNA.RESET)

    # Menampilkan rincian pembelian
    print(WARNA.CYAN, "\n ======================= Rincian Pembelian ==========================", WARNA.RESET)
    print(WARNA.WHITE, "No\tJenis Buku\tHarga\t\tJumlah\t\tSubtotal", WARNA.RESET)
    print(WARNA.CYAN, "====================================================================", WARNA.RESET)
    total_bayar = 0  # Menghitung total harga semua buku
    for i in range(len(keranjang1)):
        subtotal = keranjang2[i] * keranjang3[i]
        total_bayar += subtotal
        print(WARNA.GREEN, f" {i + 1}\t{keranjang1[i]:<15}\tRp.{keranjang2[i]:<8,}\t{keranjang3[i]:<5}\t\tRp.{subtotal:<10,}", WARNA.RESET)
    print(WARNA.CYAN, "====================================================================", WARNA.RESET)
    print(WARNA.WHITE, f"Total Bayar: Rp {total_bayar:,}\n", WARNA.RESET)
    
    # Proses pembayaran
    uang_total = 0
    while uang_total < total_bayar:
        # Meminta jumlah uang yang dibayarkan
        uang_cash = int(input(f" Masukkan Uang Cash (kurang Rp. {total_bayar - uang_total:,}): Rp. "))
        uang_total += uang_cash
        
        if uang_total < total_bayar:
            # Jika uang kurang, tampilkan pesan kekurangan
            kekurangan = total_bayar - uang_total
            print(f" Uang Anda masih kurang Rp.{kekurangan:,}. ")
            print(" Harap masukkan uang tambahan untuk melanjutkan pembayaran.\n")
    
    # Menghitung kembalian
    kembalian = uang_total - total_bayar
        
    # Mencetak struk pembelian
    return keranjang1, keranjang2, keranjang3, total_bayar, uang_total, kembalian
