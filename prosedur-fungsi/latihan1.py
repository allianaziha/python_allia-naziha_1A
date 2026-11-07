# nama : Allia Naziha
# NIM : 2603338
# kelas : 1A


def faktorial(n):
    if n <= 1:
        return 1
    else:
        return n * faktorial(n-1)

n = int(input("Masukkan angka : "))

print(f"{n}! = {faktorial(n)}")











# def fibonacci(n):
#     if n <= 1:
#         return n
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)

# n = int(input("masukan jumlah deret angka : "))

# for i in range(n):
#     print(fibonacci(i), end=" ")


