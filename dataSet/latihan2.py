# 2 daftar anggorta 
# 1. anggota kelas : andi,budi,citra,gita,doni,eka
# 2. anggota sirkel : citra,doni,eka

# bikin 2 kelompok
# kelompok 1 . anggota kelas yang ada didalem sirkel
# kelompok 2 . anggota kelas yang tidak ada didalam sirkel tambah Hani

anggota_kelas = {"andi", "budi", "citra", "gita", "doni", "eka"} 
anggota_sirkel = {"citra", "doni", "eka"}

kelompok1 = anggota_kelas.intersection(anggota_sirkel)
kelompok2 = anggota_kelas.difference(anggota_sirkel)
kelompok2.add("Hani")

print(kelompok1)
print(kelompok2)
