"""
# Oyun Haritası
"""
odalar = {
    "giris": {
        "aciklama": "Karanlık bir giriş.", 
        "kuzey": "salon"},
    "salon": {
        "aciklama": "Geniş bir salon. Bir anahtar parlıyor.",
        "guney": "giris", 
        "dogu": "hazine"},
    "hazine": {
        "aciklama": "Kilitli hazine kapısı.",
        "bati": "salon"},
}
"""
# Oyuncu Bilgileri
"""
kullanici_bilgileri = {
    "kullanici_adi": "",
    "hp": 100,
    "konum": "giris",
    "aktif_odalar": [""],
    "ekipmanlar": {
        "anahtar": False,
        "hazine": False
    },
}

# Kullanıcıdan alacağımız komutları önden belirliyoruz !
komutlar = ["bak", "kuzey", "al", "dogu", "ac", "cik", "yardim"]

# Seperator Fonksiyonu
def seperator(mesaj):
    print("-" * 20)
    print(mesaj.center(20).upper())
    print("-" * 20)

# Sistem Mesajı Fonksiyonu
def sistem_mesaji(mesaj):
    return f"[ SİSTEM MESAJI ] >>> {mesaj}"

# Kullanıcı Adı Fonksiyonu
def kullanici_adi_kontrol(kullanici_adi):
    if not kullanici_adi:
        print(sistem_mesaji("Kullanıcı adı boş bırakılamaz! Tekrar deneyiniz."))
        return False
    elif len(kullanici_adi) < 3:
        print(sistem_mesaji("Kullanıcı adı en az 3 karakter olmalıdır! Tekrar deneyiniz."))
        return False
    elif len(kullanici_adi) > 10:
        print(sistem_mesaji("Kullanıcı adı en fazla 10 karakter olmalıdır! Tekrar deneyiniz."))
        return False
    else:
        return kullanici_adi

# Kullanıcı Bilgileri Fonksiyonu
def kullanici_bilgileri_goster():
    seperator("KULLANICI BİLGİLERİ")
    print(f"Kullanıcı Adı : {kullanici_bilgileri['kullanici_adi']}")
    print(f"HP : {kullanici_bilgileri['hp']}")
    print(f"Konum : {kullanici_bilgileri['konum']}")
    print(f"Aktif Odalar : {kullanici_bilgileri['aktif_odalar']}")
    print(f"Ekipmanlar : {kullanici_bilgileri['ekipmanlar']}")

# Harita konum bilgisini göster ve konum dön !
def harita_goster(konum):
    while True:
        # 1. Oda oyunda hiç yoksa
        if konum not in odalar:
            print(sistem_mesaji("Gitmek istediğiniz oda karanlık dünyada yok! Tekrar deneyiniz."))
            konum = input(sistem_mesaji("Lütfen geçerli bir oda giriniz: ")).strip().lower()
        
        # 2. Girilen oda HEM mevcut konum DEĞİLSE HEM DE aktif odalar listesinde YOKSA
        elif konum != kullanici_bilgileri['konum'] and konum not in kullanici_bilgileri['aktif_odalar']:
            print(sistem_mesaji("Bu odaya şu an erişemezsiniz !"))
            konum = input(sistem_mesaji("Lütfen geçerli bir oda giriniz: ")).strip().lower()
            
        # 3. Şartlar sağlanıyorsa (Bulunduğu konumdaysa veya aktif odalardan biriyse)
        else:
            print(sistem_mesaji(odalar[konum]['aciklama']))
            return konum

# Kullanıcı Komutları Fonksiyonu
def kullanici_komutlari(komut):
    while True:
        if komut not in komutlar:
            print(sistem_mesaji("Geçersiz komut! Tekrar deneyiniz."))
            komut = input(sistem_mesaji("KOMUT : ")).strip().lower()
        
        match komut:
            case "bak":
                harita_goster(kullanici_bilgileri['konum'])
                yonler = [yon for yon in odalar[kullanici_bilgileri['konum']].keys() if yon != "aciklama"]
                print(sistem_mesaji(f"Yönler : {", ".join(yonler)}"))
                komut = input(sistem_mesaji("KOMUT : ")).strip().lower()
            case "kuzey" | "guney" | "dogu" | "bati":
                if komut not in odalar[kullanici_bilgileri['konum']].keys():
                    print(sistem_mesaji("Bu yöne gidemezsiniz! Tekrar deneyiniz."))
                else:
                    kullanici_bilgileri['konum'] = odalar[kullanici_bilgileri['konum']][komut]
                    kullanici_bilgileri['aktif_odalar'].append(kullanici_bilgileri['konum'])
                    print(sistem_mesaji("Odaya giriş yapıldı. Konum bilgileri güncellendi."))
                    print(sistem_mesaji(f"Aktif Konumunuz : {kullanici_bilgileri['konum']}"))
                    komut = input(sistem_mesaji("KOMUT : ")).strip().lower()
            case "al":
                if kullanici_bilgileri['konum'] == "salon":
                    kullanici_bilgileri['ekipmanlar']['anahtar'] = True
                    print(sistem_mesaji("Anahtar alındı. Şimdi kilitli hazine kapısını açabilirsiniz."))
                    komut = input(sistem_mesaji("KOMUT : ")).strip().lower()
                else:
                    print(sistem_mesaji("Bu odaya anahtar yok. Tekrar deneyiniz."))
                    komut = input(sistem_mesaji("KOMUT : ")).strip().lower()
            case "ac":
                if kullanici_bilgileri['konum'] == "hazine" and kullanici_bilgileri['ekipmanlar']['anahtar']:
                    print(sistem_mesaji("Hazine kapısı açıldı. Şimdi hazineyi alabilirsiniz."))
                    print(sistem_mesaji("TEBRİKLER ! HAZİNEYİ BAŞARILI BİR ŞEKİLDE ALDINIZ !"))
                    print(sistem_mesaji("YENİDEN GÖRÜŞÜRÜZ !"))
                    break
                else:
                    print(sistem_mesaji("Anahtarınız yok / hazine odasında değilsiniz"))
                    komut = input(sistem_mesaji("KOMUT : ")).strip().lower()
            case "bilgi":
                kullanici_bilgileri_goster()
                komut = input(sistem_mesaji("KOMUT : ")).strip().lower()
            case "cik":
                break
            case _:
                print(sistem_mesaji("Geçersiz komut! Tekrar deneyiniz."))
                komut = input(sistem_mesaji("KOMUT : ")).strip().lower()

while True:
    kullanici_adi = kullanici_adi_kontrol(input(sistem_mesaji("Kullanıcı Adını Giriniz : ")).strip().lower())
    if kullanici_adi:
        kullanici_bilgileri['kullanici_adi'] = kullanici_adi
        seperator(f"Hoşgeldin {kullanici_adi.upper()} !")
        kullanici_komutlari(input(sistem_mesaji("KOMUT : ")).strip().lower())
        break
    else:
        continue