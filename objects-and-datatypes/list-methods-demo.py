names = ['Ali', 'Yağmur', 'Hakan', 'Deniz']
years = [1998, 2000, 1998, 1987]

# 1- "Cenk" ismini listenin sonuna ekleyiniz.
names.append('Cenk')
# 2- "Sena" değerini listenin başına ekleyiniz.
names.insert(0, 'Sena')
# 3- "Hakan" ismini listeden siliniz.
names.remove('Hakan')
# 4- "Deniz" isminin indeksi nedir?
print(f"'Deniz' isminin indeksi: {names.index('Deniz')}")
# 5- "Ali" listenin bir elemanı mıdır?
print('Ali' in names)
# 6- Liste elemanlarını ters çevirin.
names.sort()
names.reverse()
# 7- Liste elemanlarını alfabetik olarak sıralayınız.
names.sort()
# 8- years listesini rakamsal büyüklüğe göre sıralayınız.
years.sort()
# 9- str = "Chevrolet, Dacia" karakter dizisini listeye çeviriniz.
str = "Chevrolet, Dacia"
brands = []
brands.append(str)
print(brands)
# 10- years dizisinin en büyük ve en küçük elemanı nedir?
print(f"en büyük eleman: {max(years)}, en küçük eleman: {min(years)}")
# 11- years dizisinde kaç tane 1998 değeri vardır?
print(f"1998 years dizisinde {years.count(1998)} defa geçmektedir.")
# 12- years dizisinin tüm elemanlarını siliniz.
years.clear()
# 13- Kullanıcıdan alacağınız 3 tane marka bilgisini bir listede saklayınız.
first = input("Birinci markayı girin:")
second = input("Birinci markayı girin:")
third = input("Birinci markayı girin:")

brands = [first, second, third]

print(names)
print(years)
print(brands)
