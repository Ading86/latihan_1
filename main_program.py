import os  
import pandas as pd

# Fungsi untuk membersihkan layar terminal sebelumnya dengan modul 'os'
def membersihkan_layar():
    os.system('cls')

# Fungsi Untuk melanjutkan dengan Klik 'Enter'
def tunggu_enter():
    input("\nTekan Enter untuk melanjutkan...")


akun = {}
# Fungsi Untuk Membuat Akun sebelum masuk ke Aplikasi Perpustakaan
def buat_akun():
    membersihkan_layar()
    print("==========   Menu 'Buat Akun'   ==========\n")
    username = input("Masukkan Username Akun yang ingin dibuat : ")
    if username in akun:
        print("\nUsername Sudah Terdaftar")
    else:
        while True:
            password = input("Masukkan Password Akun yang ingin dibuat : ")
            if any(char.isdigit() for char in password) and any(char.isalpha() for char in password):                    
                akun[username] = password
                print("\n==><==        Akun Anda berhasil dibuat       ==><==")   
                break 
            else:
                print("\nPassword Harus berisi gabungan Huruf dan Angka")
    tunggu_enter()    


# Fungsi Untuk Masuk dengan akun yg sebelumnya dibuat'
def login_akun():
    membersihkan_layar()
    print("==========   Menu 'Login'   ==========\n")
    username = input("Masukkan Username Anda : ")
    password = input("Masukkan Password Anda : ")
    if username in akun and akun[username] == password:
        print(f"\n==><==       Login Berhasil, Selamat Menjadi Member Baru {username}       ==><==")
        return True  # Login berhasil
    else:
        print("\nLogin Gagal! Username atau Password salah")
        return False  # Login gagal


# Fungsi untuk menjalankan semua kode yang berhubungan dengan registrasi akun
def main_registrasi():
    print("\n==================            Registrasi Akun         ================")
    print("==========        Member Perpustakaan E-Heulang Bersama       ==========\n")

    while True:
        print("\nMenu Registrasi : ")
        print("1. Buat Akun")
        print("2. Login Akun")
        print("3. Keluar")
        
        pilihan_registrasi = int(input("Masukkan Pilihan [1 - 3] : ")) 
        if pilihan_registrasi == 1:
            buat_akun()
        elif pilihan_registrasi == 2:
            if login_akun():
                return True  # Berhasil login, lanjut ke program perpustakaan
        elif pilihan_registrasi == 3:
            print("Kamu telah Keluar dari program registrasi")
            return False  # Keluar dari program utama
        else:
            print("Masukkan pilihan yg sesuai")


"""Daftar buku di perpustakaan"""
# Data buku dalam bentuk dictionary (untuk awal inisialisasi)
data_buku = {
    'Kode Buku': ['001', '002', '003', '004', '005', '006', '007', '008', '009', '010'],
    'Penulis': ['Tereliye', 'Tereliye', 'Tereliye', 'Tereliye', 'Tereliye', 'Eka Kurniawan',
                'Pramoedya Ananta Toer', 'Leila S. Chudori', 'Fiersa Besari', 'Andrea Hirata'],
    'Judul Buku': ['Komet', 'Bulan', 'Matahari', 'Bumi', 'Bintang', 'Lelaki Harimau',
                   'Bumi Manusia', 'Laut Bercerita', 'Garis Waktu', 'Laskar Pelangi'],
    'Tahun Terbit': [2011, 2012, 2013, 2010, 2014, 2004, 1980, 2011, 2017, 2005],
    'Stok': [5, 3, 4, 2, 4, 4, 5, 4, 3, 5],
}

# Konversi data_buku menjadi DataFrame pandas
daftar_buku = pd.DataFrame(data_buku)

# Fungsi untuk menampilkan buku
def tampilkan_buku():
    membersihkan_layar()    
    print(f"\n\t\t\t\t\t\t\t{'='*35}")
    print("\t\t\t\t\t\t========           Perpustakaan            ========")
    print("\t\t\t\t\t\t========          Heulang Bersama          ========")
    print(f"\t\t\t\t\t\t\t{'='*35}")
    print("="*150)
    print(f"\t{'Kode Buku':<10} \t{'Penulis':<35}{'Judul Buku':<35}{'Tahun Terbit':<15}\t\t{'Stok':<5}")
    print("="*150)
    
    # Looping menggunakan DataFrame untuk menampilkan data
    for index, row in daftar_buku.iterrows():
        print(f"\t{row['Kode Buku']:<10}  \t{row['Penulis']:<35}{row['Judul Buku']:<35}{row['Tahun Terbit']:<15}\t\t{row['Stok']:<5}")
    
    print(f"{'_'*150}\n")
    print(f"{'='*150}\n")
    tunggu_enter()


# Fungsi untuk meminjam buku
def pinjam_buku():
    tampilkan_buku()
    kode_buku = input("Masukkan kode buku yang ingin dipinjam: ")
    buku = daftar_buku[daftar_buku['Kode Buku'] == kode_buku]
    print(buku)
    tunggu_enter()
    if not buku.empty:
        if buku.iloc[0]['Stok'] > 0:
            daftar_buku.loc[daftar_buku['Kode Buku'] == kode_buku, 'Stok'] -= 1
            print(f"Buku '{buku.iloc[0]['Judul Buku']}' berhasil dipinjam!")
        else:
            print("Maaf, stok buku sedang habis.")
    else:
        print("Kode buku tidak ditemukan.")
    tunggu_enter()


# Fungsi untuk mengembalikan buku
def balikin_buku():
    tampilkan_buku()
    kode_buku = input("Masukkan kode buku yang ingin dikembalikan: ")
    buku = daftar_buku[daftar_buku['Kode Buku'] == kode_buku]
    if not buku.empty:
        daftar_buku.loc[daftar_buku['Kode Buku'] == kode_buku, 'Stok'] += 1
        print(f"Buku '{buku.iloc[0]['Judul Buku']}' berhasil dikembalikan!")
    else:
        print("Kode buku tidak ditemukan.")
    tunggu_enter()


# Logika Buat Pilihan Program Buku nya
def main_program(username):    
    while True: 
        membersihkan_layar()
        print(f"\n\n{'='*40}")
        print("         Menu Aplikasi Perpustakaan            ")
        print("            E-Heulang Bersama          ")
        print("="*40)
        print(f"\n(Login sebagai: {username})         ")
        print("\n1. Tampilkan Buku")
        print("2. Pinjem Buku")
        print("3. Balikkin Buku")
        print("4. Keluar Program")
        
        try:
            pilihan = int(input("Masukkan pilihan [1 - 4]: "))
            if pilihan == 1:
                tampilkan_buku()
            elif pilihan == 2:
                pinjam_buku()
            elif pilihan == 3:
                balikin_buku()
            elif pilihan == 4:
                print("Terima kasih telah menggunakan aplikasi perpustakaan.")
                break
            else:
                print("Masukkan angka pilihan yang sesuai!")
        except ValueError:
            print("Input harus berupa angka!")
            tunggu_enter()

# Gabung Program Registrasi dan Perpustakaan
def main():
    if main_registrasi():
        username = input("\n==>  Masukkan Username untuk login ke Aplikasi perpustakaan : ")
        print(f"Selamat datang di sistem Aplikasi perpustakaan, {username} ^_^ !")
        tunggu_enter()
        if username in akun:
            main_program(username)
        else:
            print("Username tidak terdaftar. Silakan Periksa Kembali.")

main()
