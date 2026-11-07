kalimat = input("Masukkan sebuah kalimat : ")

print("\n  MENU OPERASI  ")
print("1. Hitung jumlah kata")
print("2. Tampilkan huruf kapital semua")
print("3. Balik urutan kata")
pilihan = input("Pilih operasi (1/2/3): ")

if pilihan == "1":
    jumlah = len(kalimat.split())
    print("Jumlah kata:", jumlah)

elif pilihan == "2":
    print("Hasil:", kalimat.upper())

elif pilihan == "3":
    kata = kalimat.split()
    kata.reverse()
    print("Hasil:", " ".join(kata))

else:
    print("Pilihan tidak valid.")