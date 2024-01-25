class Product():
    def __init__(self,price):
        self.price = price

    def __add__(self, other):
        return self.price + other.price

    def __sub__(self, other):
        return self.price - other.price

    def __mul__(self, other):
        return self.price * other.price

    def __truediv__(self, other):
        return self.price / other.price

    def __floordiv__(self, other):
        return self.price // other.price

    def __mod__(self, other):
        return self.price % other.price

    def __pow__(self, other):
        return self.price ** other.price

    def __it__(self, other):
        return self.price < other.price

    def __gt__(self, other):
        return self.price > other.price

    def __le__(self, other):
        return self.price <= other.price

    def __ge__(self, other):
        return self.price >= other.price

    def __eq__(self, other):
        return self.price == other.price

    def __ne__(self, other):
        return self.price < other.price

    def __it__(self, other):
        return self.price < other.price


p = Product(5)
q = Product(46)

a = [print(p+q),print(p-q),print(p/q),print(p//q),print(p*q),print(p**q),print(p%q),print(p<q),print(p>q),print(p<=q),print(p>=q),print(p==q),print(p!=q),p+q]
print(a)



