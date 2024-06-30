sayilar = [1, 3, 5, 7, 9, 12, 19, 21]

# 1- sayilar listesini while ile ekrana yazdırın
# 2- Başlangıç ve bitiş değerlerini kullanıcıdan alıp aradaki tüm tek sayıları ekrana yazdırın
# 3 - 1-100 arasındaki sayıları azalan sırayla yazdırın.
# 4- Kullanıcıdan alacağınız 5 sayıyı ekranda sıralı bir şekilde yazdırın.
# 5- Kullanıcıdan alacağınız sınırsız ürün bilgisini ürünler listesinde saklayın.
#   ** ürün sayısını kullanıcıya sorun
#   ** dictionary liste yapısı (name, price) şeklinde olsun.
#   ** ürün ekleme işlemi bittiğinde ürünleri ekranda while ile listeleyin.

'''
# Çözüm 1:
i = 0

while i < len(sayilar):
    print(sayilar[i])
    i += 1

'''

'''
# Çözüm 2:
start = int(input('Başlangıc Değeri: '))
end = int(input('Bitiş Değeri: '))

while start <= end:
    if start % 2 != 0:
        print(start)
    start += 1

'''

'''
# Çözüm 3:

num = 100

while num > 0:
    print(num)
    num -= 1

'''

'''
# Çözüm 4:
i = 0

numbers = []

while i < 5:
    numbers.append(int(input('sayı: ')))
    i += 1

numbers.sort()

print(numbers)

'''

# Çözüm 5:

count = int(input('Max ürün sayısı:'))
i = 0

products = []

while i <= count:
    temp_product = {}

    temp_product['name'] = input('Ürün Adı: ')
    temp_product['price'] = input('Ürün Fiyatı: ')

    products.append(temp_product)

    i += 1

x = 0

while x < len(products):
    print(f"{products[x]['name']} adlı ürünün fiyatı {products[x]['price']}₺")
    x += 1
