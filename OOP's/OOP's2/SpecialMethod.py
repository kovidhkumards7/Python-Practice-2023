class Pro():
    def __init__(self,name,pri):    #constructor
        self.name = name
        self.pri = pri

    def __str__(self):  #special method
        return self.name + " " + str(self.pri)

class WithoutSpecialMethod():   #WithoutSpecialMethod
    def __init__(self,val):
        self.val = val


p1 = Pro("gsd",4546)
print(p1)   #special method

print("------------------------")

w1 = WithoutSpecialMethod(541)  #WithoutSpecialMethod
print(w1)
