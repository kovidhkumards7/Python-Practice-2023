class Car():
    color = None

class Bike():
    color = None

def change_color(veh,color):
    veh.color = color

car_1 = Car()
car_2 = Car()
car_3 = Car()

bik = Bike()

change_color(car_1,"red")
change_color(car_2,"blue")
change_color(car_3,"green")
change_color(bik,"maroon")

print(car_1.color)
print(car_2.color)
print(car_3.color)
print(bik.color)