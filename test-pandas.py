# Modul yang diperlukan dalam program ini
import pandas as pd 
import os   
import sys


print("\n==============================================================")
print("|                                                            |")
print("|       SELAMAT DATANG DI APLIKASI PERPUSTAKAAN SIMMY ^_^    |")
print("|                                                            |")
print("==============================================================")

username = input("\n==> Masukkan Nama anda untuk menjalankan menu aplikasi : ")


# Fungsi untuk membersihkan layar tampilan
def membersihkan_layar():
    os.system('cls')

# Fungsi untuk melanjutkan jalannya program dengan meng klik Enter
def tunggu_enter():
    input("\nTekan Enter untuk melanjutkan...")

# Variabel dibawah adalah untuk menyimpan data buku yang sedang dipinjem
buku_dipinjam = {}

# Data buku dalam bentuk dictionary 
daftar_buku = {
    '001': {'penulis': 'Tereliye', 'title': 'Komet', 'stok': 5, 'tahun_terbit': 2011},
    '002': {'penulis': 'Tereliye', 'title': 'Bulan', 'stok': 3, 'tahun_terbit': 2012},
    '003': {'penulis': 'Tereliye', 'title': 'Matahari', 'stok': 4, 'tahun_terbit': 2013},
    '004': {'penulis': 'Tereliye', 'title': 'Bumi', 'stok': 2, 'tahun_terbit': 2010},
    '005': {'penulis': 'Tereliye', 'title': 'Bintang', 'stok': 4, 'tahun_terbit': 2014},
    '006': {'penulis': 'Eka Kurniawan', 'title': 'Lelaki Harimau', 'stok': 4, 'tahun_terbit': 2004},
    '007': {'penulis': 'Pramoedya Ananta Toer', 'title': 'Bumi Manusia', 'stok': 5, 'tahun_terbit': 1980},
    '008': {'penulis': 'Leila S. Chudori', 'title': 'Laut Bercerita', 'stok': 4, 'tahun_terbit': 2011},
    '009': {'penulis': 'Fiersa Besari', 'title': 'Garis Waktu', 'stok': 3, 'tahun_terbit': 2017},
    '010': {'penulis': 'Andrea Hirata', 'title': 'Laskar Pelangi', 'stok': 5, 'tahun_terbit': 2005}
}

# Fungsi untuk menampilkan buku
def tampilkan_buku():
    membersihkan_layar()

    # membuat data buku baru agar bisa diakses dengan pandas
    data_buku = {
        "Kode Buku": list(daftar_buku.keys()),
        "Penulis": [],
        "Judul Buku": [],
        "Tahun Terbit": [],
        "Stok": []
    }
    
    for buku in daftar_buku.values():
        data_buku["Penulis"].append(buku['penulis'])
        data_buku["Judul Buku"].append(buku['title'])
        data_buku["Tahun Terbit"].append(buku['tahun_terbit'])
        data_buku["Stok"].append(buku['stok'])
    
    
    # menampilkan tampilan daftar buku dengan implementasi pandas
    df_buku = pd.DataFrame(data_buku)
    
    print(f"\n\t\t\t\t\t\t\t{'='*35}")
    print("\t\t\t\t\t\t========           Perpustakaan            ========")
    print("\t\t\t\t\t\t========          <== SIMMY ==>            ========")
    print(f"\t\t\t\t\t\t\t{'='*35}")
    print("="*150)
    print(f"\t{'Kode Buku':<10} \t{'Penulis':<35}{'Judul Buku':<35}{'Tahun Terbit':<15}\t\t{'Stok':<5}")
    print("="*150)
    
    for index, row in df_buku.iterrows():
        print(f"\t{row['Kode Buku']:<10}  \t{row['Penulis']:<35}{row['Judul Buku']:<35}{row['Tahun Terbit']:<15}\t\t{row['Stok']:<5}")
    
    print(f"{'_'*150}\n")
    print(f"{'='*150}\n")
    
    tunggu_enter()


