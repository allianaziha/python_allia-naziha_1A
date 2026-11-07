#nama : allia naziha
#nim : 2603338
#kelas : 1A

menu = ["Nasi Goreng", "Mie Goreng", "Ayam Geprek"]

pesanan = input("Masukkan nama makanan yang dicari: ")

if pesanan in menu:
    print("Menu tersedia")
else:
    print("Menu tidak tersedia")