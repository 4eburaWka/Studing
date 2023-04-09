from math import cos, fabs
from random import uniform
from threading import Thread


while True:
    b = float(input("Введите b от [2, 10] : "))
    if 2 <= b <= 10:
        break

def f(x):
    return cos(x)+1/b*cos(8*x+1)+1/b**2*cos(8**2*x+2)+1/b**3*cos(8**3*x+3)+1/b**4*cos(8**4*x+4)
    
ress = []

res = [1]
Nmax = 10

x0 = 5#float(input("Стартовая точка : "))
a = 0.1#float(input("Введите начальный шаг : "))
amin = 0.0001

print('<#>', '<x>', '<y>', '<a>', sep='\t\t')

y0 = f(x0)
while Nmax:
    x1 = x0 + a * uniform(-1, 1)
    y1 = f(x1)

    res.append(fabs(fabs(y1)-fabs(y0)))

    if y1 < y0:
        x0, y0 = x1, y1

    print(11 - Nmax, round(x0, 4), round(y0, 4), round(a,4), sep='\t\t')
    a *= uniform(0.75, 0.999)
    if (res[-2] < 0.01 and res[-1] < 0.01) or a < amin:
        break

    Nmax -= 1
