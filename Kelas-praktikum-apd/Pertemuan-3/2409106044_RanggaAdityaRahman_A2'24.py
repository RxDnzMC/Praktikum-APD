# cuaca = input("cuaca saat ini [cerah/hujan] :")
# if cuaca == "cerah":
#     print("kamu pergi keluar ruma")
# elif cuaca == "hujan":
#     print("Hari ini mendung kamu tidak keluar rumah")
# else:
#     print("baca komik aja sana")

# Umur = int(input("Masukkan umur Anda : "))
# if Umur <= 10:
#     print("Umur Anda termasuk kategori anak-anak")
# elif Umur <= 18:
#     print("Umur Anda termasuk kategori remaja")
# elif Umur <=35:
#     print("Umur Anda termasuk kategori dewasa")
# elif Umur <=65:
#     print("Umur Anda termasuk kategori paruh baya")
# else:
#     print("Umur Anda termasuk kategori Tua")

# angka = int(input("Masukkan angka: "))
# result = "Genap" if angka % 2 == 0 else "Ganjil"
# print(angka, "adalah angka",result)

# print("""
# ==========================
#     PILIH METODE KALKULATOR
#       1. +
#       2. -
#       3. *
#       4. /
# ==========================
#       """)
# fitur = int(input("Pilih fitur : "))
# match fitur:
#     case 1:
#         a = int(input("masukkan angka 1 : "))
#         b = int(input("masukkan angka 2 : "))
#         c = a + b
#         print(f"hasil pertambahan dari n angka 1 dan 2 adalah : {c}")
#     case 2:
#         a = int(input("masukkan angka 1 : "))
#         b = int(input("masukkan angka 2 : "))
#         c = a - b
#         print(f"hasil pengurangan dari  angka 1 dan 2 adalah : {c}")
#     case 3:
#         a = int(input("masukkan angka 1 : "))
#         b = int(input("masukkan angka 2 : "))
#         c = a * b
#         print(f"hasil perkalian dari angka 1 dan 2 adalah : {c}")
#     case 4:
#         a = int(input("masukkan angka 1 : "))
#         b = int(input("masukkan angka 2 : "))
#         c = a / b
#         print(f"hasil pembagian dari  angka 1 dan 2 adalah : {c}")

# harga = int(input("Masukkan harga barang = "))
# jumlah = int(input("Masukkan jumlah barang = "))
# diskon = 0.20
# harga_total = harga * jumlah

# if harga_total > 100000 and jumlah >= 5:
#     diskon_barang = harga_total * diskon
#     harga_diskon = harga_total - diskon_barang
#     print(harga_diskon)
# else : 
#     print("Anda tidak mendapat diskon")

# jenis_kelamin = input("Masukkan jenis kelamin (L/P) :")
# kelamin = "Jenis Kelamin Anda laki-laki" if jenis_kelamin == "L" else "Jenis Kelamin Anda Perempuan" if jenis_kelamin == "P" else "Jenis Kelamin Tidak Diketahui"
# print(kelamin)

# ada mahasiswa inputan nilai jika lebih 80 maka A tapi ada A- (80-89) A+ (90-100)
# B lebih dari 70-79
# B- 70 - 74
# B+ 75 - 79
# Pake elif dan nested if

# nilai = int(input("Masukkan Nilai Anda :"))
# if nilai >= 80 and nilai <= 100 :
#     if nilai >= 90 and nilai <= 100:
#         nilaihuruf = "A+"
#     else:
#         nilaihuruf = "A-"
#     print(f"nilai kamu {nilai} dan kamu mendapatkan {nilaihuruf}")
# elif nilai >= 70 and nilai <= 79:
#     if nilai >= 75 and nilai <= 79:
#         nilaihuruf = "B+"
#     else:
#         nilaihuruf = "B-"
#     print(f"nilai kamu {nilai} dan kamu mendapatkan {nilaihuruf}")
# else :
#     print("nilai kamu tidak memenuhi syarat")
