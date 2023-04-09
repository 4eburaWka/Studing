import math
from random import uniform

i = 0
a, b, d = 1.1, 1.2, 0.001

while a <= b:
    y = 1 * a ** 3 + (1 + uniform(0, 2)) * a ** 2 + 2 * a - 7 - 7 * 8 * math.sin(8 * a)
    print(f"{round(a, 3)}  {y}")
    a += d
    i += 1
