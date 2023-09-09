
class Pet:
    def __init__(self, name):
        self.name = name

    def pet_name(self):
        return self.name

    def type(self):
        return "unknown"


class Dog(Pet):
    def pet_name(self):
        return self.name + ' (Wow wow)'

    def type(self):
        return "Dog"


class Cat(Pet):
    def pet_name(self):
        return self.name + ' (Mnew mnew)'

    def type(self):
        return "Cat"


list = [Cat("Picis"), Dog("Reksis"), Pet("Piika")]


for index in range(0, len(list)):
    print(f'Animal name={list[index].pet_name()} type={list[index].type()}')
