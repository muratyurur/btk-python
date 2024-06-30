# try:
#     file = open("newfile.txt", "r")
#     print(file)
# except FileNotFoundError:
#     print("Dosya okuma hatası")
# finally:
#     print("Dosya kapandı.")
#     file.close()

file = open('newfile.txt', 'r', encoding='utf-8')

# ************* for döngüsü

# for i in file:
#     print(i, end='')

# ************* read() fonksiyonu
# content1 = file.read()
#
# print("İçerik 1")
# print(content1)
#
file = open('newfile.txt', 'r', encoding='utf-8')
#
# content2 = file.read()
#
# print("İçerik 2")
# print(content2)

# content = file.read(5)
# content = file.read(3)
# content = file.read(3)

# print(content)


# ************* readline() fonksiyonu

# print(file.readline(), end="")
# print(file.readline(), end="")
# print(file.readline(), end="")
# print(file.readline(), end="")
# print(file.readline(), end="")
# print(file.readline(), end="")

# liste = file.readlines()
#
# print(liste[0])
# print(liste[1])
# print(liste[2])
#

file.close()
