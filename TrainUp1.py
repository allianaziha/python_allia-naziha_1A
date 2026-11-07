biodata = {}  

while True:
    print("\n  MENU BIODATA  ")
    print("1. Input biodata")
    print("2. Tampilkan biodata")
    print("3. Keluar")
    pilihan = input("Pilih menu (1/2/3): ")

    if pilihan == "1": 
        biodata = {
            "Nama Lengkap": input("Nama Lengkap : "),
            "NIM": input("NIM : "),
            "Kelas": input("Kelas : "),
            "Program Studi": input("Program Studi : "),
            "Umur": input("Umur : "),
            "No Telepon": input("No Telepon : "),
        }
        print("Biodata berhasil disimpan!")

    elif pilihan == "2":
        if biodata == {}:
            print("Belum ada biodata. Input dulu ya.")
        else:
            print("\n BIODATA ")
            for judul, isi in biodata.items():
                print(f"{judul}: {isi}")

    elif pilihan == "3":
        print("Terima kasih!")
        break

    else:
        print("Pilihan tidak valid.")