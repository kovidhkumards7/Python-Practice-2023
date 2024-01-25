'''
Prevents a user from creating an obj of that class + comples a user to override abstract methods in a child class

Abstract class = a class which contains 1 or more abstract methods
Abstract method = a method that has a declaration but does not have an implementation
abc = "abstract base class"
'''
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass
    @abstractmethod
    def stop(self):
        pass
class Car(Vehicle):
    def go(self):
        print("u r driving the car")

    def stop(self):
        print("car stopped")
class Bike(Vehicle):
    def go(self):
        print("u r riding a bike")
    def stop(self):
        print("bike stopped")

car = Car()
bik = Bike()

car.go()
bik.go()

car.stop()
bik.stop()