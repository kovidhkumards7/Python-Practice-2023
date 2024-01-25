class pro():
    def __init__(self,prod,pri):
        self.prod = prod
        self.pri = pri
        print("Inside a constructor")
        print(f"the product is {self.prod} which is of {self.pri}")

    def __del__(self):
        print(f"object {self} is destroyed")

p1 = pro("fecf",545)
p2 = pro("hrf",274)
p3 = pro("rfhgdf",74684)

