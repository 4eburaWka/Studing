x=[int(x) for x in "1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37".split()]
y=[int(x) for x in "0 0 0 0 0 0 1 1 2 2 3 3 3 4 5 5 6 7 7 8 9 10 11 12 12 13 13 14 15 16 17 18 19 20 21 22 23".split()]
print(x,y)

from matplotlib import pyplot as plt
plt.plot(x,y)
plt.show()