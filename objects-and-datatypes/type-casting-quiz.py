"""
    Daire Alanı     : πr2
    Daire Çevresi   : 2πr

    * Yarı çapı verilen bir dairenin alan ve çevresini hesaplayınız. (π = 3.14)
"""

pi = 3.14

r = input("Lütfen yarıçap bilgisini girin: ")

r = int(r)

area = pi * (r ** 2)
perimeter = 2 * (pi * r)

print("Yarıçapı " + str(r) + " metre olan dairenin çevresi " + str(int(perimeter)) + " metre ve alanı " + str(
    int(area)) + " metrekaredir.")
