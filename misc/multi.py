class Abab:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def get_age(self):
        return self.age
    def get_name(self):
        return self.name

first = Abab('Henry', 25)

print(
    first.get_name()\
        .get_age()
)