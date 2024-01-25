class Cus():
    def __init__(self,name,age,phNum,add):
        self.name = name
        self.age = age
        self.phNum = phNum
        self.add = add

    def view_details(self):
        print(f"The details r:\n {self.name}\n{self.age}\n{self.phNum}\n")
        print(f"The address is \n{self.add.get_doorNum()}\n{self.add.get_street()}\n{self.add.get_pinCode()}------------")

    def update_add(self,add):
        self.add = add


class Address():
    def __init__(self,doorNum,street,pinCode):
        self.__doorNum = doorNum
        self.__street = street
        self.__pinCode = pinCode

    def set_doorNum(self,a):
        self.__doorNum = a

    def set_street(self,a):
        self.__street = a

    def set_pinCode(self,a):
        self.__pinCode = a

    def get_doorNum(self):
        return self.__doorNum

    def get_street(self):
        return self.__street

    def get_pinCode(self):
        return self.__pinCode

add1 = Address(454,"dws",5456)
add2 = Address(47,"hfg",54645)
add3 = Address(4367,"ad",23423)

cus1 = Cus("fbewjk",45,48641,add1)  #Aggregation Link

cus1.view_details()
cus1.update_add(add2)
cus1.view_details()