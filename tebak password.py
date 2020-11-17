import random

jawaban = random.randint(1000000000,9999999999)
tebakan = 0
kesempatan = 50

print("DOKUMEN NEGARA")
print("SANGAT RAHASIA")
print("SECURITY SYSTEM")

while tebakan!=jawaban and kesempatan>0 :
    tebakan=int(input("Masukkan Password[10 digit]: "))
    if tebakan<jawaban and tebakan<=9999999999 and tebakan>=1000000000:
        print("Silahkan input password yang lebih tinggi lagi")
        kesempatan-=1
        print("Sisa kesempatan:",kesempatan)
        print()
    elif tebakan>jawaban and tebakan<=9999999999 and tebakan>=1000000000:
        print("Silahkan input password yang lebih rendah lagi")
        kesempatan-=1
        print("Sisa kesempatan:",kesempatan)
        print()
    elif tebakan==jawaban:
        print("Password anda benar")
        kesempatan-=1
        print("Sisa kesempatan:",kesempatan)
        print()
        while 1!=0:
            print("Congratz")
    else:
        print("Input yang benar woi")
if kesempatan==0:
    print("Anda kehabisan kesempatan. Password yang benar adalah",jawaban)
    print("Dasar Hacker NOOB")

