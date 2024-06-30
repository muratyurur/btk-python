fruits = {'orange', 'apple', 'banana'}

# print(fruits[0]) indekslenemez

for x in fruits:
    print(x)

fruits.add('cherry')

print(fruits)

fruits.update(['mango', 'grape', 'apple'])

print(fruits)

my_list = [1, 2, 5, 4, 4, 2, 1]

print(my_list)

print(set(my_list))

fruits.remove('mango')
fruits.discard('apple')

print(fruits)

fruits.pop()

print(fruits)

fruits.clear()

print(fruits)
