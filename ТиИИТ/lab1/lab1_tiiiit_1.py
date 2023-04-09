import matplotlib.pyplot as plt
import math
from random import uniform

i = 0
a, b, d = 0, 10, 0.1

y = []
x = []
zero = []

while a <= b:
	x.append(a)
	y.append(1 * x[i] ** 3 + (1 + uniform(0,2))* x[i] ** 2 + 2 * x[i] - 7 - 7 * 8 * math.sin(8 * x[i]))
	zero.append(0)
	a += d
	i += 1

plt.plot(x, y, x, zero)
plt.show()