# Fungsi untuk meminjam buku
def pinjam_buku(username):
    tampilkan_buku() # memanggil fungsi untuk menampilkan daftar buku
    print(f"\nHalo, {username}.")
    no_buku = input("=> Masukkan Kode Buku yang ingin dipinjam : ") # input untuk memasukkan kode buku yg ingin dipinjem

    # Mengecek apakah input kode buku nya sesuai dengan yg ada di daftar buku
    if no_buku in daftar_buku.keys():
        if daftar_buku[no_buku]['stok'] > 0:
            daftar_buku[no_buku]['stok'] -= 1
            
            # menambahkan buku ke daftar pinjaman user
            if username not in buku_dipinjam:
                buku_dipinjam[username] = []
            
            buku_dipinjam[username].append(no_buku)
            
            print(f"\n==>>> Buku '{daftar_buku[no_buku]['title']}' berhasil dipinjam.")
            print("\n==>>>  Batas waktu pinjam buku adalah 14 hari, lebih dari itu akan dikenakan denda sebesar 5.000 per hari.")
        else:
            print("Maaf, stok buku sudah habis.")
    else:
        print("Kode buku tidak valid!")
    tunggu_enter()


# Fungsi untuk mengembalikan buku
def balikin_buku(username):
    print(f"\nHalo, {username} ^_^.")
    print("Berikut daftar buku yang sedang Anda pinjam :")
    
    # untuk mengecek apakah user punya buku yang dipinjam
    if username not in buku_dipinjam or not buku_dipinjam[username]:
        print("Tidak ada buku yang perlu dikembalikan.")
        tunggu_enter()
        return False

    # Menampilkan daftar buku yang sedang dipinjam
    for kode in buku_dipinjam[username]:
        print(f"- Kode Buku => {kode} : Buku '{daftar_buku[kode]['title']}' Karya {daftar_buku[kode]['penulis']} ")

    no_buku = input("\n==> Masukkan Kode Buku yang ingin dikembalikan: ") # input untuk memasukkan kode buku yg ingin dipinjem

    # Memproses pengembalian buku
    if no_buku in buku_dipinjam[username]:
        try:
            total_hari_pinjam = int(input(f"==> Masukkan jumlah hari pinjam untuk '{daftar_buku[no_buku]['title']}': ")) # input total hari pinjam buku
        
            # buat variabel baru untuk 'waktu batas pinjam' dan 'denda perhari'
            batas_pinjam = 14
            denda_per_hari = 5000

            # Hitung hari terlambat
            if total_hari_pinjam > batas_pinjam:
                hari_telat = total_hari_pinjam - batas_pinjam
            else:
                hari_telat = 0

            denda_total = hari_telat * denda_per_hari

            # Kembalikan buku dan update stok
            daftar_buku[no_buku]['stok'] += 1
            buku_dipinjam[username].remove(no_buku)

            # Tampilkan informasi pengembalian
            if hari_telat > 0:
                print(f"\n==><==        Buku '{daftar_buku[no_buku]['title']}' berhasil dikembalikan.       ==><==")
                print(f"\nBatas Waktu Pinjam => {batas_pinjam} hari")
                print(f"Total Waktu Pinjam Anda => {total_hari_pinjam} hari")
                print(f"Denda Per hari => Rp. {denda_per_hari}")
                print(f"\n==>   Anda terlambat {hari_telat} hari. Denda: Rp. {denda_total}")
            else:
                print(f"==><==      Buku '{daftar_buku[no_buku]['title']}' berhasil dikembalikan tanpa denda.       ==><==")
        
        except ValueError:
            print("Input harus berupa angka.")
    else:
        print("Kode buku tidak valid atau Anda tidak meminjam buku ini.")
    
    tunggu_enter()

# Fungsi yang berisi logika untuk menjalankan pilihan menu aplikasi perpustakaan nya
def main_program(username):    
    while True:
        membersihkan_layar()
        print(f"\n\n{'='*40}")
        print("         Menu Aplikasi Perpustakaan            ")
        print("               <== SIMMY ==>                   ")
        print("="*40)
        print(f"\n(Login sebagai: {username})         ")
        print("\n1. Menampilkan Buku")
        print("2. Meminjam Buku")
        print("3. Mengembalikkan Buku")
        print("4. Keluar Program")

        pilihan = int(input("\n==> Masukkan Pilihan untuk menjalankan Sistem : ")) # input untuk memilih menu yang ingin dijalankan
        
        
        if pilihan == 1:
            tampilkan_buku()
        elif pilihan == 2:
            pinjam_buku(username)
        elif pilihan == 3:
            balikin_buku(username)    
        elif pilihan == 4:
            print("\nAnda Berhasil Keluar Dari program Aplikasi Perpustakaan")
            print("Terimakasih Telah Menggunakan Program Aplikasi Perpustakaan Ini ^_^")
            input("\nTekan Enter Untuk Membersihkan layar sepenuhnya...")
            membersihkan_layar()
            sys.exit()
        
        else:
            print("Masukkan angka pilihan yang sesuai!")


main_program(username)