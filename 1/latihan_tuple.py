# buah = ("apel", "ceri", "durian", "mangga")

# (a, b, c, d) = buah

# print(a)   # apel
# print(b)   # ceri
# print(c)   # durian
# print(d)   # mangga

# Nama : Allia Naziha
# NIM : 2603338
# kelas : 1A

import math

x1 = int(input("Masukan x1: "))
y1 = int(input("Masukan y1: "))
titik_A = (x1, y1)

x2 = int(input("Masukan x2: "))
y2 = int(input("Masukan y2: "))
titik_B = (x2, y2)

(x1, y1) = titik_A
(x2, y2) = titik_B

d = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print(f"titik A: {titik_A}")
print(f"titik B: {titik_B}")
print(f"Jarak antara titik A dan B: {d}")