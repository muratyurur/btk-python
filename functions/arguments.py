# def changeName(n):
#     n = 'Elif Birce'
#
#
# name = 'Ömer Buğra'
#
# changeName(name)
#
# print(name)
#
#
# def change(n):
#     n[0] = 'istanbul'
#
#
# cities = ['ankara', 'izmir']
#
# change(cities)
#
# print(cities)

# def add(*params):
#     print(params)
#     print(params[0])
#     return sum((params))
#
#
# print(add(10, 20))
# print(add(10, 20, 30))
# print(add(10, 20, 30, 50, 60, 10, 20))

def displayUser(**args):
    for key, value in args.items():
        print(f'{key} is {value}')


displayUser(name='Ömer Buğra', age=2, city='İstanbul')
displayUser(name='Elif Birce', age=8, mail='ebirceyurur@gmail.com')
displayUser(name='Kuzey Kayra', age=7, mail='kuzeykayraoznalbant@gmail.com', phone='12345612')


def myFunc(a, b, c, *args, **kwargs):
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)


myFunc(10, 20, 30, 40, 50, 60, 70, key1='value 1', key2='value2')
