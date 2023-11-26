import numpy as np

# Генерация датасета XOR
np.random.seed(0)
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])  # входные данные
y = np.array([0, 1, 1, 0])  # выходные данные (результат XOR)

# Функция активации - сигмоида
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Производная функции активации сигмоиды
def sigmoid_derivative(x):
    return x * (1 - x)

# Настройка параметров сети
input_neurons = X.shape[1]  # количество входных нейронов
hidden_neurons = 4  # количество нейронов в скрытом слое
output_neurons = 1  # количество выходных нейронов
learning_rate = 0.1  # коэффициент обучения

# Инициализация весов сети случайными значениями
weights_input_hidden = np.random.uniform(size=(input_neurons, hidden_neurons))
weights_hidden_output = np.random.uniform(size=(hidden_neurons, output_neurons))

# Обучение нейронной сети
epochs = 10000  # количество эпох обучения

for epoch in range(epochs):
    # Прямое распространение (forward propagation)
    hidden_input = np.dot(X, weights_input_hidden)
    hidden_output = sigmoid(hidden_input)
    output_input = np.dot(hidden_output, weights_hidden_output)
    predicted_output = sigmoid(output_input)

    # Вычисление ошибки
    error = y.reshape(-1, 1) - predicted_output
    
    # Обратное распространение (backpropagation)
    # Вычисление градиентов и коррекция весов
    output_error = error * sigmoid_derivative(predicted_output)
    hidden_layer_error = output_error.dot(weights_hidden_output.T) * sigmoid_derivative(hidden_output)

    weights_hidden_output += hidden_output.T.dot(output_error) * learning_rate
    weights_input_hidden += X.T.dot(hidden_layer_error) * learning_rate

# Проверка обученной сети
test_input = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
predicted_output = sigmoid(np.dot(sigmoid(np.dot(test_input, weights_input_hidden)), weights_hidden_output))

# Вывод результатов
print("Предсказанные значения для входных данных XOR:")
print(predicted_output.ravel())
