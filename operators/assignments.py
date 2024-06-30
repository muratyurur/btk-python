x, y, z, = 2, 5, 107

numbers = 1, 5, 7, 10, 6

# 1- Kuıllanıcıdan aldığınız 2 sayının çarpımı ile x,y,z toplamının farkı nedir?

# first = int(input('Birinci sayıyı girin:'))
# second = int(input('İkinci sayıyı girin:'))
#
# print((first + second) - (x + y + z))

# 2- y'nin x'e kalansız bölümünü hesaplayınız.

print(y / x)
print(y // x)

# 3- (x,y,z) toplamının mod 3'ü nedir?

print((x + y + z) % 3)

# 4- y'nin x. kuvvetini hesaplayınız.

print(y ** x)

# 5- x, *y, z = numbers işlemine göre z'nin küpü kaçtır?

x, *y, z = numbers

print(z ** 3)

# 6- x, *y, z = numbers işlemine göre y'nin değerleri toplamı kaçtır?

total = 0

for i in y:
    total += i

print(total)
