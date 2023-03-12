import numpy as np

# Задаем параметры нейросети
input_size = 8 # размер входных данных
output_size = 12 # размер выходных данных
hidden_size = 16 # размер скрытого слоя
learning_rate = 0.01 # коэффициент скорости обучения

# Инициализируем веса нейронов
w1 = np.random.normal(size=(input_size, hidden_size))
w2 = np.random.normal(size=(hidden_size, output_size))

# Определяем функцию активации нейронов
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Определяем функцию для вычисления производной функции активации
def sigmoid_prime(x):
    return sigmoid(x) * (1 - sigmoid(x))

# Определяем функцию ошибки
def mse_loss(y_true, y_pred):
    return ((y_true - y_pred) ** 2).mean()

# Определяем функцию для обучения нейросети
def train(X, y, w1, w2, learning_rate):
    # Прямое распространение
    hidden_layer = sigmoid(np.dot(X, w1))
    output_layer = sigmoid(np.dot(hidden_layer, w2))

    # Вычисление функции ошибки
    loss = mse_loss(y, output_layer)

    # Вычисление градиентов
    output_error = (y - output_layer) * sigmoid_prime(output_layer)
    hidden_error = np.dot(output_error, w2.T) * sigmoid_prime(hidden_layer)
    output_gradient = np.dot(hidden_layer.T, output_error)
    hidden_gradient = np.dot(X.T, hidden_error)

    # Обновление весов
    w2 += learning_rate * output_gradient
    w1 += learning_rate * hidden_gradient

    return w1, w2, loss

# Обучаем нейросеть
for i in range(1000):
    # Генерируем случайные данные
    input_data = np.array([[0,1,1,0,1,1,0,0]] * 10)
    target_data = np.array([[1,0,1,0,0,0,1,1,0,1,1,0]] * 10)

    # Обновляем веса нейросети
    w1, w2, loss = train(input_data, target_data, w1, w2, learning_rate)

    # Выводим текущее значение функции ошибки
    print("Step %d, loss = %f" % (i, loss))
