class Thing:
    pass


print(Thing)
example = Thing()
print(example)


class Thing2:
    letters = 'abc'


print(Thing2.letters)


class Thing3:
    def __init__(self):
        self.letters1 = 'xyz'


third = Thing3()
print(third.letters1)


#############################
class Element:
    def __init__(self, name, symbol, number):
        self.__name = name
        self.__symbol = symbol
        self.__number = number

    @property
    def name(self):
        return self.__name

    @property
    def symbol(self):
        return self.__symbol

    @property
    def number(self):
        return self.__number

        # def __str__(self):
        # return 'name=%s, symbol=%s, number=%s' % (self.__name, self.__symbol, self.__number)


# elm = {"name": 'Hydrogen', "symbol": "H", "number": 1}
# hydrogen = Element(**elm)
hydrogen = Element('Hydrogen', 'H', 1)
print(hydrogen.name, hydrogen.symbol, hydrogen.number)


#############################
class Bear:
    def eats(self):
        return 'berries'


class Rabbit:
    def eats(self):
        return 'clover'


class Octothorpe:
    def eats(self):
        return 'campers'


b = Bear()
r = Rabbit()
o = Octothorpe()
print(b.eats(), r.eats(), o.eats())


###################################


class Laser:
    def does(self):
        return 'disintegrate'


class Claw:
    def does(self):
        return 'crush'


class Smartphone:
    def does(self):
        return 'ring'


class Robot:
    def __init__(self):
        self.laser = Laser()
        self.claw = Claw()
        self.smartphone = Smartphone()

    def does(self):
        return '''to %s, to %s, to %s''' % (self.laser.does(), self.claw.does(), self.smartphone.does())


ten = Robot()
print(ten.does())
