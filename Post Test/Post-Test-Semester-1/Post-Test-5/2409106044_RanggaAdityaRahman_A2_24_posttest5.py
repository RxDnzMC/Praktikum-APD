# PASSWORD ADMIN : admin123

admin = ""
adminpw = "admin123"
pilihanadmin = 0
pilihanpengguna = 0
registered = 0
pengguna = ""
penggunapw = ""
login = 0
resep = ""

# UNTUk MEMILIH MENJADI SEBAGAI USER ATAU ADMIN 

while True:
    while True:
        pilihan1 = input("""
=========== Admin / Pengguna ===========
Selamat Datang Di Daftar Menu Resep Makanan
Kamu Disini Sebagai Apa
(admin/pengguna/keluar) : """)
        if pilihan1.lower() == "admin":
            pilihanadmin = 1
            break
        if pilihan1.lower() == "pengguna":
            pilihanpengguna = 1
            break
        if pilihan1.lower() == "keluar":
            exit("Terimakasih Sudah Mencoba Program Yang Saya Buat")
        else:
            print("Input Yang Anda Masukkan Salah!! Coba Ulangi!!")

# KETIKA MEMILIH OPSI ADMIN

    if pilihanadmin == 1:
        while True:
            adminlogin = input("Masukkan Password : ")
            if adminlogin == adminpw:
                pilihanadmin += 1
                break
            else:
                print("Password Anda Salah!!")

        resep = []
        stepresep = []

        if pilihanadmin == 2:
            while True:
                pilihanresep = input("""
====== PANEL ADMIN ======
1. Tambah Resep
2. Tampilkan Resep
3. Ubah Isi Resep
4. Hapus Resep
5. Keluar
=======================                                                                                                                                                                    
pilihan : """)
                
# === PROGRAM MENAMBAHKAN RESEP ===
                if pilihanresep == "1":
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
                    resep.append([judul,stepresep])
                    # print(resep) Di hidupkan untuk melihat nested list

# === PROGRAM MENAMPILKAN RESEP ===
                elif pilihanresep == "2":
                    if not resep:
                        print("Tidak Ada Resep!!")
                    else:
                        for i,resepdata in enumerate(resep):
                            print(f"\nResep Ke {i+1}: {resepdata[0]}")
                            for j,stepresep in enumerate(resepdata[1], start=1):
                                print(f"Step {j}: {stepresep}")
                    print()

# === PROGRAM MENGUBAH ISI RESEP ===
                elif pilihanresep == "3":
                    if not resep:
                        print("Tidak Ada Resep Yang Dapat Diubah!!")
                    else:
                        for i,resepdata in enumerate(resep):
                            print(f"{i+1}. {resepdata[0]}")
                        try:
                            pilihanubah = int(input("Pilih Nomor Resep Yang Ingin Diubah : "))
                            if 1 <= pilihanubah <= len(resep):
                                ubahresep = resep[pilihanubah - 1]
                                print(f"Mengubah resep: {ubahresep[0]}")
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
                                resep[pilihanubah - 1] = [ubahresep[0], stepresep]
                                print("Resep Berhasil Diubah!!")
                            else:
                                print("Nomor Resep Tidak Ada")
                        except ValueError:
                            print("Pilihlah Nomor Resep Dengan Benar!!")

# === PROGRAM MENGHAPUS RESEP ===
                elif pilihanresep == "4":
                    if not resep:
                        print("Tidak Ada Resep Yang Dapat Dihapus!!")
                    else:
                        for i,resepdata in enumerate(resep):
                            print(f"{i+1}. {resepdata[0]}")
                        try:
                            pilihanhapus = int(input("Pilih Resep Berapa Yang Ingin Dihapus"))
                            if 1 <= pilihanhapus <= len(resep):
                                del resep[pilihanhapus - 1]
                            else:
                                print("Nomor Resep Tidak Ada")
                        except ValueError:
                            print("Pilihlah Nomor Resep Dengan Benarr")

# === PROGRAM KELUAR DARI TAB ADMIN ===
                elif pilihanresep == "5":
                    pilihanadmin = 0
                    break

# === PROGRAM LANJUTAN UNTUK LOGOUT DARI ADMIN ===
        if pilihanadmin == 0:
            continue

# KETIKA MEMILIH OPSI PENGGUNA :
    if pilihanpengguna == 1:
        while True:
            
# === PROGRAM UNTUK MEMILIH USER PENGGUNA UNTUK LOGIN/REGISTER/KELUAR ===
            pilihanregister = input("""
============ Panel Login / Register ============
Silahkan Memilih Login / Register Akun Pengguna
(login/register/keluar) : """)
            if pilihanregister.lower() == "login": # Ketika Memilih Login
                while True:
                    if login == 0: # Sesi Pengecekan Register Dan Login Pengguna
                        if registered == 0:
                            print("Kamu Belum Register!! Silahkan Register Terlebih Dahulu")
                            break
                        elif registered >= 1:
                            loginnama = input("Masukkan Username : ")
                            loginpw = input("Masukkan Password : ")
                            if pengguna == loginnama and penggunapw == loginpw:
                                print("Login Berhasil!!")
                                login = 2
                            else:
                                print("Username dan Passowrd Salah")
                    if login == 2: # Sesi Ketika Sudah Login Akan Masuk Ke Dalam TAB PENGGUNA
                        while True:
                            try:
                             pilihlogin = int(input(f"""
=============== PANEL PENGGUNA ===============
{loginnama} Pilihah Apa Yang Ingin Anda Lakukan
1. Tampilkan Resep 
2. Keluar
==============================================                                                                                                                                                               
pilihan : """))
                             if pilihlogin == 1: # Program Menampilkan Resep Yang Sudah Dibuat Oleh Admin
                                if not resep:
                                       print("Tidak Ada Resep!!")
                                else:
                                    for i,resepdata in enumerate(resep):
                                        print(f"\nResep Ke {i+1}: {resepdata[0]}")
                                        for j,stepresep in enumerate(resepdata[1], start=1):
                                            print(f"Step {j}: {stepresep}")
                                    print()
                        
                             if pilihlogin == 2: # Program Untuk Keluar Dari TAB PENGGUNA
                                login = 1
                                break
                            except ValueError:
                              print("Salah Input!!")
                    if login == 1: # Program Lanjutan Supaya Bisa Logout
                        login = 0
                        break


                    
            elif pilihanregister.lower() == "register": # Ketika Memilih Register
                while True:
                    if registered >= 1: # Program Register dan Pengecekan Apakah Sudah Register
                        print("Kamu Udh Register!!")
                        break
                    pengguna = input("Buatlah Username : ")
                    penggunapw = input("Buatlah Password : ")
                    registered += 1
                    if registered == 1:
                        print("Register Berhasil!!") 
                        break
    
            elif pilihanregister.lower() == "keluar": # Untuk Keluar Dari Program PENGGUNA/LogOut
                break


