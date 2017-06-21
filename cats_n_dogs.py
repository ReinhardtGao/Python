class Barking:
    def bark(self):
        print('This program shows how does an animal bark')


class Cat(Barking):
    def bark(self):
        print('Miao Miao')
        return '\n'


class Dog(Barking):
    def bark(self):
        print('Wang Wang')
        return '\n'

kitty = Cat()
puppy = Dog()
print(kitty.bark())
print(puppy.bark())
