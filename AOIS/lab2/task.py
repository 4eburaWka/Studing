import numpy as np

from math import sin, pi
from matplotlib import pyplot as plt


f = lambda x: 4 * sin(7 * x) + 0.2


class Network:
    def __init__(self, weights=np.random.rand(4, 1), T=5, a=0.01) -> None:
        self.weights = weights
        self.T = T
        self.a = a
    
    def predict(self, input: list) -> float:
        return np.sum(input @ self.weights) - self.T

    def training(self, inputs, targets, E_des=0.1) -> list:
        print("Прогнозирование\t\tЦель\t\t\tОшибка")
        iter = 0
        E_arr=[]
        while True:
            e = []
            for index, input in enumerate(inputs):
                prediction = self.predict(input)
                e.append((prediction - targets[index]) ** 2)
                

                for i, w in enumerate(self.weights):
                    w[0] = w[0] - self.a * (prediction - targets[index]) * input[i]
                self.T = self.T + self.a * (prediction - targets[index])

            iter += 1
            print(prediction, targets[index], abs(prediction-targets[index]), sep='\t')
            E = 0.5 * np.sum(e)
            E_arr.append(E)
            if E_des > E:
                print("\n")
                plt.plot(list(range(iter)),E_arr)
                plt.show()
                break
        return E, iter

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


T = 2 * pi / 7 # Период функции


# ДЛЯ 30 ТОЧЕК
x_30 = [el for el in np.arange(10, 13, 0.1)] # Разбиение на 30 точек
data = [f(el) for el in x_30] # Заполнение массива реальных значений функции
inputs = np.array([data[i-4:i] for i in range(4, len(data))]) # Создание массива входных значений
targets = data[4:] # Создание массива целевых значений

NN = Network(a=0.01)
# NN.find_optimal_speed(0.0001, 0.01, 10, inputs, targets)
NN.training(inputs, targets)

result = []
x_30_2 = np.arange(12.5, 15.9, 0.1)
print("Прогнозирование\t\tЦель\t\t\tОшибка")
for i, el in enumerate(x_30_2[:-4]):
    prediction = NN.predict([f(x_30_2[i]), f(x_30_2[i+1]), f(x_30_2[i+2]), f(x_30_2[i+3])])
    result.append(prediction)
    print(prediction, f(x_30_2[i+3]+0.1), abs(prediction-f(x_30_2[i+3]+0.1)), sep='\t')
plt.plot(x_30, data, x_30_2[4:], result, "--")
plt.show()


# ДЛЯ 15 ТОЧЕК
x_15 = [el for el in np.arange(11.5, 13, 0.1)] # Разбиение на 15 точек
data2 = [f(el) for el in x_15] # Заполнение массива реальных значений функции
inputs2 = np.array([data2[i-4:i] for i in range(4, len(data2))]) # Создание массива входных значений
targets2 = data2[4:] # Создание массива целевых значений

NN2 = Network(a=0.01)
# NN.find_optimal_speed(0.0001, 0.01, 10, inputs, targets)
NN2.training(inputs2, targets2)

result2 = []
x_15_2 = np.arange(12.5, 14.4, 0.1)
print("Прогнозирование\t\tЦель\t\t\tОшибка")
for i, el in enumerate(x_15_2[:-4]):
    prediction = NN2.predict([f(x_15_2[i]), f(x_15_2[i+1]), f(x_15_2[i+2]), f(x_15_2[i+3])])
    result2.append(prediction)
    print(prediction, f(x_15_2[i+3]+0.1), abs(prediction-f(x_15_2[i+3]+0.1)), sep='\t')
plt.plot(x_15, data2, x_15_2[4:], result2, "--")
plt.show()