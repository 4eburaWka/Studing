from math import *

xa=list(range(0,120001, 1200))
y=[x for x in xa]
print(xa,y)

from matplotlib import pyplot as plt
plt.plot(xa,y)
plt.show()