class Prey():
    def flee(self):
        print("Fleeing")

class Predator():
    def hunt(self):
        print("Hunting")

class Fish(Prey,Predator):
    pass

fis = Fish()
fis.flee()
fis.hunt()