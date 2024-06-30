# class
class Person:
    # class attributes
    address = 'no information'

    # constructor (yapıcı metod)
    def __init__(self, name, year):
        # object attributes
        self.name = name
        self.year = year
        print('__init__ metodu çalıştı.')

    # methods


# object (instance)
p1 = Person('Murat', 1982)
p2 = Person('Elif Birce', 2015)

# updating
p1.address = 'istanbul'
p1.address = 'istanbul'

# accessing object attributes
print(f'p1 => name: {p1.name}, year: {p1.year}, address: {p1.address}')
print(f'p2 => name: {p2.name}, year: {p2.year}, address: {p2.address}')
