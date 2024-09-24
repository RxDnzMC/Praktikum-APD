nama = input("Masukkan Nama : ")
nim = int(input("Masukkan NIM : "))
pinjaman = int(input("Masukkan Jumlah Pinjaman : "))
lamacicilan = int(input("Masukkan Waktu Cicilan Dalam Bentuk Tahun (Maksimal 3 Tahun) : "))

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
{nama} Dengan NIM {nim}
Ingin Meminjam Uang Sebesar RP.{pinjaman} 
Secara Kredit Dengan Waktu {lamacicilan} Tahun Atau {bulan} Bulan 
Dengan Bunga Sebesar {bungapersen}
Jadi Total Cicilan Perbulan Adalah {totalcicilanperbulan}
===============================================================
      """)