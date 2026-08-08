# Kullanıcı Giriş Paneli Simülasyonu
# .env simüle ediyoruz.

"""
Geliştirme aşamasında yazdığımız bir kodun doğrudan ne çıktı ürettiğini görmek isteriz. Görmek istediğimiz sonuçlar ise test ortamında zararsızken production aşamasında ölümcül açıklar oluşturabilir. Bu yüzden production aşamasında kodun doğrudan ne çıktı ürettiğini görmek istemiyoruz. Dacha sonradan uğraşmamak, kodun bakımının, okunurluğunun ve test edilebilirliğinin artması için böyle bir yaklaşım uyguluyoruz. Bu bu tarz alıştırma uygulamalcarında gerekli bir yöntem olmasa da el alışkanlığı, algoritma mantığının oturması ve alışkcanlık kazanma açısından önemli olduğunu düşünerek koda ekliyorum.
"""
production = False

# Veritabanını simüle ediyoruz.

kullanici_verileri = [
    {"kullanici_adi" : "mert",
    "şifre" : "1"},
    {"kullanici_adi" : "elif",
    "şifre" : "0511"},
    {"kullanici_adi" : "ahmet",
    "şifre" : "123456"},
    {"kullanici_adi" : "mehmet",
    "şifre" : "123456"},
    {"kullanici_adi" : "ali",
    "şifre" : "123456"},
    {"kullanici_adi" : "veli",
    "şifre" : "123456"},
    {"kullanici_adi" : "ayşe",
    "şifre" : "123456"},
]

giris_denemesi_sayisi = 3

# Sistem Mesaj Fonksiyonunu Oluşturuyoruz.

def sistem_mesaj(mesaj):
    print("-" * 50)
    print(f"[ SİSTEM MESAJI ] >>> {mesaj}")
    print("-" * 50)

# Giriş Fonksiyonunu Oluşturuyoruz.

def kullanici_giris(kullanici_adi: str, sifre: str, kullanicilar: list) -> str | bool:
    """
    Burada fonkson ile alakcalı bilgiler verebiliriz. Böylece fonksiyonu kullanan, dışarıdan çağıran kişiler bu fonksiyonu nasıl kullanacakları hakkında bilgiler alabilirler.

    kullanici_adi : String bir değer alır ve kullanıcı adını kontrol eder.
    sifre : String bir değer alır ve şifreni kontrol eder.
    kullanicilar : List bir değer alır ve kullanıcıların listesini kontrol eder.

    return : String bir değer döndürür. Eğer kullanıcı adı ve şifre doğruysa kullanıcı adını döndürür. Eğer kullanıcı adı veya şifre hatalıysa False döndürür.

    İlk olarak veritabanına bağlanıyoruz. Burada veritabanına bağlantı sekansının olduğunu varsayıyoruz. Normalde bu sürecince belirli aşamaları vardır ama şuanda bunları simüle ediyoruz. SQL konusunda alıştırmalarda;

    1) Veritabanına bağlantı kurma
    2) Veritabanına sorgu gönderme
    3) Veritabanından sonuç alma
    4) Veritabanından sonuç alındıktan sonra sonuç işleme
    5) Sonuç işlendikten sonra veritabanından çıkış
    6) İndex oluşturma
    7) Redis cache kullanımı
    8) ORM kullanımı
    gibi aşamaların olduğunu öğrenmişsin. Burada da bunları simüle ediyoruz.
    """

    kullanici_bilgileri = None
    
    # Veritabanında kullanıcıyı arıyoruz.
    for kullanici in kullanicilar:
        if kullanici_adi == kullanici["kullanici_adi"]:
            kullanici_bilgileri = kullanici
            if not production:
                sistem_mesaj("[ DEBUG ] Kullanıcı veritabanında bulundu ! ✅")
                sistem_mesaj(f"[ DEBUG ] Kullanıcı bilgileri : {kullanici_bilgileri} ✅")
            break
    
    # Kullanıcı bulunamadıysa
    if kullanici_bilgileri is None:
        if production:
            sistem_mesaj("Kullanıcı adı veya şifre hatalı. Lütfen tekrar deneyiniz. ❌")
        else:
            sistem_mesaj("[ DEBUG ] Kullanıcı veritabanında bulunamadı ! ❌")
        return False

    # Kullanıcı bulundu fakat şifre hatalıysa
    if sifre != kullanici_bilgileri["şifre"]:
        if production:
            sistem_mesaj("Kullanıcı adı veya şifre hatalı. Lütfen tekrar deneyiniz. ❌")
        else:
            sistem_mesaj("[ DEBUG ] Kullanıcı şifresi veritabanında bulunamadı ! ❌")
        return False
    
    # Kullanıcı bulundu ve şifre doğruysa
    if kullanici_adi == kullanici_bilgileri["kullanici_adi"] and sifre == kullanici_bilgileri["şifre"]:
        sistem_mesaj(f"Giriş başarılı. Hoşgeldiniz {kullanici_bilgileri["kullanici_adi"]}! ✅")
        return kullanici_bilgileri["kullanici_adi"]

while giris_denemesi_sayisi > 0:
    sistem_mesaj("Kullanıcı Giriş")

    kullanici_adi_giris = input("Kullanici adinizi giriniz : ").strip().lower()
    sifre_giris = input("Şifrenizi giriniz : ").strip()

    sonuc = kullanici_giris(kullanici_adi_giris, sifre_giris, kullanici_verileri)

    if sonuc:
        break

    giris_denemesi_sayisi -= 1

    if giris_denemesi_sayisi > 0:
        sistem_mesaj(f"Hatalı giriş. {giris_denemesi_sayisi} deneme hakkınız kaldı. 🔒")
    else:
        sistem_mesaj("Giriş hakkınız doldu. Lütfen daha sonra tekrar deneyiniz. 🔒")