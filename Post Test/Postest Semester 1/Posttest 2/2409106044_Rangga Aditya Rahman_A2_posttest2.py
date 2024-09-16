nama = input("Masukkan Nama Lengkap :")
nim = input("Masukkan NIM :")
hargaberas = int(input("Harga Beras :"))

diskon = (0.11, 0.14, 0.17)

diskonMR = hargaberas * diskon[0]
diskonSN = hargaberas * diskon[1]
diskonMS = hargaberas * diskon[2]

hargaMR = hargaberas - diskonMR
hargaSN = hargaberas - diskonSN
hargaMS = hargaberas - diskonMS

print(f"{nama} Dengan NIM {nim} Ingin Membeli Beras Seharga {hargaberas}")
print(f"Jika dia membeli beras Mawar ia harus membayar {hargaMR} Setelah mendapat diskon 11%")
print(f"Jika dia membeli beras Sania ia harus membayar {hargaSN} Setelah mendapat diskon 14%")
print(f"Jika dia membeli beras Maknyus ia harus membayar {hargaMS} Setelah mendapat diskon 17%")