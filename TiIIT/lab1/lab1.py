from numpy import arange
from random import uniform
from math import sqrt, fabs

def f(x):
    return x / sqrt(1 + x)

a, b = 0, 3 # Значения по ОХ
c, d = min(f(x) for x in arange(a, b, 0.01)), max(f(x) for x in arange(a, b, 0.01))

Snp = (b - a) * (d - c)  # Площадь прямоугольника

N = int(input("Введите кол-во точек: "))

n = 0
for x in range(N):
    if fabs( uniform(c, d) ) <= fabs( f(uniform(a, b)) ):
        n += 1
    
Scp = Snp * n / N  # Площадь фигуры

print(N, n, Scp, sep='\t')

