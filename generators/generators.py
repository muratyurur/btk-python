# def cube(count):
#     for x in range(count):
#         yield x ** 3
#
#
# for i in cube(8):
#     print(i)

generator = (i ** 3 for i in range(5))

print(generator)

for i in generator:
    print(i)
