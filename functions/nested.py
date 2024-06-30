# def greeting(name):
#     print("hello", name)


# greeting("Murat")
# print(greeting)

# sayHello = greeting

# print(sayHello)
# print(greeting)

# greeting("Murat")
# sayHello("Murat")

# del sayHello
# print(greeting)

# encapsulation
# def outer(num1):
#     print("Outer")
#
#     def inner_increment(num1):
#         print("Inner")
#         return num1 + 1
#
#     num2 = inner_increment(num1)
#     print(num1, num2)
#
#
# outer(10)

def factorial(number):
    if not isinstance(number, int):
        raise TypeError("number must be an integer")

    if not number >= 0:
        raise ValueError("number must be zero or higher")

    def inner_factorial(number):
        if number <= 1:
            return 1

        return number * inner_factorial(number - 1)

    return inner_factorial(number)


try:
    print(factorial(1.3))
except Exception as e:
    print(e)
