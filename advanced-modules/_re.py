import re

str = 'Python Kursu: Python Programlama Rehberiniz | 40 Saat'

# result = re.findall("Python", str)
# result = len(result)

# re.split()

# result = re.split(" ", str)
# result = re.split('R', str)

# result = re.sub("\s", "-", str)

# result = re.search('Python', str)
#
# result = result.span()

# result = result.start()
# result = result.end()
# result = result.group()
# result = result.string

result = re.findall("[abc]", str)
result = re.findall("[sat]", str)
result = re.findall("[a-e]", str)
result = re.findall("[a-z]", str)
result = re.findall("[0-5]", str)
result = re.findall("[^abc]", str)
result = re.findall("[^0-9]", str)
result = re.findall("...", str)
result = re.findall("Py..on", str)
result = re.findall("^P", str)
result = re.findall("t$", str)
result = re.findall("Saat$", str)
result = re.findall("Saatt$", str)
result = re.findall("Saatt$", str)
result = re.findall("Sa*t", str)
result = re.findall("Sa+t", str)
result = re.findall("Sa?t", str)
result = re.findall("a{2}", str)
result = re.findall("[0-9]{2}", str)
# result = re.findall("\APython", str)
# result = re.findall("Saat\Z", str)
result = re.findall("[0-9]{2}", str)

print(result)
