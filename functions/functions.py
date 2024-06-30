def say_hello(name='user'):
    return 'Hello ' + name


print(say_hello('Murat'))
print(say_hello('Fatma'))
print(say_hello())


def total(num1, num2):
    return num1 + num2


result = total(10, 20)
result = total(15, 27)

print(result)


def yas_hesapla(dogum_yili):
    return 2024 - dogum_yili


eb_yas = yas_hesapla(2015)
kk_yas = yas_hesapla(2017)
ob_yas = yas_hesapla(2021)

print(eb_yas, kk_yas, ob_yas)


def EmekliligeKacYilKaldi(dogumYili, isim):
    print(f"Sn. {isim}")

    yas = yas_hesapla(dogumYili)

    emeklilik = 60 - yas

    if emeklilik > 0:
        print(f"Emekliliğinize {emeklilik} yıl kaldı.")
    else:
        print('Zaten emekli oldunuz...')


EmekliligeKacYilKaldi(1982, 'Murat Yürür')
