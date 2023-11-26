from matplotlib import pyplot as plt
import numpy as np
import time


def f(x): return 2 * x - 3


def get_class(x, y):
    return int(y > f(x))


def make_dataset(count: int, noise_percent: int):
    train_data = [np.array([x, y]) for x, y in [(np.random.random()*4-0.5, np.random.random()*4-2)
                  for _ in range(count)]]
    train_test = [get_class(x, y) for x, y in train_data]
    for _ in range(int(count * noise_percent)):
        train_test[np.random.randint(count)] = not train_data

    return np.array(train_data), np.array(train_test)


E_arr = []
BEEE = False

class SingleLayerPerceptron:
    def __init__(self, input_size, learning_rate=0.001):
        self.input_size = input_size
        if BEEE:
            self.weights = np.array([0.95836374, 0.45664507])
        else:
            self.weights = np.random.randn(self.input_size)
        self.bias = np.random.randn(1)
        self.learning_rate = learning_rate
        self.start_rate = learning_rate

    def reset(self):
        global E_arr
        E_arr.clear()
        if BEEE:
            self.weights = np.array([0.95836374, 0.45664507])
        else:
            self.weights = np.random.randn(self.input_size)
        self.bias = np.random.randn(1)
        self.learning_rate = self.start_rate

    def predict(self, x):
        output = np.dot(self.weights, x) - self.bias
        # return int(output[0] > 0.5)
        return int(1/(1+np.exp(-output)) > 0.5)

    def deritivate(self, x):
        output = self.predict(x)
        return output*(1-output)
        # return x * (1 - x)

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
                    self.learning_rate = b*error / (b**2) if b*error/(b**2) <= 0.3 else 0.3
                self.weights -= self.learning_rate * error * np.array(X[i])
                self.bias += self.learning_rate * error
            E_arr.append(np.sum(abs(np.array(e_arr))))
            if E_arr[-1] <= 2:
                return epoch
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
                    predictions.append(self.predict(x))
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
                            deritivate * np.array(X_batch[k])
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


X_train, Y_train = make_dataset(200, 0.0)
X_test, Y_test = make_dataset(40, 0)
epochs = 250
plt.plot(range(-2, 3, 1), [f(x) for x in range(-2, 3, 1)])
plt.scatter([x[0] for x in X_train], [x[1] for x in X_train], c='blue')
plt.show()

NN = SingleLayerPerceptron(2)

################################################## [0.95836374 0.45664507]
print("CONSTANT ONLINE LEARNING")
print(NN.weights)
NN.train_constant_learning_rate(X_train, Y_train, epochs)
plt.plot(range(len(E_arr)), E_arr)
plt.show()
output = ([NN.predict(x) for x in X_test])
correct_points, incorrect_points = [], []
for i, point in enumerate(output):
    if point == Y_test[i]:
        correct_points.append(X_test[i])
    else:
        incorrect_points.append(X_test[i])
plt.plot(range(-2, 3, 1), [f(x) for x in range(-2, 3, 1)])
plt.scatter([x[0] for x in correct_points], [x[1] for x in correct_points], c='blue')
plt.scatter([x[0] for x in incorrect_points], [x[1] for x in incorrect_points], c='red')
plt.show()
NN.reset()

##################################################
print("BATCH ONLINE LEARNING")
NN.train_batch_learning(X_train, Y_train, epochs)
plt.plot(range(len(E_arr)), E_arr)
plt.show()
output = ([NN.predict(x) for x in X_test])
correct_points, incorrect_points = [], []
for i, point in enumerate(output):
    if point == Y_test[i]:
        correct_points.append(X_test[i])
    else:
        incorrect_points.append(X_test[i])
plt.plot(range(-2, 3, 1), [f(x) for x in range(-2, 3, 1)])
plt.scatter([x[0] for x in correct_points], [x[1] for x in correct_points], c='blue')
plt.scatter([x[0] for x in incorrect_points], [x[1] for x in incorrect_points], c='red')
plt.show()
NN.reset()

##################################################
print("ADAPT ONLINE LEARNING")
NN.train_constant_learning_rate(X_train, Y_train, epochs, isAdapt=True)
plt.plot(range(len(E_arr)), E_arr)
plt.show()

output = ([NN.predict(x) for x in X_test])
correct_points, incorrect_points = [], []
for i, point in enumerate(output):
    if point == Y_test[i]:
        correct_points.append(X_test[i])
    else:
        incorrect_points.append(X_test[i])
plt.plot(range(-2, 3, 1), [f(x) for x in range(-2, 3, 1)])
plt.scatter([x[0] for x in correct_points], [x[1] for x in correct_points], c='blue')
plt.scatter([x[0] for x in incorrect_points], [x[1] for x in incorrect_points], c='red')
plt.show()
NN.reset()

##################################################
print("BATCH ADAPT LEARNING")
NN.train_batch_learning(X_train, Y_train, epochs, isAdapt=True)
plt.plot(range(len(E_arr)), E_arr)
plt.show()
output = ([NN.predict(x) for x in X_test])
correct_points, incorrect_points = [], []
for i, point in enumerate(output):
    if point == Y_test[i]:
        correct_points.append(X_test[i])
    else:
        incorrect_points.append(X_test[i])
plt.plot(range(-2, 3, 1), [f(x) for x in range(-2, 3, 1)])
plt.scatter([x[0] for x in correct_points], [x[1] for x in correct_points], c='blue')
plt.scatter([x[0] for x in incorrect_points], [x[1] for x in incorrect_points], c='red')
plt.show()
NN.reset()
