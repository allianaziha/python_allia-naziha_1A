#If
x = 5
if (x > 1):
    print("Nilai x lebi besar daripada 1")

x = 0
if (x > 1):
    print("Nilai x lebi besar daripada 1")

x = 3
if (x > 0 and x < 5):
    print("Nilai x lebih besar dari 0 dan lebih kecil dari 5 ")


#If Else
nilai = 80
if (nilai > 75):
    print("selamat anda lulus")
else: 
    print("ayo belajar lebih giat lagi")

nilai = 80
absen = 70
if (nilai > 75 and absen > 80):
    print("selamat anda lulus")
else: 
    print("ayo belajar lebih giat lagi")


#if Elif Else
nilai = 75
if (nilai > 90):
    print("A")
elif (nilai > 80):
    print("B")
elif (nilai > 70):
    print("C")
else:
    print("ngejain ngga?")


#pernyataan berkondisi ShortHand 
a = 2
b = 1  
if a > b: print("nilai a lebih besar dair b")

a = 2
b = 3
print ("nilai a lebih besar") if a > b else print("nilai b lebih besar")

a = 5
b = 3
print("a") if a > b else print("a == b") if a == b else print("b")

a = 3
b = 3
print("a") if a > b else print("a == b") if a == b else print("b")


# pernyataan berkondisi id dan operators
a = 2
b = 3
c = 5
if (a > b or a > c):
    print("aku")
else: 
    print("dia")

a = 0
b = 2
if not(a > b):
    print("nilai a lebih kecil")
else: 
    print("nilai b lebih kecil")


#pernyataan berkondisi nested if 
a = 10
if (a > 0):
    print("nilai a lebih besar dari 0")
    if (a > 5):
        print("nilai a juga lebih besar dari 5")
    else:
        print("nilai a lebih kecil dari 5")
else:
    print("gagal")


# pernyataan kondisi Pass Statement
a = 5
if(a > 5):
    print   
