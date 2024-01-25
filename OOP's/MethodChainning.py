'''
METHOD-CHAINNING - calling multiple methods sequencially, each call performs an action on the same object and returns self
'''

class Car():
    def turn_On(self):
        print("starting the engine")
        return self
    def drive(self):
        print("driving")
        return self
    def brake(self):
        print("braking")
        return self
    def turn_Off(self):
        print("Engine off")
        return self

car = Car()
car.turn_On().drive().brake().turn_Off()
print("---------------")
car.brake().turn_Off()