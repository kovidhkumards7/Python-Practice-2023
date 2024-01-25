'''
Walrus_operator.py -(:=) (only in Python 3.8 n abv) assignment expression aka walrus operator
assigns values to variables as a part of a larger expression
'''

happy = True
print(happy)

print(ru_happy:="vguyjh")

# print("---------------")
# foods = list()
# while True:
#     food = input("wt food u like?: ")
#     if food == "quit":
#         break
#     foods.append(food)
# print(foods)

print("---------------using walrus oprator")
foods1 = []
while (food := input("wt food u like?: ")) != "quit":
    foods1.append(food)
print(foods1)
