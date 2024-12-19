
akun = {}


def buat_akun():
        username = input("Masukkan Username yang ingin dibuat : ")
        if username in akun:
            print("\nUsername Sudah Terdaftar")
        else:
            while True:
                password = input("Masukkan Password yang ingin dibuat : ")
                if any(char.isdigit() for char in password) and any(char.isalpha() for char in password):                    
                    akun[username] = password
                    print("\nAkun Anda berhasil dibuat")   
                    break 
                else:
                    print("\nPassword Harus berisi dengan gabungan ehuruf dan angka juga")


def login_akun():
    username = input("Masukkan Username Anda : ")
    password = input("Masukkan Password Anda : ")
    if username in akun and akun[username] == password:
        print(f"Login Berhasil, Selamat Datang {username} dengan pass = {password}")
    else:
        print("Login Gagal! Username dan Password salah")


def main_registrasi():
    print("\n===============       Account Registration     ===============")
    print("==========         Member of E-Heulang Library      ==========\n")


    while True:
        print("\nMenu Registrasi : ")
        print("1. Buat Akun")
        print("2. Login Akun")
        print("3. Keluar")
        
        pilihan_registrasi = int(input("Masukkan Pilihan [1 - 3] : ")) 
        if pilihan_registrasi == 1:
            buat_akun()
        elif pilihan_registrasi == 2:
            login_akun()
        elif pilihan_registrasi == 3:
            print("kamu telah Keluar dari main registrasi")
            break
        else:
            print("Masukkan pilihan yg sesuai")
main_registrasi()


