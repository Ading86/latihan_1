from functools import reduce

from datetime import datetime
import datetime
last= 2


MENU_AWAL = """
Selamat datang di perpustakaan
MENU
1. Login admin
2. Login user
"""

MENU_ADMIN = """
Menu Admin
1. Tambahkan buku
2. Hapus buku
3. Edit buku
4. Tampilkan semua buku
5. Tampilkan anggota
6. Tambah anggota
7. Hapus anggota
8. Edit anggota
9. EXIT

"""
# we
MENU_USER = """ 
Menu User
1. Tampilkan semua buku
2. Tampilkan buku yang dipinjam
3. Pinjam buku
4. Kembalikan buku
5. Riwayat 
6. Tanggal Join
7. Filter
8. reduce
9. EXIT

"""
# list
buku = ['madilog', 'komunis', 'anarkisme', 'filsafat']

buku_user = ['memasak', 'mananam']
anggota =[
    {
        "id":0,
        "nama":"akak",
        "riwayat":["hatta","kalkulus"],
        "mulai": datetime.date(2022,9,28),
        "pernah":["hatta","kalkulus"]
    },
    {
        "id":1,
        "nama":"alif",
        "riwayat":[],
        "mulai": datetime.date(2022,2,3),
        "pernah":[]
    }
]
#//////////////////////////////////////////////////////////////////////////////////////////////////
def hof(n,sogo,boleanya):
    a=n
    b=sogo
    def panggil_hapus(a,b):
        for x in (anggota[a]["riwayat"]):
            if b == x:
                (anggota[a]["riwayat"].remove(b))
                print("buku so hapus")

    def panggil_editnya(a,b):
        rumah =0
        for x in (anggota[a]["riwayat"]):

            if b == x:
                josua = str(input("ganti dengan : "))
                (anggota[a]["riwayat"][rumah])=josua
            
            
            rumah = rumah+1

    if boleanya==1:
        return panggil_hapus(a,b)

    else :
        return panggil_editnya(a,b)

    

    

def mapping(n):
    
    ini_map= map(lambda hus: hus+" pernah dipinjam",anggota[n]["riwayat"])
    print("====daftar====")
    for x in ini_map:
        print(x)

def filltering(n):
    rahman = str(input("filter : "))
    joko=filter(lambda xo:xo==rahman,anggota[n]["riwayat"])
    print(tuple(joko))
def pinjam_book(list,list2):
    print("pinjam book")
    i = 0
    tes = False
    buku_pinjam = str(input("buku yang ingin dipinjam : "))

    for x in list:
        if buku_pinjam == list[i]:
            list.remove(buku_pinjam)
            
            (list2[i]["riwayat"].append(buku_pinjam))
            (list2[i]["pernah"].append(buku_pinjam))
            tes = True

        i = i+1
    if tes == False:
        print("")
        print("buku tidak ada bro")





def tampil_anggota(list):
    for x in list:
        print(x)

def tambah_anggota (list):
    
    
    tambah_nama = str(input("Nama : "))
    list.append({
        "id":last,
        "nama":tambah_nama,
        "riwayat":[],
        "mulai": datetime.date.today(),
        "pernah":[]
    })

def hapusini(int1,int2,str1):
    if str1==(anggota[int1]["riwayat"][int2]):
        (anggota[int1]["riwayat"].remove(str1))

def editini(int1,int2,str1):
    if str1==(anggota[int1]["riwayat"][int2]):
        gantien= str(input("ganti dengan : "))
        (anggota[int1]["riwayat"][int2])=gantien
        


def hapus_anggota(list):
    i = 0
    hapus_buku = int(input("id anggota yang ingin dihapus : "))
    # list.remove(hapus_buku)
    tes = False
    for x in list:

        if hapus_buku == list[i]["id"]:
            list.remove(list[i])
            tes = True
            
        i = i+1

    if tes == False:
        print("")
        print("id anggota tidak ada puki")

def edit_anggota(list):
    i = 0
    hapus_buku = int(input("id anggota yang ingin dihapus : "))
    # list.remove(hapus_buku)
    tes = False
    for x in list:

        if hapus_buku == list[i]["id"]:
            names = str(input("ganti nama  : "))
            list[i]["nama"]=names
            
            tes = True
        i = i+1

    if tes == False:
        print("")
        print("id anggota tidak ada puki")




