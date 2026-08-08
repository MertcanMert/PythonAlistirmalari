def separetor(mesaj):
    print("-" * 50)
    print(mesaj)
    print("-" * 50)


separetor("""
KULLANICI GİRİŞ EKRANI

1 ) KAYIT OL
2 ) GİRİŞ YAP
3 ) ÇIKIŞ
""")


kullanicilar = {
    "mertcan": "123456",
    "elif": "0511"
}

giris_denemesi = 3


while True:
    secim = input("Lütfen seçim yapınız : ").strip()

    # KAYIT OL
    if secim == "1":
        kullanici_adi = input("Kullanıcı Adı : ").strip().lower()
        sifre = input("Şifre : ").strip()

        if kullanici_adi in kullanicilar:
            print(
                "Kullanıcı adı zaten mevcut. "
                "Lütfen farklı bir kullanıcı adı giriniz."
            )
            continue

        kullanicilar[kullanici_adi] = sifre

        print("Kullanıcı başarıyla oluşturuldu.")
        separetor(f"Kullanıcı bilgileri : {kullanicilar}")

    # GİRİŞ YAP
    elif secim == "2":

        if giris_denemesi <= 0:
            separetor(
                "Giriş denemeleriniz bitti. "
                "Uygulama kapanıyor ..."
            )
            break

        kullanici_adi = input(
            "Kullanıcı Adı : "
        ).strip().lower()

        sifre = input("Şifre : ").strip()

        # Kullanıcı mevcut değil
        if kullanici_adi not in kullanicilar:
            giris_denemesi -= 1

            print("Kullanıcı bulunamadı.")

            separetor(
                f"Kalan giriş deneme sayısı : "
                f"{giris_denemesi}"
            )

            if giris_denemesi == 0:
                separetor(
                    "Giriş denemeleriniz bitti. "
                    "Uygulama kapanıyor ..."
                )
                break

            continue

        # Şifre yanlış
        if sifre != kullanicilar[kullanici_adi]:
            giris_denemesi -= 1

            print(
                "Girmiş olduğunuz bilgiler hatalı. "
                "Lütfen tekrar deneyiniz."
            )

            separetor(
                f"Kalan giriş deneme sayısı : "
                f"{giris_denemesi}"
            )

            if giris_denemesi == 0:
                separetor(
                    "Giriş denemeleriniz bitti. "
                    "Uygulama kapanıyor ..."
                )
                break

            continue

        # Giriş başarılı
        print("Giriş başarılı.")
        separetor(f"Hoşgeldin : {kullanici_adi}")
        break

    # ÇIKIŞ
    elif secim == "3":
        separetor("Çıkış yapıldı.")
        break

    # GEÇERSİZ SEÇİM
    else:
        print(
            "Geçersiz seçim. "
            "Lütfen tekrar deneyiniz."
        )