from numpy import power as pw
from random import uniform

import math as m

def f(x, y, z):
    return y ** 2 + y * z * m.sin(x) + (x * y + 2 * y) * y ** 3
def dfdx(x,y,z):
    return pw(y, 4) + y * z * m.cos(x)
def dfdy(x, y, z):
    return 2 * y + 2 * m.sin(x) + 4 * pw(y, 3) * (x + 2)
def dfdz(x, y, z):
    return y * m.sin(x)

a = float(input("Введите стартовую точку: "))
b = float(input("Введите конечную точку: "))

h = float(input("Введите шаг: "))

x0 = uniform(a, b)
y0 = uniform(a, b)
z0 = uniform(a, b)
if input("min или max? ") == "min":
    while True:
        x1 = x0 - h * dfdx(x0, y0, z0)
        y1 = y0 - h * dfdy(x0, y0, z0)
        z1 = z0 - h * dfdz(x0, y0, z0)
        if m.fabs(x1 - x0) < 0.1:
            x0, y0, z0 = x1, y1, z1
            break
        x0, y0, z0 = x1, y1, z1
else:
    while True:
        x1 = x0 + h * dfdx(x0, y0, z0)
        y1 = y0 + h * dfdy(x0, y0, z0)
        z1 = z0 + h * dfdz(x0, y0, z0)
        if m.fabs(x1 - x0) < 0.1:
            x0, y0, z0 = x1, y1, z1
            break
        x0, y0, z0 = x1, y1, z1

print(x0,y0,z0, f(x0,y0,z0))
