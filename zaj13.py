import random
ilosc_parzystych=0
for i in range(10):
    wylosowana=random.randint(1,20)
    print(wylosowana)
    if wylosowana % 2==0:
        ilosc_parzystych+=1
print("parzyste liczby pojawiły się", ilosc_parzystych, "razy")
