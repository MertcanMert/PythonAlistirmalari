# ATM Makinesi Programı

from time import sleep


def sistem_mesajı(mesaj):
    print("-" * 50)
    print(mesaj.center(50))
    print("-" * 50)

def separetor():
    print("-" * 50)

mustri_bilgileri_verisi = [
    {
        "kullanici_adi": "mert",
        "sifre": "1",
        "bakiye": 1000,
    },
    {
        "kullanici_adi": "elif",
        "sifre": "12",
        "bakiye": 10000000,
    },
]

# Kullanıcı giriş yapmasını istiyoruz.
def giris_yap(kullanici_adi:str, sifre:str, musteri_bilgileri:list) -> dict | None:
    """

    Args:
        kullanici_adi (str): Kullanıcı adı
        sifre (str): Şifre
        mustri_bilgileri (list): Mustri bilgileri
        giris_deneme_hakki (int): Giriş deneme hakkı

    Returns:
        bool: True veya False
    """

    # Listedeki tüm müşterileri dolaş; eşleşme yoksa döngü BITINCE hata ver.
    # else+return döngü içinde olursa ilk eşleşmeyen kayıtta (örn. mert)
    # fonksiyon biter ve elif hiç denenmez.
    for musteri in musteri_bilgileri:
        if kullanici_adi == musteri["kullanici_adi"] and sifre == musteri["sifre"]:
            sistem_mesajı(f"Hoşgeldiniz SN {musteri['kullanici_adi'].upper()}")
            print(f"Bakiyeniz: {musteri['bakiye']} TL")
            separetor()
            return {
                "giris": True,
                "musteri": musteri,
            }

    print("[SİSTEM] >>> Hatalı kullanıcı adı veya şifre. Lütfen tekrar deneyiniz.")
    return None

# Kullanıcıdan bir seçim yapmasını istiyoruz.
def menu_goster():
    print("""    
    [1] Bakiye Sorgulama
    [2] Para Çekme
    [3] Para Yatırma
    [4] MRT Para Transferi


    [9] Çıkış Yap

    [0] Oturum Değiştirme
    """)
    separetor()
    secim = input("Seçiminiz: ")
    return secim

# Kullanıcının seçimine göre işlemleri gerçekleştiriyoruz.
def islemler(menu_secimi:str, oturum:dict) -> str:
    """'devam' | 'oturum_degistir' | 'cikis'"""

    musteri = oturum["musteri"]

    match menu_secimi:
        case "1":
            print(f"Bakiyeniz : {musteri["bakiye"]} TL")
            return "devam"
        case "2":
            try:
                talep_edilen_tutar = float(input("Para Çekme Tutarınızı Giriniz: "))
            except ValueError:
                print("Geçersiz para tutarı. Lütfen tekrar deneyiniz.")
                return "devam"
            
            if talep_edilen_tutar <= 0:
                print("Para Çekme Tutarınız 0'dan büyük olmalıdır. Lütfen tekrar deneyiniz.")
                return "devam"
            elif talep_edilen_tutar > musteri["bakiye"]:
                print("Bakiyeniz yetersiz. Lütfen tekrar deneyiniz.")
                return "devam"
            else:
                musteri["bakiye"] -= talep_edilen_tutar
                print(f"""
                Para Çekme İşlemi Başarılı. 
                Çekilen Tutar: {talep_edilen_tutar} TL. 
                Bakiyeniz    : {musteri["bakiye"]} TL""")
                separetor()
                return "devam"
        case "3":
            try:
                yatirilan_tutar = float(input("Para Yatırma Tutarınızı Giriniz: "))
            except ValueError:
                print("Geçersiz para tutarı. Lütfen tekrar deneyiniz.")
                return "devam"
            
            if yatirilan_tutar <= 0:
                print("Para Yatırma Tutarınız 0'dan büyük olmalıdır. Lütfen tekrar deneyiniz.")
                return "devam"
            else:
                musteri["bakiye"] += yatirilan_tutar
                print(f"""
                Para Yatırma İşlemi Başarılı. 
                Yatırılan Tutar: {yatirilan_tutar} TL. 
                Bakiyeniz    : {musteri["bakiye"]} TL""")
                separetor()
                return "devam"
        case "4":
            return para_transferi(oturum)
        case "9":
            print("Çıkış Yapılıyor...")
            return "cikis"
        case "0":
            """
            Kullanıcı oturumunu değiştiriyoruz.
            """
            oturum["giris"] = False
            oturum["musteri"] = None
            return "oturum_degistir"
        case _:
            print("Geçersiz seçim. Lütfen tekrar deneyiniz.")
            return "devam"

