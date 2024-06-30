import os

result = dir(os)

result = os.name

# klasör oluşturma
# os.mkdir('new-directory')

# os.chdir('..')

# etkin klasörü öğrenme
# result = os.getcwd()

# os.makedirs('new-directory/yeni-klasor')

# result = os.listdir()

# for dosya in os.listdir():
#     if dosya.endswith('.py'):
#         print(dosya)

result = os.stat("_date.py")

# result = result.st_size / 1024
# result = datetime.datetime.fromtimestamp(result.st_ctime) # oluşturulma tarihi
# result = datetime.datetime.fromtimestamp(result.st_atime) # son erişilme tarihi
# result = datetime.datetime.fromtimestamp(result.st_mtime) # değiştirilme tarihi

# os.rename('new-directory', 'yeni-klasor')

# os.removedirs('yeni-klasor/yeni-klasor')

# path

result = os.path.abspath('_os.py')
result = os.path.dirname('/Users/muratyurur/Desktop/Projeler/btk-python/advanced-modules/_os.py')
result = os.path.dirname(os.path.abspath('_os.py'))

result = os.path.exists('_os.py')

result = os.path.isdir('/Users/muratyurur/Desktop/Projeler/btk-python/advanced-modules')
result = os.path.isdir('/Users/muratyurur/Desktop/Projeler/btk-python/advanced-modules/_os.py')

result = os.path.isfile('/Users/muratyurur/Desktop/Projeler/btk-python/advanced-modules/_os.py')

result = os.path.splitext('_os.py')

result = result[1]

print(result)
