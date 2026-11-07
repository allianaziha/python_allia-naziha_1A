# Nama : Allia Naziha
# NIM : 2603338
# kelas : 1A

hari_1 = 120 
hari_2 = 150 
hari_3 = 155 # 135 => 140 => 155
hari_4 = 180
hari_5 = 160
hari_6 = 175

penjualan = [120, 150, 135, 180, 160, 175]

harga_satuan = 75000

print("Data awal:", penjualan)

penjualan[2] = 140
penjualan.insert(2, 155)
penjualan.append(175)
penjualan.pop(1)

total_produk_terjual = sum(penjualan)
pendapatan_kotor = total_produk_terjual * harga_satuan
biaya_platform = pendapatan_kotor * 0.05
pendapatan_bersih = pendapatan_kotor - biaya_platform
penjualan_tertinggi = max(penjualan)
penjualan_terendah = min(penjualan)
selisih = penjualan_tertinggi - penjualan_terendah

print(f"Total produk yang terjual: {total_produk_terjual} unit")
print(f"Pendapatan kotor: Rp{pendapatan_kotor:,.0f}")
print(f"Biaya platform: Rp{biaya_platform:,.0f}")
print(f"Pendapatan bersih: Rp{pendapatan_bersih:,.0f}")
print(f"Penjualan tertinggi: {penjualan_tertinggi} unit")
print(f"Penjualan terendah: {penjualan_terendah} unit")
print(f"Selisih penjualan: {selisih} unit")