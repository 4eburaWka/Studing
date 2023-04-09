from math import cos
from threading import Thread
from function import EXtr

while True:
    b = float(input("Введите b от [2, 10] : "))
    if 2 <= b <= 10:
        break

def f(x):
    return cos(x)+1/b*cos(8*x+1)+1/b**2*cos(8**2*x+2)+1/b**3*cos(8**3*x+3)+1/b**4*cos(8**4*x+4)

results = []

for x in range(10):
    Thread(target=EXtr, args=(results, f,)).start()

print(min(results))