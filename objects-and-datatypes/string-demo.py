website = "http://www.muratyurur.com"
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"

# 1- 'course' karakter dizisinde kaç karakter bulunmaktadır?
print(len(course))

# 2- 'website' içinden www karakterlerini alın.

print(website[7:10])

# 3- 'website' içinden com karakterlerini alın.

print(website.split('.')[2])

# 4- 'course içinde ilk 15 ve son 15 karakterleri alın.

print(course[:16])
print(course[-15:])

# 5- 'course ifadesindeki karakterleri tersten yazdırın.

print(course[::-1])

name, surname, age, job = 'Bora', 'Yılmaz', 32, 'mühendis'

# 6- Yukarıdaki verilen değişkenler ile ekrana aşağıdaki ifadeyi yazdırın.
#   'Benim adım Bora Yılmaz, yaşım 32 ve mesleğim mühendis.'

print(f"Benim adım {name} {surname}, yaşım {age} ve mesleğim {job}.")

# 7- 'Hello world!' ifadesindeki w harfini 'W' ile değiştirin.

print('Hello world!'.replace('w', 'W'))

# 8- 'abc' ifadesini yan yana 3 defa yazdırın.

print('abc' * 3)
