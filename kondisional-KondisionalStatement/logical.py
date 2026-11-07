# x = 2 and x < 5       and
# x > 2 or x < 4        or
# not(x < 0 and x > 5)  not

# and akan bernilai true jika kedua pernyataan benar, dan false jika salah satu pernyataan salah,
# or akan bernilai true jika salah satu pernyataan benar, dan false jika kedua pernyataan salah,
# not akan membalikkan nilai dari pernyataan, jika pernyataan true maka not akan menjadi false, dan sebaliknya.


# urutan nya () > not > and > or

x = 2
y = 2 
print(x > 0 and  y > 0)

x = 2
y = 0
print(x > 0 or  y > 0)

x = 2
y = 2
print(not(x > 0 and x < 5))