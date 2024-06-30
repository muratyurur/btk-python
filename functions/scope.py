# x = 'global x'
#
#
# def function():
#     x = 'local x'
#
#
# function()
#
# print(x)

###########################

# name = 'Ömer Buğra'
#
# def changeName(new_name):
#     name = new_name
#     print(name)
#
#
# changeName('Elif Birce')
# print(name)

###########################

# name = 'global string'
#
#
# def greeting():
#     # name = 'Ömer Buğra'
#
#     def hello():
#         # name = 'Elif Birce'
#         print('Hello ' + name)
#
#     hello()
#
#
# greeting()

###########################

x = 50


def test():
    global x
    print(f'x: {x}')

    x = 100
    print(f'x changed to -> {x}')


test()
print(x)
