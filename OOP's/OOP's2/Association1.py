class Cus():
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def pur(self,pay):
        if pay.type == "card":
            print("payment by card")
        else:
            print("payment by other means")

class Payment():
    def __init__(self,type):
        self.type = type

p1 = Payment("card")
c1 = Cus("bfcdsh",63)   #Association Link
c1.pur(p1)