# Nama : Allia Naziha
# NIM : 2603338
# kelas : 1A


jumlah_peserta = int(input("Masukkan jumlah peserta seminar: "))


# a. Perhitungan Biaya Konsumsi

harga_konsumsi = 35000
cadangan_konsumsi = jumlah_peserta * 10 / 100     # cadangan 10% dari peserta
jumlah_konsumsi = jumlah_peserta + cadangan_konsumsi
total_biaya_konsumsi = jumlah_konsumsi * harga_konsumsi

print(f"Jumlah konsumsi yang disediakan (termasuk cadangan): {int(jumlah_konsumsi)} paket")
print(f"Total biaya konsumsi: Rp{int(total_biaya_konsumsi)}")


# b. Perhitungan Kebutuhan Cetak Sertifikat

harga_per_rim = 65000
lembar_per_rim = 500

cadangan_sertifikat = jumlah_peserta * 5 / 100    # cadangan 5% dari peserta
jumlah_sertifikat = jumlah_peserta + cadangan_sertifikat
jumlah_lembar_kertas = jumlah_sertifikat * 1       # 1 lembar per sertifikat
jumlah_rim = jumlah_lembar_kertas / lembar_per_rim
total_biaya_kertas = jumlah_rim * harga_per_rim

print(f"Jumlah sertifikat yang perlu dicetak: {int(jumlah_sertifikat)}")
print(f"Jumlah lembar kertas yang dibutuhkan: {int(jumlah_lembar_kertas)}")
print(f"Perkiraan jumlah rim kertas: {round(jumlah_rim, 2)} rim")
print(f"Total biaya pembelian kertas: Rp{int(total_biaya_kertas)}")


# c. Perhitungan Biaya Pendaftaran Peserta

biaya_sewa_tempat = int(input("Masukkan biaya sewa tempat (Rp): "))
biaya_dokumentasi = int(input("Masukkan biaya dokumentasi (Rp): "))

total_biaya_acara = total_biaya_konsumsi + total_biaya_kertas + biaya_sewa_tempat + biaya_dokumentasi
dana_cadangan = total_biaya_acara * 10 / 100
total_dana_dikumpulkan = total_biaya_acara + dana_cadangan
biaya_pendaftaran_per_peserta = total_dana_dikumpulkan / jumlah_peserta

print(f"Total biaya penyelenggaraan acara: Rp{int(total_biaya_acara)}")
print(f"Dana cadangan (10%): Rp{int(dana_cadangan)}")
print(f"Total dana yang harus dikumpulkan: Rp{int(total_dana_dikumpulkan)}")
print(f"Biaya pendaftaran per peserta: Rp{int(biaya_pendaftaran_per_peserta)}")