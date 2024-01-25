class Athlete():
    def __init__(self,name,gender):
        self.__name = name
        self.__gender = gender

    def running(self):
        if self.__gender == "Female":
            print("150mts running")
        else:
            print("200mts running")

    def set_name(self,name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_gender(self,gender):
        self.__name = gender

    def get_gender(self):
        return self.__gender

a1 = Athlete("bgfhyed","Female")
a2 = Athlete("bgfhhgfyed","male")

a1.running()
a2.running()

# a1.__gender = "vcdbnju"
# print(a1.__gender)

print(a1._Athlete__gender)
print("------------")
print(a1.set_name("tguvghjvhj"))
print(a1.get_name())
print(a2.set_gender("female"))
print(a2.get_gender())