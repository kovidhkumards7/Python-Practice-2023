'''
HigherOrderFunc - it is a func that either,
accepts a func as an arguement
or
returns a func(in python, funcs r also treated as objects)
'''

def loud(a):
    return a.upper()
def quite(a):
    return a.lower()

def hello(func):    #higher order func
    a = func("hello")
    print(a)

hello(loud)     #higher order func call
hello(quite)    #higher order func call

print("--------------------------")

def divisor(x):
    def dividend(y):
        return y/x
    return dividend     #higher order func return

divide = divisor(2)
print(divide(10))       #higher order func call