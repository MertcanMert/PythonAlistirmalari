try: 
    sayi_1 = int(input("1. Sayıyı Giriniz: "))
    sayi_2 = int(input("2. Sayıyı Giriniz: "))
except ValueError:
    print("Geçersiz sayı. Lütfen tekrar deneyiniz.")
    exit()

toplam = 0
# Mükemmel sayı bulma algoritması (ÖRN: 6 = 1 + 2 + 3)
# Mükemmel sayı : Bir sayının kendisi hariç bölenlerinin toplamı kendisine eşit olan sayıdır.
for i in range(1, sayi_1):
    if sayi_1 % i == 0:
        print(f"Sayi : {sayi_1} Bölen : {i}")
        toplam += i
    
if toplam == sayi_1:
    print(f"{sayi_1} bir tam MÜKEMMEL sayıdır.")
else:
    print(f"{sayi_1} bir tam MÜKEMMEL sayı değildir !")

# Armstrong sayı bulma algoritması (ÖRN: 153 = 1^3 + 5^3 + 3^3)
# Armstrong sayı : Bir sayının basamaklarının sayının rakamlarının kuvvetlerinin toplamı kendisine eşit olan sayıdır.
rakamlar = [int(x) for x in str(sayi_2)]
toplam = 0

for rakam in rakamlar:
    toplam += rakam ** len(rakamlar)

if toplam == sayi_2:
    print(f"{sayi_2} bir tam ARMSTRONG sayıdır.")
else:
    print(f"{sayi_2} bir tam ARMSTRONG sayı değildir !")

# Çarpım tablosu
for i in range(1, 11):
    print("*" * 50)
    for j in range(1,11):
        print(f"{i} x {j} = {i * j}")

# Fibonacci sayıları

fibonacci = []

a = 1
b = 1

for i in range(10):
    a,b = b, a + b
    print(f"a sayısı : {a} b sayısı : {b}")
    fibonacci.append(a)

print(f"Fibonacci sayıları : {fibonacci}")

# while döngüsü

onay_while = input("While döngüsünü çalıştırmak istiyor musunuz? (E/H): ").lower()

if onay_while == "e":
    toplam = 0
    while True:
        sayi = int(input("Bir sayı giriniz: "))
        toplam += sayi
        if sayi == 0:
            break
        print(f"Toplam : {toplam}")

else:
    print("While döngüsü çalıştırılmadı.")

# 1 den 100 e kadar olan 3 e bölünen sayılar
katlari_3 = []
for i in range(1,101):
    if i % 3 !=0:
        continue
    else:
        katlari_3.append(i)

print(f"3'ün katları : {katlari_3}")

# 1 den 100 e kadar olan çift sayılar
çift_sayilar = [i for i in range(1,101) if i % 2 == 0]

print(f"Çift sayılar : {çift_sayilar}")