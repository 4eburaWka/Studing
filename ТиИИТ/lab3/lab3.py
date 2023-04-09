import math as m

def f(x):
    return 2.1 * x ** 3 + x - 4

e = 0.01

a = -3
b = 3

x = b
x1 = x * 2

while m.fabs(f(x1) - f(x)) > e:
    x1 = x
    x -= f(x)*(x-a)/(f(x)-f(a))
    print(x)

