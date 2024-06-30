'''

    ogrenciler = {
        '120': {
            'ad': 'Elif Birce',
            'soyad': 'Yürür',
            'telefon': '532 000 00 01',
        },
        '125': {
            'ad': 'Kuzey Kayra',
            'soyad': 'Öznalbant',
            'telefon': '532 000 00 02',
        },
        '128': {
            'ad': 'Ömer Buğra',
            'soyad': 'Yürür',
            'telefon': '532 000 00 03',
        },
    }

    1- Bilgileri verilen öğrencileri kullanıcıdan aldığınız bilgilerle dictionary içinde saklayınız.

    2- Öğrenci nuamrasını kullanıcıdan alıp ilgili öğrenci bilgisini gösterin.

'''

ogrenciler = {}

for i in range(0, 3):
    number = input('Öğrencinin numarasını girin:')
    ogrenciler.update({
        number: {
            'ad': input('Öğrencinin adını girin:'),
            'soyad': input('Öğrencinin soyadını girin:'),
            'telefon': input('Öğrencinin telefon numarasını girin:'),
        }
    })

print(ogrenciler)
