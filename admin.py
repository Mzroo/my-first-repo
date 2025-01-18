import time
from data_buku import DataBuku, simpan_data_buku,clear_os

# Fungsi admin
def admin():
    clear_os()
    print('======================================')
    print('|             Menu Admin             |')
    print('======================================')
    print('| [1] Lihat Daftar Buku              |')
    print('| [2] Tambah Buku Baru               |')
    print('| [3] Edit Buku                      |')
    print('| [4] Hapus Buku                     |')
    print('| [5] Kembali ke Menu Utama          |')
    print('======================================')
    pilihan = int(input('Pilihan Menu : '))
    
    if pilihan == 1:
        lihat_buku()
    elif pilihan == 2:
        tambah_buku()
    elif pilihan == 3:
        edit_buku()
    elif pilihan == 4:
        hapus_buku()
    elif pilihan == 5:
        import main
        main.menu_utama()
    else:
        print('Pilihan tidak valid. Silahkan coba lagi.')
        time.sleep(1)
        admin()

# fungsi untuk menampilkan daftar buku (admin)
def lihat_buku():
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
            print(f"| {kode:<5} | {buku['judul']:<20} | Rp. {buku['harga']:<8,} |   {buku['qty']:<8} |")
            print('------------------------------------------------------------')
    input('Tekan [Enter] untuk kembali ...')
    admin()

# fungsi untuk menambah buku baru
def tambah_buku():
    print('======================================')
    print('|          - TAMBAH BUKU BARU -      |')
    print('======================================')
    
    try:
        kode_buku = input(' Masukan Kode Buku   : ').upper()
        if kode_buku in DataBuku:
            print(f"Error: Buku dengan kode {kode_buku} Sudah Ada.")
        else:
            judul_buku = input(' Masukkan Judul Buku : ')
            harga_buku = int(input(' Masukkan Harga Buku : '))
            stok_buku  = int(input(' Masukkan Stok Buku  : '))
            DataBuku[kode_buku] = {'judul': judul_buku, 'harga': harga_buku, 'qty': stok_buku}
            print('======================================')
            print(f"Buku '{judul_buku}' Berhasil ditambahkan.")
            simpan_data_buku()
            
    except ValueError:
        print("Error: Harga dan stok buku harus berupa angka. Silahkan Coba Lagi.")
    input('Tekan [Enter] untuk kembali ...')
    admin()
    
# fungsi untuk mengedit buku
def edit_buku():
    print('======================================')
    print('|         - EDIT DATA BUKU -         |')
    print('======================================')

    kode_buku = input('Masukkan Kode Buku yang akan diedit: ').upper()
    if kode_buku in DataBuku:
        print(f"Judul Saat Ini: {DataBuku[kode_buku]['judul']}")
        print(f"Harga Saat Ini: Rp. {DataBuku[kode_buku]['harga']}")
        print(f"Stok  Saat Ini: {DataBuku[kode_buku]['qty']}")
        judul_baru = input('Masukkan Judul Baru (tekan Enter jika tidak ingin mengubah): ')
        harga_baru = input('Masukkan Harga Baru (tekan Enter jika tidak ingin mengubah): ')
        stok_baru =  input('Masukkan Stok Baru (tekan Enter jika tidak ingin mengubah): ')
        
        if judul_baru.strip():
            DataBuku[kode_buku]['judul'] = judul_baru
        
        # update harga jika diisi
        if harga_baru.strip():
            try:
                DataBuku[kode_buku]['harga'] = int(harga_baru)
            except ValueError:
                print("Error: Harga baru harus berupa angka.")
        
        # update stok jika diisi
        if stok_baru.strip():
            try:
                DataBuku[kode_buku]['qty'] = int(stok_baru)
            except:
                print("Error: stok baru harus berupa angka.")
        print(f"Buku dengan kode {kode_buku} berhasil diperbarui.")
        simpan_data_buku()
    else:
        print(f"Error: Buku dengan kode {kode_buku} tidak ditemukan.")
        
    input('Tekan [Enter] untuk Kembali...')
    admin()
    
    
# fungsi untuk hapus buku
def hapus_buku():
    print('======================================')
    print('|         - HAPUS DATA BUKU -        |')
    print('======================================')
    
    kode_buku = input('Masukkan kode Buku yang akan dihapus : ').upper()
    if kode_buku in DataBuku:
        konfirmasi = input(f"Apakah Anda yakin menghapus buku '{DataBuku[kode_buku]['judul']}'? (y/n): ").lower()
        if konfirmasi == 'y':
            del DataBuku[kode_buku]
            print(f"Buku dengan kode {kode_buku} berhasil dihapus.")
            simpan_data_buku()
        else:
            print("Penghapusan dibatalkan.")
    else:
        print(f"Error: Buku dengan kode {kode_buku} tidak ditemukan.")
    input('Tekan [Enter] untuk kembali...')
    admin()