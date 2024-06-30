# 1- Kullanıcıdan isim, yaş ve eğitim bilgilerini isteyip ehliyet alabilme durumunu kontrol ediniz. Ehliyet alma koşulu
# en az 18 yaş ve eğitim durumu lise ya da üniversite olmalıdır.

# 2- Bir öğrencinin 2 yazılı bir sözlü notunu alıp hesaplanan ortalamaya göre not aralığına karşılık gelen not bilgisini
# yazdırınız.
#  0-24  =>  0
# 25-44  =>  1
# 45-54  =>  2
# 55-69  =>  3
# 70-84  =>  4
# 85-100 =>  5

# 3- Trafiğe çıkış tarihi alınan bir aracın servis zamanını aşağıdaki bilgilere göre hesaplayınız.

# 1. Bakım => 1. yıl
# 2. Bakım => 2. yıl
# 3. Bakım => 3. yıl
# ** Süre hesabını alınan gün, ay, yıl bilgisine göre gün bazlı hesaplayınız.
# ** datetime modülünü kullanmanız gerekiyor.

'''
# Çözüm 1:

name = input('Adınız: ')
age = int(input('Yaşınız: '))
graduation = input('Öğrenim Durumunuz: ')

classes = ['lise', 'üniversite']

print(f"Merhaba Sn. {name}. Başvuru sonucunuz aşağıdaki gibidir:")

if age <= 18:
    print('"18 yaşından küçük olduğunuz için ehliyet alamazsınız."')
elif graduation not in classes:
    print('"Öğrenim durumunuz uygun olmadığından ehliyet alamazsınız."')
else:
    print('"Ehliyet almanızda herhangi bir sakınca yoktur. Başvuru yapabilirsiniz."')

'''

'''
# Çözüm 2:

not1 = int(input('1. Yazılı Notu: '))
not2 = int(input('2. Yazılı Notu: '))
not3 = int(input('Sözlü Notu: '))

score = (not1 + not2 + not3) // 3

print('--------------------------------------')

if score >= 85:
    print(f'Not ortalamanız: {score} | Karne notunuz: 5')
elif 70 <= score < 85:
    print(f'Not ortalamanız: {score} | Karne notunuz: 4')
elif 55 <= score < 70:
    print(f'Not ortalamanız: {score} | Karne notunuz: 3')
elif 45 <= score < 55:
    print(f'Not ortalamanız: {score} | Karne notunuz: 2')
elif 25 <= score < 45:
    print(f'Not ortalamanız: {score} | Karne notunuz: 1')
else:
    print(f'Not ortalamanız: {score} | Karne notunuz: 0')

'''

'''
# Çözüm 3:
from datetime import datetime, timedelta

start_date = datetime.strptime(input('Trafiğe çıkış tarihi: '), "%d.%m.%Y")

first_service_date = start_date + timedelta(days=365)
second_service_date = first_service_date + timedelta(days=365)
third_service_date = second_service_date + timedelta(days=365)

print(f"1. Bakım Tarihi: {first_service_date.strftime('%d.%m.%Y')}")
print(f"2. Bakım Tarihi: {second_service_date.strftime('%d.%m.%Y')}")
print(f"3. Bakım Tarihi: {third_service_date.strftime('%d.%m.%Y')}")

'''
