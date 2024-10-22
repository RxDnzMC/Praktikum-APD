# ---------------------------------------=[ VARIABEL GLOBAL ]=---------------------------------------

adminpw = "admin123"
pilihanadmin = 0
pilihanpengguna = 0
resep = {}
pilihanresep = 0
pilihanregister = ""
login = 0
registered = 0
pengguna = ""
penggunapw = ""
pilihlogin = 0


# ---------------------------------------=[ MENU UTAMA ]=---------------------------------------


def menu_login():
    global pilihanadmin, pilihanpengguna
    pilihanadmin = 0
    pilihanpengguna = 0
    pilihan1 = input("""
=========== Admin / Pengguna ===========
Selamat Datang Di Daftar Menu Resep Makanan
Kamu Disini Sebagai Apa
(admin/pengguna/keluar) : """)
    if pilihan1.lower() == "admin":
        pilihanadmin = 1
        return pilihanadmin
    elif pilihan1.lower() == "pengguna":
        pilihanpengguna = 1
        return pilihanpengguna
    elif pilihan1.lower() == "keluar":
        exit("Terimakasih Sudah Mencoba Program Yang Saya Buat")
    else:
        print("Input Yang Anda Masukkan Salah!! Coba Ulangi!!")


# ---------------------------------------=[ HALAMAN ADMIN ]=---------------------------------------


def menu_adminlogin():
    global adminpw, pilihanadmin
    adminlogin = input("Masukkan Password : ")
    if adminlogin == adminpw:
        pilihanadmin = 2
        return pilihanadmin
    else:
            print("Password Anda Salah!!")


# ---------------------------------------=[ MENU ADMIN ]=---------------------------------------


def menu_admin():
    try: 
        pilihanresep = int(input("""
====== PANEL ADMIN ======
1. Tambah Resep
2. Tampilkan Resep
3. Ubah Isi Resep
4. Hapus Resep
5. Keluar
=======================                                                                                                                                                                    
pilihan : """))
        if 1 <= pilihanresep <= 5:
            return pilihanresep
        else:
            print("Silahkan Memilih 1-5!!")
    except ValueError:
        print("Input Salah!! Tolong Masukkan angka dari 1 sampai 5!!")


def tambah_resep():
    stepresep = []
    counter = 1
    judul = input("Judul Resep: ")
    print("Buatlah Step Resep Sesuai Yang Diinginkan. Ketik [berhenti] Untuk Berhenti")
    while True:
        print(f"Masukkan Step Ke - {counter}")
        stepinput = input()
        if stepinput.lower() == "berhenti":
            break
        stepresep.append(stepinput)
        counter += 1
    resep[judul] = stepresep
    return resep


def tampilkan_resep():
    global resep
    if not resep:
        print("Tidak Ada Resep!!")
    else:
        for i,j in resep.items():
            print(f"\nResep {i} Adalah:")
            for k,l in enumerate(j):
                print(f"Step {k+1}: {l}")
    print()


def mengubah_resep():
    global resep
    if not resep:
        print("Tidak Ada Resep Yang Dapat Diubah!!")
    else:
        for i, j in enumerate(resep):
            print(f"{i + 1}. {j}")
        try:
            pilihanubah = int(input("Pilih Nomor Resep Yang Ingin Diubah : "))
            if 1 <= pilihanubah <= len(resep):
                ubahresep = list(resep.keys())[pilihanubah - 1]
                print(f"Mengubah resep: {ubahresep}")
                stepresep = []
                counter = 1
                print("Buatlah Step Resep Sesuai Yang Diinginkan. Ketik [berhenti] Untuk Berhenti")
                while True:
                    print(f"Masukkan Step Ke - {counter}")
                    stepinput = input()
                    if stepinput.lower() == "berhenti":
                        break
                    stepresep.append(stepinput)
                    counter += 1
                resep[ubahresep] = stepresep
                print("Resep Berhasil Diubah!!")
                return resep
            else:
                print("Nomor Resep Tidak Ada")
        except ValueError:
            print("Pilihlah Nomor Resep Dengan Benar!!")


