from car import Car

car1 = Car("Audi","A5",2022,"Green")
print(car1.make)
print(car1.model)
print(car1.year)
print(car1.color)
car1.drive()
car1.stop()

print("---------------------")

car2 = Car("Mustang","400",2012,"Blazing Red")
print(car2.make)
print(car2.model)
print(car2.year)
print(car2.color)

car2.drive()
car2.stop()

print(car1.wheels)
print(car2.wheels)

print(Car.wheels)
Car.wheels = 3
print(Car.wheels)

print(car1.wheels)
print(car2.wheels)