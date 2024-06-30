# # class
# class Person:
#     # class attributes
#     address = 'no information'
#
#     # constructor (yapıcı metod)
#     def __init__(self, name, year):
#         # object attributes
#         self.name = name
#         self.year = year
#
#     # methods
#     def intro(self):
#         print(f'Hello {self.name}!')
#
#     def calcAge(self):
#         return 2024 - self.year
#
#
# # object (instance)
# p1 = Person('Murat', 1982)
# p2 = Person('Elif Birce', 2015)
#
# p1.intro()
# p2.intro()
#
# print(f'ad: {p1.name} => yaş: {p1.calcAge()}')
# print(f'ad: {p2.name} => yaş: {p2.calcAge()}')

class Circle:
    # class object attribute
    pi = 3.14

    def __init__(self, yaricap=1):
        self.yaricap = yaricap

    def cevreHesapla(self):
        return 2 * self.pi * self.yaricap

    def alanHesapla(self):
        return self.pi * (self.yaricap ** 2)


c1 = Circle()
c2 = Circle(5)

print(f'c1: alan => {c1.alanHesapla()} - çevre => {c1.cevreHesapla()}')
print(f'c2: alan => {c2.alanHesapla()} - çevre => {c2.cevreHesapla()}')
