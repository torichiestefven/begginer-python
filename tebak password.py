import random

jawaban = random.randint(1000000000,9999999999)
tebakan = 0
kesempatan = 20

print("SECURITY SYSTEM")

while tebakan!=jawaban and kesempatan>0 :
    tebakan=int(input("Please enter the Password[10 digit]: "))
    if tebakan<jawaban and tebakan<=9999999999 and tebakan>=1000000000:
        print("Please input higher password ammount")
        kesempatan-=1
        print("Sisa kesempatan:",kesempatan)
        print()
    elif tebakan>jawaban and tebakan<=9999999999 and tebakan>=1000000000:
        print("Please input lower password ammount")
        kesempatan-=1
        print("Sisa kesempatan:",kesempatan)
        print()
    elif tebakan==jawaban:
        print("Your password is correct ! ")
        kesempatan-=1
        print("Sisa kesempatan:",kesempatan)
        print()
        while 1!=0:
            print("Congratz, you win the game")
    else:
        print("Harap masukkan format yang benar")
if kesempatan==0:
    print("You have no chance, the correct password is ",jawaban)
    

