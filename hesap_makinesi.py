"""
PYTHON ALIŞTIRMALARI - HESAP MAKİNESİ

Kullanıcıdan alacağımız iki sayıyı toplayıp sonucu ekrana yazdıran bir hesap makinesi programı yazınız.
"""

def separetor(mesaj):
    print("-" * 50)
    print(mesaj)
    print("-" * 50)

separetor("""
HESAP MAKİNESİ

1. Toplama
2. Çıkarma
3. Çarpma
4. Bölme

q : Çıkış
""")

def toplama(*args) -> float:
    return sum(args)

def cikarma(*args) -> float:
    return args[0] - args[1]

def carpma(*args) -> float:
    return args[0] * args[1]

def bolme(*args) -> float:
    if args[1] == 0:
        return "Sıfıra bölme hatası"
    return args[0] / args[1]

while True:
    secim = input("Seçiminiz : ").strip().lower()

    matematiksel_işlemler ={
        "1" : toplama,
        "2" : cikarma,
        "3" : carpma,
        "4" : bolme,
    }

    if secim in matematiksel_işlemler.keys():
        sayi_1 = float(input("1. Sayı : "))
        sayi_2 = float(input("2. Sayı : "))
        sonuc = matematiksel_işlemler[secim](sayi_1, sayi_2)
        separetor(f"Sonuc = {sonuc}")
    elif secim == "q":
        break
    else:
        separetor("Geçersiz seçim")
        continue

separetor("Çıkış yapıldı")
