print("Hello, World!")      # bisa pakai kutip dua
print('Hello, World!')      # atau kutip satu
print("Hello" * 3)          # HelloHelloHello
print(1 + 1)                # 2

# ini komentar satu baris
print("Ini akan dieksekusi")

"""
ini komentar
lebih dari satu baris
"""

nama = "Budi"
umur = 20
print(nama)
print(umur)

# multi-words variable style
nama_lengkap = "Budi"     # snake_case
namaLengkap = "Budi"      # camelCase
NamaLengkap = "Budi"      # PascalCase

a, b, c = "apel", "belimbing", "ceri"
x = y = z = "Buah"

a = "Hello"
print(type(a))   # <class 'str'>

# casting (ubah tipe data)
a = int(3)
b = float(3)
c = str(3)

nama = input("Masukan nama Anda: ")
print(f"Selamat datang, {nama}")

umur = int(input("Masukan umur Anda: "))
print(umur + 1)   # baru bisa dihitung

print(abs(-10))          # 10
print(max(1, 3, 5))      # 5
print(min(1, 3, 5))      # 1
print(pow(2, 3))         # 8
print(round(10.7374, 2)) # 10.74

a = "Halo, selamat pagi"
print(len(a))        # cek panjang teks -> 18

# slicing (ambil sebagian teks)
print(a[1:4])   # "alo"  -> kayak motong roti dari irisan ke-1 sampai ke-4
print(a[:5])    # dari awal sampai index 5
print(a[10:])   # dari index 10 sampai akhir

# modifikasi
print(a.upper())     # HALO, SELAMAT PAGI
print(a.lower())     # halo, selamat pagi
print(a.strip())     # hapus spasi kosong di depan/belakang
print(a.replace("Halo", "Hai"))
print(a.split(","))  # pecah jadi list

# gabung teks (concatenation)
print("Bahasa" + " " + "Python")

# format teks
umur = 20
print(f"Umur saya {umur} tahun")
print("Umur saya {}".format(umur))

nama = input("Masukan nama Anda: ")
tahun_lahir = int(input("Masukan tahun lahir Anda: "))
umur = 2026 - tahun_lahir
print(f"Selamat datang, {nama}! Umur Anda sekarang adalah {umur}")

# Data resep untuk 4 gelas
buah = 600      # gram
susu = 400      # ml
gula = 4        # sendok makan

gelas_dibutuhkan = 15

# Cari kebutuhan per 1 gelas, lalu kali jumlah gelas yang diinginkan
buah_total = (buah / 4) * gelas_dibutuhkan
susu_total = (susu / 4) * gelas_dibutuhkan
gula_total = (gula / 4) * gelas_dibutuhkan

print(f"Untuk membuat {gelas_dibutuhkan} gelas jus, dibutuhkan:")
print(f"Buah: {buah_total} gram")
print(f"Susu: {susu_total} ml")
print(f"Gula: {gula_total} sendok makan")

jarak_km = 180
konsumsi_per_liter = 12   # km per liter
harga_bensin = 13000       # rupiah per liter

# Hitung liter bensin yang dibutuhkan
liter_dibutuhkan = jarak_km / konsumsi_per_liter

# Hitung total biaya
total_biaya = liter_dibutuhkan * harga_bensin

print(f"Jarak tempuh: {jarak_km} km")
print(f"Liter bensin yang dibutuhkan: {liter_dibutuhkan} liter")
print(f"Total biaya bensin: Rp{total_biaya}")