# Dosya açmak ve oluşturmak için open() fonksiyonu kullanılır.
# KullanımıÇ open(dosya_adi, dosya_erişme_modu)
# dosya_erişme_modu => dosyayı hangi amaçla açtığımızı belirtir.

# "w": (Write) yazma modu.
#       ** Dosyayı konumda oluşturur.
#       ** Dosya içeriğini siler ve yeniden ekleme yapar. (Üzerine yazar.)


# file = open("newfile.txt", "w")
# file = open("/Users/muratyurur/Desktop/deneme.txt", "w")
# file.close()

# file = open("newfile.txt", "w", encoding="utf-8")
# file.write("Murat Yürür")
# file.close()

# "a": (Append) ekleme modu. Dosya konumda yoksa oluşturur.

# file = open("newfile.txt", "a", encoding="utf-8")
# file.write("\nFatma Aydın Yürür")
# file.close()

# "x": (Create) oluşturma modu. Dosya zaten varsa hata verir.

file = open("newfile2.txt", "x", encoding="utf-8")

# "r": (Read) okuma modu. Dosya konumda yoksa hata verir.
