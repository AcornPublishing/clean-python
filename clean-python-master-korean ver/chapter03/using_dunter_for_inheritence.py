class Person:
    def __init__(self, first_name, last_name):
        self.age = 50
        self.full_name = first_name + last_name

    def get_name(self):
        return self.full_name

class Child(Person):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.__age = 20


ch = Child("Larry", "Page")
print(ch.age)              # 50
print(ch._Child__age)      # 20