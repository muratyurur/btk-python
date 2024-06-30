# 1- Gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyonu yazınız.
# 2- Kendine gönderilen sınırsız sayıdaki parametreyi bir listeye çeviren fonksiyonu yazınız.
# 3- Gönderilen 2 sayı arasındaki tüm asal sayıları bulan fonksiyonu yazınız.
# 4- Kendisine gönderilen bir sayının tam bölenlerini bir liste şeklinde döndüren fonksiyonu yazınız.

'''
# Çözüm 1:

def repeatWord(word, repeat):
    print(word * repeat)


repeatWord('deneme ', 5)

'''

'''
# Çözüm 2:

def createList(*args):
    myList = []
    for i in args:
        myList.append(i)

    print(myList)


createList(10, 20, 30, 40, 50)

'''

'''
# Çözüm 3:
def getPrimes(num1, num2):
    primes = []
    check = False
    for num in range(num1, num2 + 1):
        for i in range(2, num):
            if num % i == 0:
                check = False
                break
            else:
                check = True

        if check:
            primes.append(num)

    return primes


print(getPrimes(10, 15))
print(getPrimes(20, 35))

'''


# Çözüm 4:

def returnsExactDivisors(num):
    result = []
    for i in range(2, num):
        if num % i == 0:
            result.append(i)

    return result


print(returnsExactDivisors(10))
print(returnsExactDivisors(27))
print(returnsExactDivisors(36))
print(returnsExactDivisors(60))
print(returnsExactDivisors(145))
