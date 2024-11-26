# main.py
import os
import datetime
from kelompok import kelompok, judul, daftar_buku
from transaksi import tampilkan_rincian

# Fungsi utama untuk login admin dan navigasi aplikasi
def menu_utama():
    os.system("CLS")  # Membersihkan layar (berfungsi di Windows)
    kelompok()  # Menampilkan informasi kelompok
    
    # Meminta input login
    admin = input(" Input (admin) untuk masuk: ")
    if admin.lower() == "admin":
        # Jika login berhasil
        judul()  # Menampilkan judul aplikasi
        daftar_buku()  # Menampilkan daftar buku
        keranjang1, keranjang2, keranjang3, total_bayar, uang_total, kembalian = tampilkan_rincian()  # Melanjutkan ke pembelian
        # kondisi mau cetak struk atau tidak
        cetak = input("\n apakah kamu yang ingin mencetak sturk (y/n): ")
        if cetak.lower() == "y":
            print("struk pembelian")
            cetak_struk(keranjang1, keranjang2, keranjang3, total_bayar, uang_total, kembalian)  # Mencetak struk
        else: 
            exit()
    else:
        # Jika login gagal
        print(" Maaf, Anda tidak memiliki akses untuk masuk ke dalam sistem.")
        input(" Tekan Enter untuk kembali ke menu utama...")
        menu_utama()  # Kembali ke menu utama

# Fungsi untuk mencetak struk pembelian
def cetak_struk(keranjang1, keranjang2, keranjang3, total_bayar, uang_total, kembalian):
    os.system("clear")  # Bersihkan layar (untuk Linux/Mac)
    
    # Mendapatkan waktu transaksi
    waktu_transaksi = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    print("\n=============================================")
    print("               TOKO BUKU ONLINE              ")
    print("=============================================")
    print(f"Waktu Transaksi: {waktu_transaksi}")  # Menampilkan waktu transaksi
    print("=============================================")
    print("No\tJenis Buku\tHarga\t\tJumlah\tSubtotal")
    print("=============================================")
    
    # Menampilkan detail pembelian pada struk
    for i in range(len(keranjang1)):
        subtotal = keranjang2[i] * keranjang3[i]
        print(f"{i + 1}\t{keranjang1[i]:<15}\tRp.{keranjang2[i]:<8,}\t{keranjang3[i]:<5}\tRp.{subtotal:<10,}")
    
    # Menampilkan total bayar, uang dibayar, dan kembalian
    print("=============================================")
    print(f"Total Bayar\t\t\tRp.{total_bayar:,}")
    print(f"Uang Dibayar\t\t\tRp.{uang_total:,}")
    print(f"Kembalian\t\t\tRp.{kembalian:,}")
    print("=============================================")
    print("    Terima kasih telah berbelanja dengan kami!    ")
    print("=============================================\n")
    
    # Menawarkan untuk melanjutkan pembelian atau keluar
    lanjut = input("Apakah kamu ingin melanjutkan pembelian? (y/n): ")
    if lanjut.lower() == "y":
        menu_utama()  # Mengulangi menu utama untuk pembelian lagi
    else:
        exit()  # Keluar dari program

if __name__ == "__main__":
    menu_utama()  # Memulai aplikasi

