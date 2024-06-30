# Inheritance (Kalıtım): Miras Alma

# Person => name, lastname, age, eat(), run(), drink()
# Student (Person), Teacher (Person)


# Animal => Dog(), Cat()

class Person():
    def __init__(self, fname, lname):
        self.firstName = fname
        self.lastName = lname
        print('Person created')

    def whoAmI(self):
        print('I am a Person!')

    def eat(self):
        print('I am eating!')


class Student(Person):
    def __init__(self, fname, lname, number):
        Person.__init__(self, fname, lname)
        self.studentNumber = number
        print('Student created')

    # override
    def whoAmI(self):
        print('I am a Student!')

    def sayHello(self):
        print(f'Hello! I an a Student')


class Teacher(Person):
    def __init__(self, fname, lname, branche):
        super().__init__(fname, lname)
        self.branche = branche

    def whoAmI(self):
        print(f'I am a {self.branche} teacher!')


p1 = Person('Murat', 'Yürür')
s1 = Student('Elif Birce', 'Yürür', 1234)
t1 = Teacher('Sadık', 'Turan', 'Python')

print(p1.firstName + ' ' + p1.lastName)
print(s1.firstName + ' ' + s1.lastName + ' ' + str(s1.studentNumber))

p1.whoAmI()
s1.whoAmI()

p1.eat()
s1.eat()

s1.sayHello()
t1.whoAmI()
