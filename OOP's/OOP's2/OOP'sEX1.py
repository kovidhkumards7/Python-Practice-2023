class Mob():
    dis = 0 #class level variable
    def __init__(self,price,brand):
        self.price = price
        self.brand = brand
        self.discount = 0

    def purchase(self):
        total = self.price - self.price * self.discount / 100
        print(f"The {self.brand} mobile of {self.price} is {total} after discount")

def enable_discount(mobList):
    for i in mobList:
        i.discount = 50
def disable_discount(mobList):
    for i in mobList:
        i.discount = 0

mob1 = Mob(45045,"bhfce")
mob2 = Mob(65,"hgd")
mob3 = Mob(7653,"df")
mob4 = Mob(765,"juy")

list = [mob1,mob2]
mob1.purchase()
enable_discount(list)
mob1.purchase()
disable_discount(list)
mob1.purchase()
print(Mob.dis)