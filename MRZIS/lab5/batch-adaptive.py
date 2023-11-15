from matplotlib import pyplot as plt
import numpy as np
from scipy.special import expit


f = lambda x: 0.3 * np.cos(0.1 * x) + 0.06 * np.sin(0.1 * x)

def normalize_data(data, min_val, max_val):
    min_data = np.min(data)
    max_data = np.max(data)
    normalized_data = (data - min_data) / (max_data - min_data) * (max_val - min_val) + min_val
    return normalized_data

ERROR = []

class Network:
    def __init__(self, input_size, hidden_size, output_size, learning_rate=0.03):
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size
        self.learning_rate = learning_rate
        self.E = 0

        self.weights_input_hidden = np.random.randn(self.input_size, self.hidden_size)
        self.bias_hidden = np.zeros((1, self.hidden_size))
        self.weights_hidden_output = np.random.randn(self.hidden_size, self.output_size)
        self.bias_output = np.zeros((1, self.output_size))

    def sigmoid(self, x):
        return (1 / (1 + expit(-x)))

    def sigmoid_derivative(self, x):
        return x * (1 - x)

    def forward(self, inputs):
        self.hidden_input = np.dot(inputs, self.weights_input_hidden) + self.bias_hidden
        self.hidden_output = self.sigmoid(self.hidden_input)
        self.output = np.dot(self.hidden_output, self.weights_hidden_output) + self.bias_output
        return self.output

    def backward(self, inputs, target, output):
        for i in range(len(target)):
            error = target[i] - output[i]
            self.E += np.sum(error**2)

            delta_hidden = error.dot(self.weights_hidden_output.T) * self.sigmoid_derivative(np.array([self.hidden_output[i]]))

            adaptive_learning_rate = self.learning_rate / (1 + np.sum(np.square(delta_hidden)))


            self.weights_hidden_output += np.array([self.hidden_output[i]]).T.dot(np.array([error])) * adaptive_learning_rate
            self.bias_output += np.sum(error, axis=0, keepdims=True) * adaptive_learning_rate
            self.weights_input_hidden += np.array([inputs[i]]).T.dot(delta_hidden) * adaptive_learning_rate
            self.bias_hidden += np.sum(delta_hidden, axis=0, keepdims=True) * adaptive_learning_rate

    def train(self, inputs, targets, epochs, batch_size=10):
        for epoch in range(epochs):
            for i in range(0, len(inputs), batch_size):
                batch_inputs = inputs[i:i+batch_size]
                batch_targets = targets[i:i+batch_size]

                output = self.forward(batch_inputs)
                self.backward(batch_inputs, batch_targets, output)

            self.E **= (1/len(inputs))
            ERROR.append(self.E)
            self.E = 0

    def predict(self, inputs):
        output = self.forward(inputs)
        result = [el[0] for el in output]
        return normalize_data(result, -0.3, 0.3)

def get_train_data(all_points, input_size):
    result_X = [all_points[i:i+input_size] for i in range(len(all_points) - input_size)]
    result_Y = [all_points[i] for i in range(input_size, len(all_points), 1)]
    return np.array(result_X), np.array(result_Y)

input_size = 6
hidden_size = 2
output_size = 1

all_train_points = f(np.arange(0, 200, 0.2))
all_test_points = f(np.arange(180, 380, 0.2))
X_train, Y_train = get_train_data(all_train_points, input_size)
X_test, Y_test = get_train_data(all_test_points, input_size)

NN = Network(input_size, hidden_size, output_size)
NN.train(X_train, Y_train, 30, batch_size=10)
plt.plot(range(len(ERROR)), ERROR)
plt.show()

predicted = NN.predict(X_test)

plt.plot(np.arange(0, 200, 0.2), all_train_points)
plt.plot(np.arange(181.2, 380, 0.2), predicted)
plt.show()
