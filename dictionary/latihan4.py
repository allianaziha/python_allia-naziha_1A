mahasiswa = {
"Andi": {"Nama": "Andi Sawargi", "Kelas": "XI RPL 1", "Kesukaan": ["Anggur", "Jeruk", "Buku"] },
"Budi": { "Nama": "Budi Setiawan", "Kelas": "XI RPL 2", "Kesukaan": ["Gaming", "Musik", "Film"] },
"Citra": { "Nama": "Citra Lestari", "Kelas": "XI RPL 1", "Kesukaan": ["Membaca", "Kucing", "Musik"] }
}

nama_panggilan = input("Nama Mahasiswa: ")
nomor_kesukaan = int(input("Nomor Kesukaan (1-3): "))

print("Nama:", mahasiswa[nama_panggilan]["Nama"])
print("Kelas:", mahasiswa[nama_panggilan]["Kelas"])
print("Kesukaan:", mahasiswa[nama_panggilan]["Kesukaan"][nomor_kesukaan - 1])