class Mob():
    __dis = 50
    def __init__(self,pri,bra):
        self.price = pri
        self.brand = bra

    @classmethod
    def purchase(self):
        total = self.price - self.price * Mob.__dis / 100
        print(f"The {self.brand} mobile of {self.price} is {total} after discount")

    @classmethod
    def get_dis(self):
        return Mob.__dis

    def set_dis(self,dis):
        Mob.__dis = dis

# mob1 = Mob(46654,"cftvh")
# mob2 = Mob(56,"hjtg")
# mob3 = Mob(445,"sdf")

# print(mob1.get_dis())
print(Mob.get_dis())
# print(Mob.__dis)