# Para Transferi Fonksiyonu
def para_transferi(oturum:dict, mustri_bilgileri_verisi=mustri_bilgileri_verisi) -> str:
    """
    Args:
        oturum (dict): Oturum bilgileri
        transfer_miktari (float): Transfer edilecek miktar

    Returns:
        str: 'devam' | 'oturum_degistir' | 'cikis'
    """

    gonderici = oturum["musteri"]
    try:
        transfer_miktari = float(input("Transfer Edilecek Miktarı Giriniz: "))
    except ValueError:
        print("Geçersiz para tutarı. Lütfen tekrar deneyiniz.")
        return "devam"
    alici = input("Transfer Edilecek Kişinin Kullanıcı Adını Giriniz: ").strip().lower()

    for x in mustri_bilgileri_verisi:
        if alici == x["kullanici_adi"]:
            if transfer_miktari <= 0:
                print("Transfer Edilecek Miktar 0'dan büyük olmalıdır. Lütfen tekrar deneyiniz.")
                return "devam"
            elif transfer_miktari > gonderici["bakiye"]:
                print("Bakiyeniz yetersiz. Lütfen tekrar deneyiniz.")
                return "devam"
            else:
                onay = input(f"""
                Sayın {gonderici["kullanici_adi"].upper()}
                Bir para tansferi işlemi gerçekleştiriyorsumuz. 
                >>> Gönderen : {gonderici["kullanici_adi"].upper()}
                >>>Alıcı    : {x["kullanici_adi"].upper()}
                >>> Transfer Edilecek Miktar: {transfer_miktari} TL
                >>> Onaylıyor musunuz? (E/H): """)

                if onay.lower() == "e":
                    gonderici["bakiye"] -= transfer_miktari
                    print("Transfer işlemi başladı. Para hesabınızdan çekiliyor...")
                    sleep(2)
                    x["bakiye"] += transfer_miktari
                    print("Transfer işlemi başarılı. Para hesabınıza yatırılıyor...")
                    sleep(2)
                    print("Transfer işlemi başarılı !")
                    print(f"""
                    Sayın {gonderici["kullanici_adi"].upper()}
                    Transfer işlemi başarılı. 
                    Transfer Edilen Tutar: {transfer_miktari} TL. 
                    Bakiyeniz    : {gonderici["bakiye"]} TL
                    """)

    print("Transfer Edilecek Kişi Bulunamadı. Lütfen tekrar deneyiniz.")
    return "devam"

sistem_mesajı("XYZ BANKA HOŞGELDİNİZ")

max_deneme = 3
deneme = 0


while deneme < max_deneme:
    # Kullanıcı Bilgilerini Talep Ediyoruz.
    kullanici_adi = input("Kullanıcı Adınızı Giriniz: ").strip().lower()
    sifre = input("Şifrenizi Giriniz: ").strip()

    # Oturum Bilgilerini Saklıyoruz.
    oturum = giris_yap(kullanici_adi, sifre, mustri_bilgileri_verisi)

    if oturum is None:
        deneme += 1
        print(f"Giriş yapılamadı. {max_deneme - deneme} deneme hakkınız kaldı.")
        continue

    deneme = 0
    sonuc = "devam"

    # Kullanıcı kart bilgileri doğrulandıktan sonra menüye yönlendiriyoruz.
    while sonuc == "devam":
        secim = menu_goster()
        sonuc = islemler(secim, oturum)

    # İç döngü bittikten sonra karar ver: continue/break burda dış while'ı etkiler.
    if sonuc == "oturum_degistir":
        continue  # yeniden giriş (başka kullanıcı, örn. elif)
    if sonuc == "cikis":
        break  # programı bitir
else:
    sistem_mesajı("Hesap geçici olarak kilitlendi. Lütfen banka ile iletişime geçiniz.")

