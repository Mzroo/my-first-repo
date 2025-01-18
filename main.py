import time
from admin import admin
from pembeli import pembeli
from data_buku import baca_data_buku, simpan_data_buku,clear_os

# Fungsi untuk menampilkan menu utama
def menu_utama():
    clear_os()
    print("======================================")
    print("|       TOKO BUKU BERBASIS TERMINAL  |")
    print("|           Jl. Teluk naga           |")
    print("======================================")
    
    print('======================================')
    print('|           Menu Utama               |')
    print('======================================')
    print('| [1] Menu Admin                     |')
    print('| [2] Menu Pembeli                   |')
    print('| [3] Exit                           |')
    print('======================================')
    pilihan = int(input("Pilihan Menu : "))
    
    if pilihan == 1:
            # Meminta input username dan password
            username = input("Username: ")
            password = input("Password: ")

            # Mengecek apakah username dan password benar
            if (username == "admin" or username == "ADMIN") and (password == "admin123" or password == "ADMIN123"):
                input("Login Sukses, Tekan [Enter] untuk ke menu admin..")
                admin()  # Jika login berhasil, panggil fungsi admin()
            else:
                print("Username atau password salah.\n")
                input("Tekan [Enter] untuk kembali ke menu utama...")
                menu_utama()
    elif pilihan == 2:
        pembeli()
    elif pilihan == 3:
        print('Terimakasih Telah mampir😊')
        exit()
    else:
        print('Pilihan tidak valid. Silahkan coba lagi.')
        time.sleep(1)
        menu_utama()

if __name__ == "__main__":
    baca_data_buku()
    menu_utama()