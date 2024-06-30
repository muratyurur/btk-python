liste = [1, 2, 3, 4, 5]

iterator = iter(liste)


# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
#
# for i in liste:
#     print(i)


# while True:
#     try:
#         element = next(iterator)
#         print(element)
#     except StopIteration:
#         break

class MyNumbers:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.start <= self.stop:
            x = self.start
            self.start += 1
            return x
        else:
            raise StopIteration


liste = MyNumbers(20, 50)

myiter = iter(liste)

while True:
    try:
        element = next(myiter)
        print(element)
    except StopIteration:
        break

# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))

# for x in liste:
#     print(x)
