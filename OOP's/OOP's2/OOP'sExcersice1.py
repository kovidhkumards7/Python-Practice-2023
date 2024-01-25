class WeCare():
    def __init__(self,id,type,cost,amt=0):
        self.id = id
        self.type = type
        self.cost = cost
        self.amt = amt
        print(f"Constructor of {self.id} initiated, all vechile details r recieved for insurance premium calculation")

    def calInsurancePremium(self):
        if self.type.lower() == "two wheeler":
            self.premium = 2
        elif self.type.lower() == "four wheeler":
            self.premium = 6
        else:
            print("*****Invalid vechile type")
            return
        self.amt = self.cost * self.premium / 100
        return

    def display(self):
        print("------------------")
        print("the vechile details are :")
        print(f"{self.id}\n{self.type}\n{self.cost}\n{self.amt}")
        print("------------------")



v1 = WeCare(1,"Two wheeler",465)
v2 = WeCare(2,"Four wheeler",4814)
v3 = WeCare(3,"Foutr wheeler",476814)

v1.calInsurancePremium()
v1.display()

v2.calInsurancePremium()
v2.display()

v3.calInsurancePremium()
v3.display()
