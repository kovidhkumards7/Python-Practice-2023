class Animal():

    alive = True

    def eat(self):
        print("eating")

    def sleep(self):
        print("sleeping")

class Rabbit(Animal):
    def run(self):
        print("running")
class Fish(Animal):
    def swim(self):
        print("swimming")
class Hawk(Animal):
    def fly(self):
        print("flying")

rab = Rabbit()
fis = Fish()
haw = Hawk()

rab.eat()
fis.sleep()
haw.sleep()

rab.run()
fis.swim()
haw.fly()