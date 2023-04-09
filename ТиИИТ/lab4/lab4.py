import matplotlib.pyplot as plt
import numpy as np
xs = []
y = []
zero = []
re=[]
x0, x1, x2 = -1, 1, 3
y0, y1, y2 = 12, 3, 5

f01 = (y1 - y0) / (x1 - x0)
f12 = (y2 - y1) / (x2 - x1)
f012 = (f12 - f01) / (x2 - x0)


def P(x):
    return y2 + f12 * (x - x2) + f012 * (x - x2) * (x - x1)

for i in np.arange(-5, 5, 0.01):
    xs.append(i)
    y.append(P(i))
    zero.append(0)
for i in range(999):
    re.append(y[i])
re.append(-4)
plt.plot(xs, y,zero,re,xs,zero)
plt.show()
