def f(n):
    if n == 0:
        return 2
    elif n == 1:
        return 1
    return 2 * f(n - 1) + 2 * f(n - 2)

def ff(n):
    return round((1 + 3 ** 0.5 / 6) * (1 - 3 ** 0.5) ** n + (1 - 3 ** 0.5 / 6) * (1 + 3 ** 0.5) ** n)

def f1(n):
    if n==0:
        return 1
    elif n==1:
        return -8
    return -4*f1(n-1)-4*f1(n-2)
def f2(n):
    return -5*4**n+5*5**n
# for x in range(5):
#     print(f1(x),end=', ')
from numpy import arange
for x in arange(-100,100,0.01):
    for y in arange(-100,100,0.01):
        if (-2)**3*x+(-2)**3*y==28:
            print(x,y)