from matplotlib import pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from scipy.special import expit

E = []

class Perceptron:
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
        print(self.weights_input_hidden)
        print(self.weights_hidden_output)

    def sigmoid(self, x):
        return 1 / (1 + expit(-x))

    def sigmoid_derivative(self, x):
        return x * (1 - x)

    def forward(self, inputs):
        self.hidden_input = np.dot(inputs, self.weights_input_hidden) + self.bias_hidden
        self.hidden_output = self.sigmoid(self.hidden_input)
        self.output = np.dot(self.hidden_output, self.weights_hidden_output) + self.bias_output
        return self.output

    def backward(self, inputs, target, output):
        error = target - output
        self.E += abs(error[0])
        

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
            E.append(self.E)
            self.E = 0

    def predict(self, inputs):
        output = self.forward(inputs)
        return output

if __name__ == "__main__":
    import csv

    perceptron = Perceptron(8, 3, 1)
    epochs = 100
    X, Y = [], []
    with open(r"MRZIS\lab6\diabetes.csv") as file:
        reader = csv.reader(file)
        for i, row in enumerate(reader):
            X.append([float(value) for value in row[:-1]])
            Y.append([float(row[-1])])
    X = np.array(X)
    Y = np.array(Y)
    X /= 1000

                
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
    
    perceptron.train(X_train, y_train, epochs)
    
    temp = perceptron.predict(X_test)
    y_pred = (temp>0.42).astype(int)
    accuracy = accuracy_score(y_test, y_pred)
    
    # for o, t in zip(y_pred, y_test):
    #     print(o, t)
    print(f"Точность модели: {accuracy:.2f}")
    print(classification_report(y_test, y_pred, zero_division=1))
