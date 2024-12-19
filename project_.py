import os  

# Fungsi untuk membersihkan layar terminal sebelumnya dengan modul 'os'
def membersihkan_layar():
    os.system('cls')


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
                print("\nPassword Harus berisi gabungan Alphabet dan Angka")
    input("\nTekan Enter untuk melanjutkan...")

# Fungsi Untuk Masuk dengan akun yg sebelumnya dibuat'
def login_akun():
    membersihkan_layar()
    print("==========   Menu 'Login'   ==========\n")
    username = input("Masukkan Username Anda : ")
    password = input("Masukkan Password Anda : ")
    if username in akun and akun[username] == password:
        print(f"\n==><==       Login Berhasil, Selamat Datang {username}       ==><==")
        return True  # Login berhasil
    else:
        print("\nLogin Gagal! Username atau Password salah")
        return False  # Login gagal


# Fungsi untuk menjalankan semua kode yang berhubungan dengan registrasi akun
def main_registrasi():
    print("\n===============              Registrasi Akun     ===============")
    print("==========         Member Perpustakaan E-Heulang Bersama      ==========\n")

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
daftar_buku = {
    '001': {'penulis': 'Tereliye', 'title': 'Komet', 'stok': 5,'tahun_terbit': 2011},
    '002': {'penulis': 'Tereliye', 'title': 'Bulan', 'stok': 3,'tahun_terbit': 2012},
    '003': {'penulis': 'Tereliye', 'title': 'Matahari', 'stok': 4,'tahun_terbit': 2013},
    '004': {'penulis': 'Tereliye', 'title': 'Bumi', 'stok': 2,'tahun_terbit': 2010},
    '005': {'penulis': 'Tereliye', 'title': 'Bintang', 'stok': 4,'tahun_terbit': 2014},
    '006': {'penulis': 'Eka Kurniawan', 'title': 'Lelaki Harimau', 'stok': 4,'tahun_terbit': 2004},
    '007': {'penulis': 'Pramoedya Ananta Toer', 'title': 'Bumi Manusia', 'stok': 5,'tahun_terbit': 1980},
    '008': {'penulis': 'Leila S. Chudori', 'title': 'Laut Bercerita', 'stok': 4,'tahun_terbit': 2011},
    '009': {'penulis': 'Fiersa Besari', 'title': 'Garis Waktu', 'stok': 3,'tahun_terbit': 2017},
    '010': {'penulis': 'Andrea Hirata', 'title': 'Laskar Pelangi', 'stok': 5,'tahun_terbit': 2005}
}


# Logika Buat Tampilin Bukunya
def tampilkan_buku():
    membersihkan_layar()    
    print(f"\n\t\t\t\t\t\t\t{'='*35}")
    print("\t\t\t\t\t\t========           Perpustakaan            ========")
    print("\t\t\t\t\t\t========          Heulang Bersama          ========")
    print(f"\t\t\t\t\t\t\t{'='*35}")
    print("="*150)
    print(f"\t{'Kode Buku':<10} \t{'Penulis':<35}{'Judul Buku':<35}{'Tahun Terbit':<15}\t\t{'Stok':<5}")
    print("="*150)
    for key, value in daftar_buku.items():
        print(f"\t{key:<10} \t{value['penulis']:<35}{value['title']:<35}{value['tahun_terbit']:<15}\t\t{value['stok']:<5}")
    print(f"{'_'*150}\n")
    print(f"{'='*150}\n")

    input("\nTekan Enter untuk Melanjutkan atau kembali ke menu...")

# Logika Buat Pinjem Bukunya
def pinjam_buku(username):
    tampilkan_buku()
    input("\nTekan Enter untuk melanjutkan meminjam buku...")

    print(f"\nHalo, {username}. Silahkan Pilih Kode Buku yang ingin dipinjam:")
    no_buku = input("\n=> Masukkan Kode Buku yang ingin dipinjam : ")

    if no_buku in daftar_buku.keys():
        hari = int(input("=> Masukkan jumlah hari untuk meminjam buku : "))
        if daftar_buku[no_buku]['stok'] > 0:
            daftar_buku[no_buku]['stok'] -= 1
            daftar_buku[no_buku]['peminjam'].append(username)
            print(f"\nBuku '{daftar_buku[no_buku]['title']}' berhasil dipinjam. Untuk {hari} hari")
            
        else:
            print("Maaf, stok buku sudah habis.")
    else:
        print("Kode buku tidak valid!")
    input("\nTekan Enter untuk melanjutkan...")


# Logika Buat Balikkin Bukunya Sekaligus Fitur Denda
def balikin_buku(username, hari):
    print(f"\nHalo, {username}. Berikut daftar buku yang sedang Anda pinjam :")
    buku_dipinjam = [key for key, value in daftar_buku.items() if username in value['peminjam']]
    
    if not buku_dipinjam:
        print("Anda belum meminjam buku.")
        return

    for kode in buku_dipinjam:
        print(f"- {kode}: {daftar_buku[kode]['title']}")
    
    no_buku = input("\nMasukkan Kode Buku yang ingin dikembalikan: ")
    
    if no_buku in buku_dipinjam:
        # Memasukkan jumlah hari keterlambatan
        try:
            hari_terlambat = int(input(f"\nMasukkan total jumlah hari untuk buku '{daftar_buku[no_buku]['title']}' yang sebelumnya kamu pinjam : "))
            if hari_terlambat < 0:
                print("Jumlah hari keterlambatan tidak bisa negatif.")
                return
        except ValueError:
            print("Input harus berupa angka.")
            return

        # Menghitung denda
        denda_per_hari = 500  # Denda per hari keterlambatan
        denda_total = hari_terlambat * denda_per_hari

        # Proses pengembalian buku
        daftar_buku[no_buku]['stok'] += 1
        daftar_buku[no_buku]['peminjam'].remove(username)

        if hari_terlambat > hari:
            total_hari_terlambat = hari_terlambat - hari
            print(f"Buku '{daftar_buku[no_buku]['title']}' berhasil dikembalikan. Anda terlambat {total_hari_terlambat} hari. Denda yang harus dibayar: Rp {denda_total}.")
        else:
            print(f"Buku '{daftar_buku[no_buku]['title']}' berhasil dikembalikan tanpa denda.")
    else:
        print("Kode buku tidak valid atau Anda tidak meminjam buku ini.")
    input("\nTekan Enter untuk melanjutkan...")


# Logika Buat Pilihan Program Buku nya
def main_program(username, hari):    
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

        pilihan = int(input("\n==> Masukkan Pilihan untuk menjalankan Sistem : "))
        
        if pilihan == 1:
            tampilkan_buku()
        elif pilihan == 2:
            pinjam_buku(username)
        elif pilihan == 3:
            balikin_buku(username, hari)    
        elif pilihan == 4:
            break
        else:
            print("Masukkan angka pilihan yang sesuai!")

# Gabung Program Registrasi dan Perpustakaan
def main():
    while True:
        if main_registrasi():
            username = input("\n==>  Masukkan Username untuk login ke Aplikasi perpustakaan : ")
            if username in akun:
                print(f"Selamat datang di sistem Aplikasi perpustakaan, {username} ^_^ !")
                hari = 7
                main_program(username, hari)
            else:
                print("Username tidak terdaftar. Silakan Periksa Kembali.")
main()