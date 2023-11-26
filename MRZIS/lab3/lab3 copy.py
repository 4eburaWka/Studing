import numpy as np
import random
import time
from matplotlib import pyplot as plt
E_arr = []


class SingleLayerPerceptron:
    def __init__(self, input_size, learning_rate=0.0046):
        self.input_size = input_size
        self.weights = np.random.randn(input_size)
        self.bias = np.random.randn(1)
        self.learning_rate = learning_rate
        self.start_rate = learning_rate

    def reset(self):
        global E_arr
        E_arr.clear()
        self.weights = np.random.randn(self.input_size)
        self.bias = np.random.randn(1)
        self.learning_rate = self.start_rate

    def predict(self, x):
        output = np.dot(self.weights, x) - self.bias
        return 1/(1+np.exp(-output))

    def deritivate(self, x):
        output = self.predict(x)
        return output*(1-output)

    def train_constant_learning_rate(self, X, y, epochs: int, isAdapt: bool = False):
        start_time = time.time()
        global E_arr
        for epoch in range(epochs):
            e_arr = []
            for i in range(len(X)):
                prediction = self.predict(X[i])
                error = prediction - y[i]
                e_arr.append(error)
                if isAdapt and abs(error) > 0.1E-10 and abs(self.deritivate(X[i])) > 0.1E-10:
                    delta_weights = error*self.deritivate(X[i])*np.array(X[i])
                    delta_bias = -error*self.deritivate(X[i])
                    b = 0.0
                    for j in range(len(self.weights)):
                        b += delta_weights[j]*X[i][j] - delta_bias
                    # if b < 0.1E-6: b = 0.1E-6
                    self.learning_rate = b*error / \
                        (b**2) if b*error/(b**2) <= 0.3 else 0.3
                self.weights = self.weights - \
                    self.learning_rate * error * np.array(X[i])
                self.bias = self.bias + self.learning_rate * error

            E_arr.append(np.sum(abs(np.array(e_arr))))
        end_time = time.time()
        training_time = end_time - start_time
        return training_time

    def train_batch_learning(self, X, y, epochs: int = 100, batch_size: int = 10, isAdapt: bool = False):
        start_time = time.time()
        global E_arr
        for epoch in range(epochs):
            e_arr = []
            for i in range(0, len(X), batch_size):
                X_batch = X[i:i+batch_size]
                y_batch = y[i:i+batch_size]
                predictions = []
                for x in X_batch:
                    predictions.append(self.predict(x)[0])
                errors = np.array(predictions) - np.array(y_batch)
                for err in errors:
                    e_arr.append(err)
                if isAdapt:
                    b_arr = []
                    for k in range(len(X_batch)):
                        if abs(errors[k]) < 0.1E-5:
                            errors[k] = 0.1E-5 if errors[k] >= 0 else -0.1E-5
                        deritivate = self.deritivate(X_batch[k])
                        if abs(deritivate) < 0.1E-6:
                            deritivate = 0.1E-6 if self.deritivate(
                                X_batch[k]) >= 0 else -0.1E-6
                        delta_weights = errors[k] * \
                            deritivate*np.array(X_batch[k])
                        delta_bias = -errors[k]*deritivate
                        b = 0.0
                        for j in range(len(self.weights)):
                            b += delta_weights[j]*X_batch[k][j] - delta_bias
                        if abs(b) < 0.1E-6:
                            b = 0.1E-5 if b <= 0 else -0.1E-5
                        b_arr.append(b)
                    # print("barr",b_arr,"err",errors)
                    up = 0
                    down = 0
                    for k in range(len(b_arr)):
                        up += b_arr[k]*errors[k]
                        down += b_arr[k]**2
                    self.learning_rate = up/down/10000 if up/down/10000 <= 0.3 else 0.3
                    # print("lr",self.learning_rate)
                self.weights = self.weights - \
                    self.learning_rate * np.dot(errors, X_batch)
                self.bias = self.bias + self.learning_rate * np.sum(errors)
            E_arr.append(np.sum(abs(np.array(e_arr))))
        end_time = time.time()
        training_time = end_time - start_time
        return training_time

# Генерация датасета с шумом


def generate_dataset():
    X = []
    Y = []
    for _ in range(400):
        x1 = random.uniform(-10, 10)
        x2 = 9 * x1 - 2 + random.uniform(-10, 10)
        X.append([x1, x2])
        Y.append(1 if x2 > 9*x1-2 else 0)
    for _ in range(80):
        index = int(random.uniform(0, len(Y)))
        Y[index] = 1 - Y[index]

    return X, Y

# Разделение датасета на обучающую и тестовую выборки


def split_dataset(X, y, split_ratio=0.8):
    split_index = int(len(X) * split_ratio)
    X_train = X[:split_index]
    y_train = y[:split_index]
    X_test = X[split_index:]
    y_test = y[split_index:]
    return X_train, y_train, X_test, y_test

# Расчет ошибки на тестовой выборке


def calculate_test_error(model, X_test, y_test):
    predictions = [model.predict(x) for x in X_test]
    errors = [1 if np.round(p) != y else 0 for p,
              y in zip(predictions, y_test)]
    correct_points, incorrect_points = [], []
    for i, error in enumerate(errors):
        if error:
            incorrect_points.append(X_test[i])
        else:
            correct_points.append(X_test[i])
    plt.scatter([x[0] for x in correct_points], [x[1] for x in correct_points], c='blue')
    plt.scatter([x[0] for x in incorrect_points], [x[1] for x in incorrect_points], c='red',)
    plt.show()
    test_error = sum(errors) / len(errors)
    return test_error


# Генерация датасета
X, Y = generate_dataset()

# Разделение на обучающую и тестовую выборки
X_test, Y_test = [], []
for _ in range(500):
    x1 = random.uniform(-10, 10)
    x2 = 9 * x1 - 2 + random.uniform(-10, 10)
    X_test.append([x1, x2])
    Y_test.append(1 if x2 > 9*x1-2 else 0)
epochs = 300

# Запуск обучения и оценка результатов
model = SingleLayerPerceptron(2)
training_time = model.train_constant_learning_rate(
    X, Y, epochs=epochs, isAdapt=False
)
test_error = calculate_test_error(model, X_test, Y_test)
print(training_time, "s", "/*/", test_error, "/*/", min(E_arr))
# plt.plot(range(epochs), E_arr, '-')
model.reset()
training_time = model.train_constant_learning_rate(
    X, Y, epochs=epochs, isAdapt=True
)
test_error = calculate_test_error(model, X_test, Y_test)
print(training_time, "s", "/*/", test_error, "/*/", min(E_arr))
# plt.plot(range(epochs), E_arr, '--')

model.reset()
training_time = model.train_batch_learning(X, Y, epochs=epochs, isAdapt=False)
test_error = calculate_test_error(model, X_test, Y_test)
print(training_time, "s", "/*/", test_error, "/*/", min(E_arr))
# plt.plot(range(epochs), E_arr, '-.')

model.reset()
training_time = model.train_batch_learning(X, Y, epochs=epochs, isAdapt=True)
test_error = calculate_test_error(model, X_test, Y_test)
print(training_time, "s", "/*/", test_error, "/*/", min(E_arr))
# plt.plot(range(epochs), E_arr, ':')
# plt.legend(['Online-Const', 'Online-Adapt', 'Batch-Const',
        #    'Batch-Adapt'], loc="upper right")
# plt.show()