def menghapus_resep():
    global resep
    if not resep:
        print("Tidak Ada Resep Yang Dapat Dihapus!!")
    else:
        for i,resepdata in enumerate(resep):
            print(f"{i+1}. {resepdata}")
        try:
            pilihanhapus = int(input("Pilih Resep Berapa Yang Ingin Dihapus"))
            if 1 <= pilihanhapus <= len(resep):
                hapusresep = list(resep.keys())[pilihanhapus - 1]
                del resep[hapusresep]
                print(f"Resep '{hapusresep}' Berhasil Dihapus!!")
                return resep
            else:
                print("Nomor Resep Tidak Ada")
        except ValueError:
            print("Pilihlah Nomor Resep Dengan Benarr")


def keluar_menuadmin():
    global pilihanadmin
    pilihanadmin = 0
    return pilihanadmin


# ---------------------------------------=[ HALAMAN PENGGUNA ]=---------------------------------------


def menu_pengguna():
    while True:
        pilihanregister = input("""
============ Panel Login / Register ============
Silahkan Memilih Login / Register Akun Pengguna
(login/register/keluar) : """)
        if pilihanregister.lower() == "login":
            return pilihanregister
        elif pilihanregister.lower() == "register":
            return pilihanregister
        elif pilihanregister.lower() == "keluar":
            return pilihanregister
        else:
            print("Input Salah!! Tolong Pilih Diantara login/register/keluar!!")


def register_pengguna():
    global registered, pengguna, penggunapw
    if registered >= 1: 
        print("Kamu Udh Register!!")
    if registered == 0:
        pengguna = input("Buatlah Username : ")
        penggunapw = input("Buatlah Password : ")
        registered += 2
        print("Register Berhasil!!") 
        return registered

        

def login_pengguna(pengguna, penggunapw):
    global registered
    print(pengguna,penggunapw)
    if registered >= 2:
        loginnama = input("Masukkan Username : ")
        loginpw = input("Masukkan Password : ")
        if pengguna == loginnama and penggunapw == loginpw:
            login = 2
            print("Login Berhasil!!")
            return login
        else:
            print("Username dan Passowrd Salah")
    elif registered == 0:
        print("Kamu Belum Register!!")


# ---------------------------------------=[ PANEL PENGGUNA ]=---------------------------------------


def panel_pengguna():
    global pilihlogin
    try:
        pilihlogin = int(input(f"""
=============== PANEL PENGGUNA ===============
{pengguna} Pilihah Apa Yang Ingin Anda Lakukan
1. Tampilkan Resep 
2. Keluar
==============================================                                                                                                                                                               
pilihan : """))
        if pilihlogin > 2:
            print("Salah Input!! Input Anda Tidak Ada Di Pilihan Menu!!")
        elif 0 > pilihlogin < 3:
            return pilihlogin
    except ValueError:
            print("Salah Input!! Tolong Masukkan Angka 1-2 Sebagai Pilihan")


# ---------------------------------------=[ SISTEM OPERASIONAL ]=---------------------------------------


while True:
    menu_login()
    while True:
        if pilihanadmin == 1:
            menu_adminlogin()
        elif pilihanadmin == 2:
            while True:
                pilihanresep = menu_admin()
                if pilihanresep == 1:
                    tambah_resep()
                elif pilihanresep == 2:
                    tampilkan_resep()
                elif pilihanresep == 3:
                    mengubah_resep()
                elif pilihanresep == 4:
                    menghapus_resep()
                elif pilihanresep == 5:
                    keluar_menuadmin()
                    if pilihanadmin == 0:
                        break
        elif pilihanpengguna == 1:
            while True:
                pilihanregister = menu_pengguna()
                pilihanpengguna = 0
                if pilihanregister == "login":
                    login_pengguna(pengguna, penggunapw)
                    while True:
                        panel_pengguna()
                        if pilihlogin == 1:
                            tampilkan_resep()
                        if pilihlogin == 2:
                            break

                if pilihanregister == "register":
                    register_pengguna()
                if pilihanregister == "keluar":
                    break


        else:
            pilihanadmin = 0
            break