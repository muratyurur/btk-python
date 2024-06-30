sayilar = [1, 3, 5, 7, 9, 12, 19, 21]

# 1- sayilar listesindeki hangi sayılar 3'ün katıdır?
# 2- sayilar listesindeki sayıların toplamı kaçtır?
# 3- sayilar listesindeki tek sayıların karesini alınız.

sehirler = ['Kocaeli', 'İstanbul', 'Ankara', 'İzmir', 'Rize']

# 4- Şehirlerden hangileri en fazla 5 karakterlidir?

urunler = [
    {'name': 'Samsung S6', 'price': '3000'},
    {'name': 'Samsung S7', 'price': '4000'},
    {'name': 'Samsung S8', 'price': '5000'},
    {'name': 'Samsung S9', 'price': '6000'},
    {'name': 'Samsung S10', 'price': '7000'}
]

# 5- Ürünlerin fiyatları toplamı nedir?
# 6- Ürünlerden fiyatı en fazla 5000 olan ürünleri gösteriniz.

'''
# Çözüm 1:

for x in sayilar:
    if x % 3 == 0:
        print(f"{x} 3'ün katıdır.")

'''

'''
# Çözüm 2:

total = 0

for x in sayilar:
    total += x

print(f"sayılar toplamı: {total}")

'''

'''
# Çözüm 3:

for x in sayilar:
    if x % 2 != 0:
        print(f"{x} karesi: {x ** 2}")
        
'''

'''
# Çözüm 4:
count = 0

for i in sehirler:
    if len(i) <= 5:
        count += 1

print(count)

'''

'''
# Çözüm 5:
total_price = 0

for urun in urunler:
    total_price += int(urun['price'])

print(total_price)

'''

# Çözüm 6:

for prod in urunler:
    if int(prod['price']) <= 5000:
        print(f"{prod['name']} adlı ürünün fiyatı: {prod['price']}₺")
