class Student():
    def __init__(self,id=None,age=None,marks=None):
        self.__id = id
        self.__age = age
        self.__marks = marks

    def validate_marks(self):
        if self.__marks >= 0 and self.__marks <= 100:
            return True
        else:
            return False

    def validate_age(self):
        if self.__age >= 20 and self.__age <= 100:
            return True
        else:
            return False

    def chk_qualification(self):
        if self.__marks >= 65 and self.__age >=20:
            return True
        else:
            return False

s1 = Student(102,22,89)
print(s1.validate_marks())
print(s1.validate_age())
print(s1.chk_qualification())