#///////////////////////////////////////////////////////////////////////////////
# tampil



def tampil(list):
    for x in list:
        print(x)


# tambah buku
def tambah(list):
    tambah_buku = str(input("Judul Buku : "))
    list.append(tambah_buku)
    print("Buku ", tambah_buku, " telah ditambahkan")


def hapus(list):
    i = 0
    hapus_buku = str(input("judul buku yg ingin dihapus : "))
    # list.remove(hapus_buku)
    tes = False
    for x in list:

        if hapus_buku == list[i]:
            list.remove(hapus_buku)
            tes = True
            print("buku ", hapus_buku, " telah dihapus dari daftar")
        i = i+1

    if tes == False:
        print("")
        print("buku tidak ada bro")




# pindah

def pinjam(list, list2):
    i = 0
    tes = False
    buku_pinjam = str(input("buku yang ingin dipinjam : "))

    for x in list2:
        if buku_pinjam == list2[i]:
            list2.remove(buku_pinjam)
            list.append(buku_pinjam)
            tes = True

        i = i+1
    if tes == False:
        print("")
        print("buku tidak ada bro")


def edit(list):
    i = 0
    tes = False
    buku_pinjam = str(input("buku yang ingin diubah : "))

    for x in list:

        if buku_pinjam == list[i]:

            ubah = str(input("ganti dengan  : "))
            list[i] = ubah
            tes = True

        i = i+1
    if tes == False:
        print("")
        print("buku tidak ada bro")


while 1 < 2:

    print(MENU_AWAL)
    pilihan = int(input("Pilihan: "))

    if pilihan == 1:

        print("Login admin")
        id = input("Masukan id: ")
        

        # aaaaaaaaaaaaaaaaaaaaaaaddddddddddddmiiiiiiiiiiiiiiiiinnnnnnnnnnnnnnnnnnn

        if id == "min":
            while 3 < 23:
                print(MENU_ADMIN)
                
                admin_input = int(input("Pilihan: "))
                if admin_input == 1:
                    print("tambah bukunya brooo")
                    print("1. Perpus")
                    print("2. Pinjam")
                    do = int(input("pilih  :"))
                    if do ==1:
                        tampil(buku)
                        tambah(buku)
                    elif do ==2:
                        print("=id=")
                        hatta =0
                        for x in anggota:
                            print(anggota[hatta]["id"])
                            hatta = hatta+1
                        idnya = int(input("pilihan id : "))
                        hatta =0
                        hohoho= False
                        for x in anggota:
                            if idnya== (anggota[hatta]["id"]):
                                booktambah= str(input("tambah : "))
                                (anggota[idnya]["riwayat"].append(booktambah))
                                (anggota[idnya]["pernah"].append(booktambah))
                                hohoho=True
                            hatta=hatta+1
                        if hohoho ==False:
                            print("id kosong")
                                
                        

                        
                    else:
                        print("salah pilih puki")

                        

                    
                elif admin_input == 2:
                    print("hapus bukunya broo")
                    print("1. Perpus")
                    print("2. Pinjam")
                    do = int(input("pilih  :"))
                    if do ==1:
                        tampil(buku)
                        hapus(buku)
                    elif do ==2:
                        print("=id=")
                        hatta =0
                        for x in anggota:
                            print(anggota[hatta]["id"])
                            hatta = hatta+1
                        idnya = int(input("pilihan id : "))
                        hatta =0
                        hohoho= False
                        for x in anggota:
                            if idnya== (anggota[hatta]["id"]):
                                iniapa= str(input("hapus : "))
                                
                                
                                hohoho=True
                                
                                panggil_hapus=hof(idnya,iniapa,1)
                            hatta=hatta+1
                        if hohoho ==False:
                            print("id kosong")

                    else:
                        print("salah pilih puki")

                elif admin_input == 3:
                    print("edit bukunya broo")
                    print("1. Perpus")
                    print("2. Pinjam")
                    do = int(input("pilih  :"))
                    if do ==1:
                        tampil(buku)
                        hapus(buku)
                    elif do ==2:
                        print("=id=")
                        hatta =0
                        for x in anggota:
                            print(anggota[hatta]["id"])
                            hatta = hatta+1
                        idnya = int(input("pilihan id : "))
                        hatta =0
                        hohoho= False
                        for x in anggota:
                            if idnya== (anggota[hatta]["id"]):
                                iniapa= str(input("hapus : "))
                                
                                panggil_editnya=hof(idnya,iniapa,2)
                                hohoho=True
                            hatta=hatta+1
                        if hohoho ==False:
                            print("id kosong")

                    else:
                        print("salah pilih puki")
                    

                elif admin_input == 4:
                    print("edit bukunya broo")
                    print("1. Perpus")
                    print("2. Pinjam")
                    do = int(input("pilih  :"))
                    if do ==1:
                        tampil(buku) 
                    elif do ==2:
                        print("=id=")
                        hatta =0
                        for x in anggota:
                            print(anggota[hatta]["id"])
                            hatta = hatta+1
                        idnya = int(input("pilihan id : "))
                        hatta =0
                        hohoho= False
                        for x in anggota:
                            if idnya== (anggota[hatta]["id"]):
                                hohoho=True
                                print("=========")
                                for alam in (anggota[idnya]["riwayat"]):
                                    print(alam)
                                print("=========")
                            hatta=hatta+1
                        if hohoho ==False:
                            print("id kosong")
                    else:
                        print("salah pilih puki")
                
                elif admin_input == 5:
                    print("=====================================anggota=========================================")
                    tampil_anggota(anggota)
                
                elif admin_input == 6:
                    tambah_anggota(anggota)
                    last = last +1
                
                elif admin_input == 7:
                    print("=====================================anggota=========================================")
                    tampil_anggota(anggota)
                    hapus_anggota(anggota)

                

                elif admin_input == 8:
                    print("edit anggota")
                    print("=====================================anggota=========================================")
                    tampil_anggota(anggota)
                    edit_anggota(anggota)
                elif admin_input == 9:
                    print("goodbhay motherfvker")
                    break
                else:
                    print("salah pilih gosi")

        else:
            print("")
            print("maaf salah")
            print("")


# ussssssssssssssssssssseeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeerrrrrrrrrrrrrrrrrrrrrrrrrrrrr
    elif pilihan == 2:
        i = 0
        pilih_user = int(input("Masukkan ID : "))
        
        for x in anggota:

            if pilih_user == anggota[i]["id"]:
                while 1>0:
                    print(MENU_USER)
                    yg_ini = int(input("pilih  : "))

                    if yg_ini ==1:
                        print("==daftar==")
                        tampil(buku)
                    elif yg_ini ==2:
                        
                        print("==daftar==")
                        for z in anggota[i]["riwayat"]:
                            print(z)

                    elif yg_ini==3:
                        tampil(buku)
                        
                        pinjam_ygini = str(input("buku yang ingin dipinjam : "))
                        angka=0
                        ini_bol=False
                        for z in buku:
                            if pinjam_ygini == buku[angka]:
                                (anggota[i]["riwayat"].append(pinjam_ygini))
                                buku.remove(pinjam_ygini)
                                ini_bol= True
                            angka=angka+1
                        if ini_bol==False:
                            print("buku tidak ada puki")


                    elif yg_ini==4:
                        print("==daftar==")
                        for z in anggota[i]["riwayat"]:
                            print(z)
                        
                        io=0
                        hooh=False
                        back_book= str(input("kembalikkan: "))

                        for lop in anggota[i]["riwayat"]:
                            if back_book== (anggota[i]["riwayat"][io]):
                                (anggota[i]["riwayat"].remove(back_book))
                                buku.append(back_book)
                                hooh = True
                            
                            io=io+1
                        if hooh == False:
                            print("buku tidak ada puki")

                    elif yg_ini==5:
                        
                        
                        mapping(i)
 
                    elif yg_ini==6:
                        print("")
                        print("Anda mulai join pada")
                        tanggal =(anggota[i]["mulai"])
                        print(tanggal.strftime("Pada %A %d %Y"))

                    elif yg_ini ==7:
                        print("ini filter")
                        filltering(i)

                    elif yg_ini ==8:
                        print("jumlah id")
                        joke = reduce(lambda x,y: x+"  "+y, (anggota[i]["riwayat"]))
                        print(f"jumlah semua element dalam list = {joke}")

                    elif yg_ini ==9:
                        print("ok bhay")
                        break
                    else:
                        print("")
                        print("salah pilih gosi")

                        
            i = i+1

        print("id tidak ada puki")


    elif pilihan == 3:
        break