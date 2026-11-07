
biodata = {}

while True:
    print("\n" + "=" * 35)
    print("       APLIKASI BIODATA")
    print("=" * 35)
    print("[1] Input Biodata")
    print("[2] Tampilkan Biodata")
    print("[3] Edit Biodata")
    print("[4] Hapus Biodata")
    print("[5] Keluar")
    print("-" * 35)

    pilihan = input("Masukkan pilihan menu: ")

    if pilihan == "1":
        biodata = {
            "Nama Lengkap": input("Nama Lengkap : "),
            "NIM": input("NIM : "),
            "Kelas": input("Kelas : "),
            "Program Studi": input("Program Studi : "),
            "Umur": input("Umur : "),
            "No Telepon": input("No Telepon : "),
        }
        print("\nBiodata berhasil disimpan!")

    elif pilihan == "2":
        if biodata == {}:
            print("\nBelum ada biodata. Input dulu ya.")
        else:
            print("\n" + "=" * 35)
            print("          DATA BIODATA")
            print("=" * 35)
            for judul, isi in biodata.items():
                print(f"{judul:<16}: {isi}")
            print("=" * 35)

    elif pilihan == "3":
        if biodata == {}:
            print("\nBelum ada biodata yang bisa diedit.")
        else:
            print("\n--- EDIT BIODATA ---")
            for judul, isi in biodata.items():
                print(f"{judul}: {isi}")

            data = input("\nMasukkan nama data yang ingin diubah: ")

            if data in biodata:
                biodata[data] = input(f"Masukkan {data} baru: ")
                print("Biodata berhasil diperbarui!")
            else:
                print("Data tidak ditemukan.")

    elif pilihan == "4":
        if biodata == {}:
            print("\nBelum ada biodata yang bisa dihapus.")
        else:
            konfirmasi = input("Yakin ingin menghapus biodata? (y/n): ")

            if konfirmasi.lower() == "y":
                biodata.clear()
                print("Biodata berhasil dihapus!")
            else:
                print("Penghapusan dibatalkan.")

    elif pilihan == "5":
        print("\nTerima kasih telah menggunakan Aplikasi Biodata!")
        break

    else:
        print("\nPilihan tidak valid. Silakan coba lagi.")

