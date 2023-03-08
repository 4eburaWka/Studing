xa=list(range(17))
y=[2**x for x in xa]
print(xa,y)

from matplotlib import pyplot as plt
plt.plot(xa,y)
plt.show()