# with open('newfile.txt', "r+", encoding='utf-8') as file:
#     print(file.read())
#
# with open('newfile.txt', "r+", encoding='utf-8') as file:
#     file.seek(20)
#     file.write("deneme")
#     print(file.read())


with open("newfile.txt", "a", encoding="utf-8") as file:
    file.write("\nMurat Yürür")

with open("newfile.txt", "r", encoding="utf-8") as file:
    print(file.read())
