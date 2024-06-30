# 1- Girilen 2 sayıdan hangisi büyüktür?
# 2- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alarak ortalamayı hesaplayınız. Eğer ortalama 50 ve üzerindeyse geçti değilse kaldı yazdırın.
# 3- Girien bir sayının tek mi yoksa çift mi olduğunuz yazdırın.
# 4- Girilen bir sayının negatif-pozitif durumunu yazdırın.
# 5- E-posta ve parola bilgisini isteyip doğruluğunu kontrol ediniz.
#    (email: admin@muratyurur.com parola: abc123)

'''
# Çözüm 1:

num1 = input('Birinci Sayı:')
num2 = input('İkinci Sayı:')

if num1 > num2:
    print(f"{num1} sayısı {num2} sayısından büyüktür.")
else:
    print(f"{num2} sayısı {num1} sayısından büyüktür.")

'''

'''
# Çözüm 2:

visa1 = int(input('Birinci Vize Notu:'))
visa2 = int(input('İkinci Vize Notu:'))
final = int(input('Final Notu:'))

score = visa1 * 0.3 + visa2 * 0.3 + final * 0.4

if score >= 50:
    print(f"Tebrikler!\nNot ortalamanız: <{score}>. Bu dersten başarıyla geçtiniz.")
else:
    print(f"Üzgünüm...\nNot ortalamanız: <{score}>. Bu dersten geçemediniz.")
    
'''

'''
# Çözüm 3:

num = int(input('Sayı: '))

if num % 2 == 0:
    print(f"{num} bir çift sayıdır.")
else:
    print(f"{num} bir tek sayıdır.")

'''

'''
# Çözüm 4:

num = int(input('Sayı: '))

if num > 0:
    print(f"{num} pozitif bir sayıdır.")
else:
    print(f"{num} negatif bir sayıdır.")

'''

'''
# Çözüm 5:

email = 'admin@muratyurur.com'
password = 'abc123'

user_email = input('E-Posta Adresi: ')
user_password = input('Kullanıcı Adı: ')

if email != user_email or password != user_password:
    print('Hatalı e-posta adresi ya da parola.')
else:
    print('Kullanıcı girişi başarılı!')
    
'''
