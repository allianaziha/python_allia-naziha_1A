#nama : allia naziha
#nim : 2603338
#kelas : 1A

nilai = int(input("Masukan nilai :"))

if nilai > 100 or nilai < 0:
    print("Nilai tidak valid")
else:
    if nilai > 90 and nilai <= 100:
        print("Grade: A")
        print("ket : Sangat Baik")
    elif nilai > 85 and nilai <= 90:
        print("Grade: B+")
        print("ket : Sangat Baik")
    elif nilai > 80 and nilai <= 85:
        print("Grade: B")
        print("ket : Baik")
    elif nilai > 70 and nilai <= 80:
        print("Grade: C")
        print("ket : Baik")
    elif nilai > 60 and nilai <= 70:
        print("Grade: D")
        print("ket : Perlu Perbaikan")
    else:
        print("Grade: E")
        print("ket : Perlu Perbaikan")

    