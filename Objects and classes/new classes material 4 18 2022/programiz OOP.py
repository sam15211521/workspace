class Person:
    "this is a person class"
    age = 10

    def greet(self):
        print('Hello')





print(Person.age)

print(Person.greet)
print(Person.__doc__)


harry = Person()

print()
print(harry.greet)

harry.greet()