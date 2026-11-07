buah = ["apel", "Belimbing", "ceri"]
angka = (1, 2)

for i in buah:
    for j in angka:
        print(i)
        print(j)


tinggi = 5

for i in range(1, tinggi + 1):
  for j in range(i):
    print('*', end='')
  print()