'''
LambdaFunc - 1 line func using lambda keyword
             accpets any number of arguements but only 1 expression
'''

def dou(x):
    return x*2
print(dou(5))

double = lambda x:x*2
print(double(7))

mul = lambda x,y:x*y
print(mul(2,8))

age_chk = lambda age:True if age>18 else False
print(age_chk(15))