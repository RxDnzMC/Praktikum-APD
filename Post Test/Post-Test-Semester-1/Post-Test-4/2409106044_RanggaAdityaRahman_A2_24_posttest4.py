# Untuk Mengulang Program Secara Terus Menerus

while True:
    nama = input("Masukkan Nama Anda : ")
    nim = str(input("Masukkan NIM : "))
    password = nim[-3:]
    percobaanpassword = 0
    percobaanusername = 0
# Untuk Mengecek Apakah username Huruf Kecil Semua
    while True:
        percobaanusername += 1
        username = input(f"""=================================================
Jika Anda Salah Memasukkan username Sebanyak 3 Kali Percobaan
Maka Program Akan Dihentikan
Percobaan Ke-{percobaanusername}
Masukkan username Anda (Harus Huruf Kecil Semua): """)
        if username.islower():
            print("=================================================")
            break
        if percobaanusername == 3:
            exit("Anda Salah Memasukkan username Sebanyak 3 Kali Percobaan Maka Program Di Hentikan")

# Untuk Membuat Password Dari 3 Angka Belakang NIM

    if int(password[-3]) == 0:
        password = str(nim[-2:])

# Untuk Mengecek Apakah Password Benar, Dengan Pengulangan Sebanyak 3 Kali

    while True:
        percobaanpassword += 1
        if percobaanpassword == 4:
            exit("Anda Salah Memasukkan Password Sebanyak 3 Kali Percobaan Maka Program Di Hentikan")
        passwordnim = input(f"""
=============================================================
Masukkan Password 3 Digit Terakhir Di NIM anda
Jika Ada Angka 0 Di Digit Pertama Maka
Masukkan 2 Angka Terakhir Sebagai Password
Jika Anda Salah Memasukkan Password Sebanyak 3 kali Percobaan
Maka Program Akan Berhenti
Percobaan Ke-{percobaanpassword}
Masukkan Password : """)
        if password == passwordnim:
            break

# Untuk Menginput Data Yang Diperlukan    

    pinjaman = int(input("Masukkan Jumlah Pinjaman : "))
    lamacicilan = int(input("Masukkan Waktu Cicilan Dalam Bentuk Tahun (Maksimal 3 Tahun) : "))

# Untuk Menghitung Total Cicilan Perbulan

    if lamacicilan == 1 :
        bunga = 0.07
        bulan = 12
        bungapersen = "7%"
    elif lamacicilan == 2 :
        bunga = 0.13
        bulan = 24
        bungapersen = "13%"
    elif lamacicilan == 3 :
        bunga = 0.19
        bulan = 36
        bungapersen = "19%"
    else : 
        exit("Maksimal lama cicilan adalah 3 Tahun!!")
        
    bungaperbulan = (bunga / 12) * pinjaman
    totalcicilanperbulan = int((pinjaman + bungaperbulan) / bulan)

    print(f"""
===============================================================
{nama} Dengan NIM {nim} Dan Username {username}
Ingin Meminjam Uang Sebesar Rp.{pinjaman} 
Secara Kredit Dengan Waktu {lamacicilan} Tahun Atau {bulan} Bulan 
Dengan Bunga Sebesar {bungapersen}
Jadi Total Cicilan Perbulan Adalah Rp.{totalcicilanperbulan}
===============================================================
        """)

# Untuk Mengulangi Program 

    ulang = input("ingin mengulang program ini lagi? [ketik 'no' untuk berhenti, input selain 'no' akan melanjutkan program] : ")
    if ulang.lower() == 'no':
        exit("Anda Memilih Program Untuk Berhenti")