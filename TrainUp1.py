
biodata = {}

while True:
    print("\n  MENU BIODATA  ")
    print("1. Input biodata")
    print("2. Tampilkan biodata")
    print("3. Edit biodata")
    print("4. Hapus biodata")
    print("5. Keluar")

    pilihan = input("Pilih menu (1/2/3/4/5): ")

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
        if biodata == {}:
            print("Belum ada biodata yang bisa diedit.")
        else:
            print("\n EDIT BIODATA ")
            for judul, isi in biodata.items():
                print(f"{judul}: {isi}")

            data = input("Masukkan nama data yang ingin diubah: ")

            if data in biodata:
                biodata[data] = input(f"Masukkan {data} baru: ")
                print("Biodata berhasil diperbarui!")
            else:
                print("Data tidak ditemukan.")

    elif pilihan == "4":
        if biodata == {}:
            print("Belum ada biodata yang bisa dihapus.")
        else:
            konfirmasi = input("Yakin ingin menghapus biodata? (y/n): ")

            if konfirmasi.lower() == "y":
                biodata.clear()
                print("Biodata berhasil dihapus!")
            else:
                print("Penghapusan dibatalkan.")

    elif pilihan == "5":
        print("Terima kasih!")
        break

    else:
        print("Pilihan tidak valid.")
