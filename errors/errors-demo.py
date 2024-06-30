liste = ['1', '2', '5a', '10b', 'abc', '10', '50']


# 1- Liste elemanları içindeki sayısal değerleri bulunuz.

# 2- Kullanıcı 'q' değerini girmedikçe aldığınız her inputun sayısal değer olduğundan emin olunuz aksi halde hata mesajı
# yazdırın.

# 3- Girilen parola içinde türkçe karakter hatası verdirin.

# 4- Faktöriyel fonksiyonu oluşturup fonksiyona gelen değer için hata mesajları verin.

# Çözüm 1:

def sayisal_degerleri_bul(liste):
    sayisal_degerler = []
    for eleman in liste:
        try:
            if eleman.isdigit():
                sayisal_degerler.append(int(eleman))
        except ValueError:
            pass

    return sayisal_degerler


print(sayisal_degerleri_bul(liste))


# Çözüm 2:

def sayisal_deger_kontrol():
    while True:
        val = input('Bir sayısal değer giriniz (çıkmak için "q" tuşlayınız): ')
        if val.lower() == 'q':
            print('Programdan çıkış yapılıyor...')
            break
        try:
            if not val.isdigit():
                raise ValueError('Hata: Girmiş olduğunuz değer sayısal bir değer değildir.')
            print(f'Girmiş olduğunuz değer: {val}')
        except ValueError as e:
            print(e)


# sayisal_deger_kontrol()

# Çözüm 3:

turkish_chars = ['ğ', 'ü', 'ş', 'ö', 'ç', 'ı', 'Ğ', 'Ü', 'Ş', 'İ', 'Ö', 'Ç']


def turkce_karakter_kontrol(metin):
    for i in metin:
        if i in turkish_chars:
            raise ValueError('Girilen parolada türkçe karakter bulunuyor.')
        else:
            pass

    print('Parolanı başarıyla değiştirildi...')


# turkce_karakter_kontrol(input('Lütfen yeni parolanızı girin: '))


def parola_kontrol():
    turkce_karakterler = "çğıöşüÇĞİÖŞÜ"

    while True:
        parola = input('Bir parola giriniz (Çıkış içim "q" tuşlayınız): ')

        if parola.lower() == 'q':
            print('Programdan çıkılıyor')
            break

        try:
            if any(char in turkce_karakterler for char in parola):
                raise ValueError('Hata: Parola Türkçe karakter içermemelidir.')

            print(f'Girdiniz parola geçerli: {parola}')

        except ValueError as e:
            print(e)


# parola_kontrol()

# Çözüm 4:

def faktoriyel(x):
    x = int(x)

    if x < 0:
        raise ValueError('Negatif değer')

    result = 1

    for i in range(1, x + 1):
        result *= i

    return result


for x in [5, 10, 20, -3, '10a']:
    try:
        y = faktoriyel(x)
    except ValueError as e:
        print(e)
        continue

    print(y)
