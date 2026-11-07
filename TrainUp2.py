
kalimat = input("Masukkan sebuah kalimat : ")

while True:
    print("\n  MENU OPERASI  ")
    print("1. Hitung jumlah kata")
    print("2. Tampilkan huruf kapital semua")
    print("3. Balik urutan kata")
    print("4. Hitung jumlah karakter")
    print("5. Tampilkan huruf kecil semua")
    print("6. Hitung jumlah huruf vokal")
    print("7. Hitung jumlah huruf konsonan")
    print("8. Tampilkan kalimat tanpa spasi")
    print("9. Ganti kata dalam kalimat")
    print("10. Keluar")

    pilihan = input("Pilih operasi (1-10): ")

    if pilihan == "1":
        jumlah = len(kalimat.split())
        print("Jumlah kata:", jumlah)

    elif pilihan == "2":
        print("Hasil:", kalimat.upper())

    elif pilihan == "3":
        kata = kalimat.split()
        kata.reverse()
        print("Hasil:", " ".join(kata))

    elif pilihan == "4":
        print("Jumlah karakter:", len(kalimat))

    elif pilihan == "5":
        print("Hasil:", kalimat.lower())

    elif pilihan == "6":
        vokal = "aiueoAIUEO"
        jumlah = 0

        for huruf in kalimat:
            if huruf in vokal:
                jumlah += 1

        print("Jumlah huruf vokal:", jumlah)

    elif pilihan == "7":
        vokal = "aiueoAIUEO"
        jumlah = 0

        for huruf in kalimat:
            if huruf.isalpha() and huruf not in vokal:
                jumlah += 1

        print("Jumlah huruf konsonan:", jumlah)

    elif pilihan == "8":
        print("Hasil:", kalimat.replace(" ", ""))

    elif pilihan == "9":
        kata_lama = input("Kata yang ingin diganti: ")
        kata_baru = input("Masukkan kata pengganti: ")

        kalimat = kalimat.replace(kata_lama, kata_baru)
        print("Hasil:", kalimat)

    elif pilihan == "10":
        print("Program selesai. Terima kasih!")
        break

    else:
        print("Pilihan tidak valid.")