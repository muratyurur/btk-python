numbers = [1, 2, 3, 4, 5]

# print(numbers[0])
# print(numbers[1])
# print(numbers[2])
# print(numbers[3])
# print(numbers[4])

for num in numbers:
    print(num)

names = ['bircoş', 'kayriş', 'buğriş']

for name in names:
    print(f"My name is {name}")

name = 'Murat Yürür'

for i in name:
    print(i)

my_tuple = [(1, 2), (1, 3), (3, 5), (5, 7)]

for a, b in my_tuple:
    print(a)

d = {'k1': 1, 'k2': 2, 'k3': 3}

for key, value in d.items():
    print(f"({key}, {value})")
