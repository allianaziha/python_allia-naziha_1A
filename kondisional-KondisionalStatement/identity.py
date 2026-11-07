# is dan is not digunakan untuk membandingkan identitas dari dua objek, bukan nilai dari objek tersebut.

x = [1, 2, 3, 4, 5]
y = [1, 2, 3, 4, 5]
z = x 

print (x is y)   # False, karena x dan y adalah dua objek yang berbeda meskipun memiliki nilai yang sama
print (x is z)   # True, karena z adalah referensi ke objek yang sama dengan x

print (x is not y)   # True, karena x dan y adalah dua objek yang berbeda meskipun memiliki nilai yang sama
print (x is not z)   # False, karena z adalah referensi ke objek yang sama dengan x
