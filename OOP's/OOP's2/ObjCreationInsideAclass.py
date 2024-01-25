class Cus():
    def __init__(self,name,cus_type,bill):
        self.name = name
        self.cus_type = cus_type
        self.bill = bill

    def cal_bill(self):
        t1 = Tax(self.cus_type) #ObjCreationInsideAclass
        return (self.bill + self.bill * t1.tax_details(self.cus_type) / 100)
class Tax():
    def __init__(self,cus_type):
        self.cus_type = cus_type

    def tax_details(self,cus_type):
        if cus_type == "stu":
            return 5
        else:
            return 10

c1 = Cus("bc","stu",4565)
print(c1.cal_bill())
