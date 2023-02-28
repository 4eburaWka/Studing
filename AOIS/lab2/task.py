from math import sin, pi
from matplotlib import pyplot as plt
import numpy as np

def f(x):
    return 4 * sin(7*x)+0.2
T = 2*pi/7
x = [el for el in np.arange(1+T, 1+2*T, T/30)]
data = [f(el) for el in x]
control_values = data[4:]
print(data, len(data))
data = np.array([data[i-4:i] for i in range(4, len(data))])


print(data)