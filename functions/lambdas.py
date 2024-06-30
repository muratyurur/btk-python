# def square(num): return num ** 3
square = lambda num: num ** 2

numbers = [1, 3, 5, 9, 10, 4]

# result = list(map(lambda num: num ** 2, numbers))
# result = list(map(square, numbers))
# result = square(3)

# def checkEven(num): return num % 2 == 0

checkEven = lambda num: num % 2 == 0

# result = list(filter(checkEven, numbers))
# result = list(filter(lambda num: num % 2 == 0, numbers))
result = list(filter(checkEven, numbers))

print(result)
