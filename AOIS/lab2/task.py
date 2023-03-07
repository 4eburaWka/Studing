import numpy as np

from math import sin
from matplotlib import pyplot as plt


f = lambda x: 4 * sin(7 * x) + 0.2


class Network:
    def __init__(self, weights=np.random.rand(4, 1)/5, T=5, a=0.01) -> None:
        self.weights = weights
        self.T = T
        self.a = a
    
    def predict(self, input: list) -> float:
        return np.sum(input @ self.weights) - self.T

    def training(self, inputs, targets, E_des=0.1) -> list:
        e = []
        for index, input in enumerate(inputs):
            prediction = self.predict(input)

            for i, w in enumerate(self.weights):
                w[0] = w[0] - self.a * (prediction - targets[index]) * input[i]
            self.T = self.T + self.a * (prediction - targets[index])

    def find_optimal_speed(self, a_min, a_max, a_h, inputs, targets, E_des=0.1):
        results = []

        self.a = a_min
        while self.a < a_max:
            results.append([self.a, *self.training(inputs, targets, E_des)])
            self.a *= a_h
            print(self.a)

            self.reset()
        
        print()
        acc = min(results, key=lambda x: x[1])
        fast = min(results, key=lambda x: x[2])
        print(
f"""
Скорость с наименьшей ошибкой: a={acc[0]}, E={acc[1]}, iter={acc[2]}
Скорость с быстрейшим обучением: a={fast[0]}, E={fast[1]}, iter={fast[2]}
""")

    def set_training_speed(self, a):
        self.a = a

    def reset(self):
        self.weights = np.random.rand(4, 1)
        self.T = 5


# ДЛЯ 30 ТОЧЕК
x_30 = [el for el in np.arange(10, 13, 0.1)] # Разбиение на 30 точек
data = [f(el) for el in x_30] # Заполнение массива реальных значений функции
inputs = np.array([data[i-4:i] for i in range(4, len(data))]) # Создание массива входных значений
targets = data[4:] # Создание массива целевых значений

x_15 = [el for el in np.arange(12.6, 14.5, 0.1)] # Разбиение на 15 точек
data2 = [f(el) for el in x_15[4:]] # Заполнение массива реальных значений функции
inputs2 = np.array([data2[i-4:i] for i in range(4, len(data2))])
print(len(inputs2))
targets2 = data2[4:] # Создание массива целевых значений

NN = Network(a=0.01)
# NN.find_optimal_speed(0.0001, 0.01, 10, inputs, targets)
E = []
E_des = 0.1
iter = 0
while True:
    iter += 1
    NN.training(inputs, targets)
    e = []
    for input, target in zip(inputs2, targets2):
        e.append((NN.predict(input) - target) ** 2)
    E = 0.5 * np.sum(e)
    if E < E_des:
        break

result = []
for input in inputs2:
    result.append(NN.predict(input))
print(len(x_30), len(data), len(x_15[:-4]), len(result))
plt.plot(x_30, data, x_15[:-4], result)
plt.show()