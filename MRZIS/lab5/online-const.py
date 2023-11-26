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
    def __init__(self, input_size, hidden_size, output_size, learning_rate=0.002):
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
        error = target - output
        self.E += error[0] ** 2
        
        delta_hidden = error.dot(self.weights_hidden_output.T) * self.sigmoid_derivative(self.hidden_output)

        self.weights_hidden_output += self.hidden_output.T.dot(error) * self.learning_rate
        self.bias_output += np.sum(error, axis=0, keepdims=True) * self.learning_rate
        self.weights_input_hidden += inputs.T.dot(delta_hidden) * self.learning_rate
        self.bias_hidden += np.sum(delta_hidden, axis=0, keepdims=True) * self.learning_rate

    def train(self, inputs, targets, epochs):
        for epoch in range(epochs):
            for i in range(len(inputs)):
                input_data = np.array([inputs[i]])
                target_data = np.array([targets[i]])

                output = self.forward(input_data)
                self.backward(input_data, target_data, output)
            ERROR.append(self.E)
            self.E = 0

    def predict(self, inputs):
        output = self.forward(inputs)
        result = [el[0] for el in output]
        # return normalize_data(result, -0.3, 0.3)
        return result

def get_train_data(all_points, input_size):
    result_X = [all_points[i:i+input_size] for i in range(len(all_points) - input_size)]
    result_Y = [all_points[i] for i in range(input_size, len(all_points), 1)]
    return np.array(result_X), np.array(result_Y)

input_size = 6
hidden_size = 3
output_size = 1

all_train_points = f(np.arange(0, 200, 0.2))
all_test_points = f(np.arange(180, 380, 0.2))
X_train, Y_train = get_train_data(all_train_points, input_size)
X_test, Y_test = get_train_data(all_test_points, input_size)

NN = Network(input_size, hidden_size, output_size)
NN.train(X_train, Y_train, 150)
plt.plot(range(len(ERROR)), ERROR)
plt.show()

predicted = NN.predict(X_test)


plt.plot(np.arange(0, 200, 0.2), all_train_points)
plt.plot(np.arange(181.2, 380, 0.2), predicted)
plt.show()


