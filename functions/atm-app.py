# bankamatik uygulaması

muratHesap = {
    'ad': 'Murat Yürür',
    'hesapNo': '12345678',
    'bakiye': 3000,
    'ekHesap': 2000,
}

fatmaHesap = {
    'ad': 'Fatma Aydın Yürür',
    'hesapNo': '87654321',
    'bakiye': 5000,
    'ekHesap': 3000,
}


def paraCek(hesap, miktar):
    print(f'Merhaba {hesap["ad"]}')

    if hesap['bakiye'] >= miktar:
        hesap['bakiye'] -= miktar
        print(
            f'paranızı alabilirsiniz. Güncel hesap bakiyeniz: {hesap['bakiye']}₺ ve Ek Hesap Bakiyeniz: {hesap['ekHesap']}₺')
    else:
        toplam = hesap['bakiye'] + hesap['ekHesap']

        if toplam >= miktar:
            ekHesapKullanimi = (
                input('Bu işlem için hesap bakiyeniz yetersiz. Ek hesabınızı kullanmak ister misiniz? (e/h)'))

            if ekHesapKullanimi == 'e':
                ekHesapKullanilacakMiktar = miktar - hesap['bakiye']

                hesap['bakiye'] = 0
                hesap['ekHesap'] -= ekHesapKullanilacakMiktar

                print('paranızı alabilirsiniz.')
                print(
                    f'{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']}₺ bakiye ve {hesap['ekHesap']}₺ ek bakiye bulunmaktadır.')
            else:
                print(
                    f'{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']}₺ bakiye ve {hesap['ekHesap']}₺ ek bakiye bulunmaktadır.')
        else:
            print('Bu işlem için yeterli bakiyeniz bulunmamaktadır.')


paraCek(muratHesap, int(input('Çekmek istediğiniz tutarı giriniz: ')))
paraCek(muratHesap, int(input('Çekmek istediğiniz tutarı giriniz: ')))
