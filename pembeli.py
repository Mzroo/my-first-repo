import time
import datetime
from data_buku import DataBuku, simpan_data_buku,clear_os
keranjang = []


# fungsi pemeli
def pembeli():
    clear_os()
    print('======================================')
    print('|            MENU PEMBELI            |')
    print('======================================')
    print('| [1] Lihat Daftar Buku              |')
    print('| [2] Tambah Buku ke Keranjang       |')
    print('| [3] Lihat Keranjang                |')
    print('| [4] Checkout                       |')
    print('| [5] Kembali ke Menu Utama          |')
    print('======================================')
    pilihan = input('Pilihan Menu: ')

    if pilihan == "1":
        lihat_buku_pembeli()
    elif pilihan == "2":
        tambah_buku_keranjang()
    elif pilihan == "3":
        lihat_keranjang()
    elif pilihan == "4":
        checkout()
    elif pilihan == "5":
        import main
        main.menu_utama()
    else:
        print('Pilihan tidak valid. Silakan coba lagi.')
        time.sleep(1)  # Memberi jeda sebelum kembali ke menu
        pembeli()
        
# Menu lihat buku di pembeli
def lihat_buku_pembeli():
    print('============================================================')
    print('|               - DAFTAR BUKU TERSEDIA -                   |')
    print('============================================================')
    print('| Kode  |      Judul Buku      |    Harga     |   Stok     |')
    print('------------------------------------------------------------')
    if not DataBuku:
        print("|          Tidak Ada Buku Tersedia                          |")
        print("=============================================================")
    else:
        for kode, buku in DataBuku.items():
            print(f"| {kode:<5} | {buku['judul']:<20} | Rp. {buku['harga']:<8,} |   {buku['qty']:<8} |\n")
    print('============================================================')
    input('Tekan [Enter] untuk kembali ...')
    pembeli()


# Menu tambah buku keranjang
def tambah_buku_keranjang():
    print('===============================================')
    print('|       - TAMBAH BUKU KE KERANJANG -          |')
    print('===============================================')
    kode_buku = input('Masukkan Kode Buku yang akan ditambahkan ke keranjang: ').upper()
    
    if kode_buku in DataBuku:
        try:
            jumlah_beli = int(input('Masukkan Jumlah Buku yang Akan Dibeli: '))
            if jumlah_beli <= DataBuku[kode_buku]['qty']:
                # Tambahkan ke keranjang
                keranjang.append({
                    'kode': kode_buku,
                    'judul': DataBuku[kode_buku]['judul'],
                    'harga': DataBuku[kode_buku]['harga'],
                    'qty_beli': jumlah_beli
                })
                print(f"\n{jumlah_beli} buku '{DataBuku[kode_buku]['judul']}' berhasil ditambahkan ke keranjang.")

            else:
                print("\nError: Stok buku tidak mencukupi.")
        except ValueError:
            print("Error: Jumlah buku harus berupa angka.")
    else:
        print('\nKode buku tidak ditemukan.')
    
    input('Tekan [Enter] untuk kembali...')
    pembeli()


# Menu lihat_keranjang
def lihat_keranjang():
    print('===============================================================')
    print('|                   KERANJANG BELANJA ANDA                    |')
    print('===============================================================')
    print('| Judul Buku          |     Harga    |  Jumlah  |   Subtotal  |')
    print('---------------------------------------------------------------')
    if not keranjang:
        print("|                    Keranjang Anda Kosong                    |")
        print("===============================================================")
    else:
        total = 0
        for buku in keranjang:
            subtotal = buku['harga'] * buku['qty_beli']
            total += subtotal
            print(f"| {buku['judul']:<19} | Rp. {buku['harga']:<8,} |   {buku['qty_beli']:<6} | Rp. {subtotal:<8,}|\n")
        print('===============================================================')
        print(f"Total Harga: Rp. {total:,}")
    input('Tekan [Enter] untuk kembali ...')
    pembeli()


# Menu checkout()
def checkout():
    print('===============================================================')
    print('|                   CHECKOUT PEMBELIAN                        |')
    print('===============================================================')
    
    if not keranjang:
        print("|            Keranjang Anda Kosong, Tidak Ada yang Dibeli. |")
        print("============================================================")
        input('Tekan [Enter] untuk kembali ke menu pembeli...')
        pembeli()  # Kembali ke menu pembeli
    else:
        total = 0
        print('| Judul Buku          |     Harga    |  Jumlah  |   Subtotal  |')
        print('---------------------------------------------------------------')
        for buku in keranjang:
            subtotal = buku['harga'] * buku['qty_beli']
            total += subtotal
            print(f"| {buku['judul']:<19} | Rp. {buku['harga']:<8,} |   {buku['qty_beli']:<6} | Rp. {subtotal:<8,}|\n")
        print("------------------------------------------------------------")
        print(f"Total Harga yang Harus Dibayar: Rp. {total:,}")
        
        # Meminta uang bayar dari pengguna
        while True:
            try:
                uang_bayar = int(input('Masukkan jumlah uang yang dibayarkan: Rp. '))
                if uang_bayar <= 0:
                    print("Error: Uang yang dibayarkan harus lebih besar dari 0.")
                elif uang_bayar < total:
                    print(f"Uang yang dibayarkan kurang. Anda masih perlu Rp. {total - uang_bayar:,}")
                else:
                    kembalian = uang_bayar - total
                    
                    # Kurangi stok buku di DataBuku
                    for buku in keranjang:
                        kode_buku = buku['kode']
                        if kode_buku in DataBuku:
                            DataBuku[kode_buku]['qty'] -= buku['qty_beli']
                            # Pastikan stok tidak negatif
                            if DataBuku[kode_buku]['qty'] < 0:
                                DataBuku[kode_buku]['qty'] = 0
                    
                    # Simpan perubahan ke file
                    simpan_data_buku()
                    clear_os()
                    # Cetak struk
                    print('\n============================================================')
                    print('|                    STRUK PEMBELIAN                       |')
                    print('============================================================')
                    print(f'| Tanggal Pembelian : { datetime.datetime.now().strftime("%d - %m - %Y | %H : %M : %S        |")}')
                    print('============================================================')
                    for buku in keranjang:
                        subtotal = buku['harga'] * buku['qty_beli']
                        print(f" {buku['judul']:<20} x {buku['qty_beli']:<3} @Rp. {buku['harga']:<8,} = Rp. {subtotal:,}")
                    print("------------------------------------------------------------")
                    print(f"Total Belanja       : Rp. {total:,}")
                    print(f"Uang Dibayarkan     : Rp. {uang_bayar:,}")
                    print(f"Kembalian           : Rp. {kembalian:,}")
                    print('============================================================')
                    print("Terima kasih telah berbelanja di toko kami!")
                    
                    keranjang.clear()  # Kosongkan keranjang setelah pembayaran
                    break
            except ValueError:
                print("Error: Masukkan angka yang valid untuk uang bayar.")
    
    input('Tekan [Enter] untuk kembali ke menu pembeli...')
    pembeli()