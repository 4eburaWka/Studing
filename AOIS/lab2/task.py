import numpy as np

from math import sin, pi


f = lambda x: 4 * sin(7 * x) + 0.2


class Network:
    def __init__(self, weights=np.random.rand(4, 1), T=5) -> None:
        self.weights = weights
        self.T = T
    
    def predict(self, input: list) -> float:
        return np.sum(input @ self.weights) - self.T

    def training(self, inputs, targets, E_des=0.1) -> None:
        while True:
            e = []
            for index, input in enumerate(inputs):
                prediction = self.predict(input)
                e.append((prediction - targets[index]) ** 2)

                for i, w in enumerate(self.weights):
                    w[0] = w[0] - a * (prediction - targets[index]) * input[i]
                
                self.T = self.T + a * (prediction - targets[index])

            E = 0.5 * np.sum(e)
            if E_des > E:
                break

a = 0.001
T = 2 * pi / 7 # Период функции
x = [el for el in np.arange(10, 13, 0.1)] # Разбиение на 30 точек
data = [f(el) for el in x] # Заполнение массива реальных значений функции
inputs = np.array([data[i-4:i] for i in range(4, len(data))]) # Создание массива входных данных
targets = data[4:] # Создание массива верных данных

NN = Network()
NN.training(inputs, targets)
result = NN.predict([f(50+T/30), f(50+T/15), f(50+T/10), f(50+T/7.5)])
print(result, f(50+T/6))