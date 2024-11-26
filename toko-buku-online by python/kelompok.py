# kelompok.py

# Kelas untuk mendefinisikan kode warna terminal
class WARNA:
    RESET = "\033[0m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    PURPLE = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"

# Fungsi untuk menampilkan informasi kelompok
def kelompok():
    print(WARNA.CYAN, "=================================", WARNA.RESET)
    print(WARNA.WHITE, "            KELOMPOK 5           ", WARNA.RESET)
    print(WARNA.CYAN, "=================================", WARNA.RESET)
    print(WARNA.GREEN, "Nama Anggota: \n")
    print(" 1. Wahyu           2. Tirta      ")
    print(" 3. Adam            4. Efri       ")
    print(" 5. Iyan                          \n", WARNA.RESET)
    print(WARNA.CYAN, "=================================", WARNA.RESET)

# Fungsi untuk menampilkan judul aplikasi
def judul():
    print(WARNA.CYAN, "=================================", WARNA.RESET)
    print(WARNA.WHITE, "        Toko Buku Online        ", WARNA.RESET)
    print(WARNA.CYAN, "=================================", WARNA.RESET)

# Fungsi untuk menampilkan daftar buku dan harga
def daftar_buku():
    print(WARNA.WHITE, "Kode     Jenis Buku       Harga  ", WARNA.RESET)
    print(WARNA.CYAN, "=================================", WARNA.RESET)
    print(WARNA.GREEN, "1       Buku Fisik     Rp 100.000")
    print(" 2       Buku Digital   Rp 150.000")
    print(" 3       Buku Kimia     Rp 200.000", WARNA.RESET)
    print(WARNA.CYAN, "=================================", WARNA.RESET)
