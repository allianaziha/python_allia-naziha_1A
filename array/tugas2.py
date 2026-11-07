import numpy as np

nilai = np.array([85, 70, 92, 65, 78, 88, 95, 60, 73, 81,
                  90, 67, 84, 77, 99, 72, 68, 86, 91, 75,
                  80, 62, 89, 94, 71, 83, 76, 87, 69, 93])

urut = np.sort(nilai)[::-1]

print("Nilai :", nilai)
print("Nilai terurut :", urut)
print("5 nilai terbesar :", urut[:5])