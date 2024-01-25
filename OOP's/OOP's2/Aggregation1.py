class Cus():
    def __init__(self,name,age,phNum,add):
        self.name = name
        self.age = age
        self.phNum = phNum
        self.add = add

    def view_details(self):
        print(f"The details r:\n {self.name}\n{self.age}\n{self.phNum}\n")
        print(f"The address is \n{self.add.doorNum}\n{self.add.street}\n{self.add.pinCode}------------")

    def update_add(self,add):
        self.add = add


class Address():
    def __init__(self,doorNum,street,pinCode):
        self.doorNum = doorNum
        self.street = street
        self.pinCode = pinCode


add1 = Address(454,"dws",5456)
add2 = Address(47,"hfg",54645)
add3 = Address(4367,"ad",23423)

cus1 = Cus("fbewjk",45,48641,add1)  #Aggregation Link

cus1.view_details()
cus1.update_add(add2)
cus1.view_details()