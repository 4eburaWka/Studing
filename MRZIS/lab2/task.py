from matplotlib import pyplot as plt
import numpy as np

# Генерация данных (нормальное распределение)
np.random.seed(0)
mean = [0, 0]  # Средние значения
cov = [[1, 0.5], [0.5, 1]]  # Ковариационная матрица
num_samples = 200  # Количество нормальных данных
normal_data = np.random.multivariate_normal(mean, cov, num_samples)

# Параметр nu контролирует долю аномалий, его можно настроить
nu = 0.05

# Обучение One-Class SVM
def train_one_class_svm(normal_data, nu):
    x_, y_ = [x[0] for x in normal_data], [y[1] for y in normal_data]
    plt.scatter(x_, y_)
    plt.show()
    num_samples, num_features = normal_data.shape

    # Вычисление среднего и дисперсии для каждой функции
    mean = np.mean(normal_data, axis=0)
    variance = np.var(normal_data, axis=0)

    # Ширина окна (сглаживающий параметр)
    width = 2.0 * np.sqrt(variance)

    # Преобразование данных
    normal_data_scaled = (normal_data - mean) / width

    # Построение матрицы Грама
    gram_matrix = np.dot(normal_data_scaled, normal_data_scaled.T)

    # Вычисление bias
    bias = -np.percentile(gram_matrix, 100.0 * nu)

    return mean, width, bias

mean, width, bias = train_one_class_svm(normal_data, nu)

# Оценка новых данных
def predict_anomalies(data, mean, width, bias):
    data_scaled = (data - mean) / width
    gram_matrix = np.dot(data_scaled, data_scaled.T)
    decision_function = gram_matrix + bias
    return decision_function

# Генерация новых данных для оценки
new_data = np.random.multivariate_normal(mean, cov, 10)  # 10 новых данных

# Добавление аномальных данных
for _ in range(5):
    new_data = np.vstack((new_data, np.random.random(2) * 10))
np.random.shuffle(new_data)

anomalies = predict_anomalies(new_data, mean, width, bias)
anomaly_scores = np.mean(anomalies, axis=1)

boolean_anomaly = anomaly_scores > 3

# Вывод графика датасета
x_, y_ = [x[0] for x in new_data], [y[1] for y in new_data]
x, y, x_anom, y_anom= [], [], [], []
for i in range(len(x_)):
    if boolean_anomaly[i]:
        x_anom.append(x_[i])
        y_anom.append(y_[i])
    else:
        x.append(x_[i])
        y.append(y_[i])
plt.scatter(x_, y_, s=20)
plt.scatter(x_anom, y_anom, s=20, c='r')
plt.show()


print("Аномальные оценки для новых данных:")
print(anomaly_scores)
