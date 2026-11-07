#nama : allia naziha
#nim : 2603338
#kelas : 1A

jk = input("Jenis kelamin (L/P): ").upper()
umur = int(input("Umur: "))
tinggi = float(input("Tinggi badan (cm): "))
iq = int(input("IQ: "))

if umur >= 18 and umur <= 25 and iq >= 130:
    if jk == "P" and tinggi >= 170:
        print("Bisa menjadi model catwalk")
    elif jk == "L" and tinggi >= 175:
        print("Bisa menjadi model catwalk")
    else:
        print("Tidak bisa, tinggi badan belum memenuhi")
else:
    print("Tidak bisa, umur atau IQ belum memenuhi")