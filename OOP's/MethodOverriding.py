class Animal():
    def eat(self):
        print("eating")

class Rabbit(Animal):
    def eat(self):
        print("Rabbit is eating")

rab = Rabbit()
rab.eat()