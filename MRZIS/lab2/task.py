from matplotlib import pyplot as plt
import numpy as np

# One-Class SVM реализация
class OneClassSVM:
    def __init__(self, nu=0.1, kernel='rbf', gamma=0.1):
        self.nu = nu
        self.kernel = kernel
        self.gamma = gamma

    def fit(self, X):
        n_samples, n_features = X.shape

        # Вычисляем ядро
        if self.kernel == 'linear':
            kernel_matrix = np.dot(X, X.T)
        elif self.kernel == 'rbf':
            kernel_matrix = np.exp(-self.gamma * ((X[:, np.newaxis] - X) ** 2).sum(axis=2))

        # Вычисляем опорные векторы с помощью One-Class SVM
        self.dual_coef_ = np.ones(n_samples) / n_samples
        for _ in range(50):  # Итерационный метод для оптимизации
            for i in range(n_samples):
                gradient = 1 - np.dot(self.dual_coef_ * kernel_matrix[i], self.dual_coef_ * kernel_matrix)
                self.dual_coef_[i] += self.nu * gradient[i]

            self.dual_coef_ = np.maximum(0, self.dual_coef_)

        self.support_ = np.where(self.dual_coef_ > 1e-5)[0]
        self.support_vectors_ = X[self.support_]

        # Определяем пороговое значение на основе обучающих данных
        if self.kernel == 'linear':
            self.threshold = -np.dot(self.support_vectors_, self.support_vectors_.T).sum() / n_samples
        elif self.kernel == 'rbf':
            self.threshold = -np.mean(np.exp(-self.gamma * ((X[:, np.newaxis] - self.support_vectors_) ** 2).sum(axis=2))) / (2 * self.nu)

    def decision_function(self, X):
        if self.kernel == 'linear':
            return np.dot(X, self.support_vectors_.T).sum(axis=1) + self.threshold
        elif self.kernel == 'rbf':
            return (np.exp(-self.gamma * ((X[:, np.newaxis] - self.support_vectors_) ** 2).sum(axis=2)).sum(axis=1) + self.threshold)

    def predict(self, X):
        print(self.decision_function(X))
        return (self.decision_function(X) >= 50).astype(int)


# Генерируем обучающие данные с нормальным распределением
np.random.seed(0)
mean = np.array([0, 0])
cov = np.array([[1, 0.5], [0.5, 1]])
X_train = np.random.multivariate_normal(mean, cov, 100)

x_tr, y_tr = [], []
for point in X_train:
    x_tr.append(point[0])
    y_tr.append(point[1])
plt.scatter(x_tr, y_tr)
plt.show()

# Генерируем тестовые данные случайным образом
X_test = np.random.rand(40, 2) * 6 - 3

# Обучение модели One-Class SVM
model = OneClassSVM(nu=0.1, kernel='rbf', gamma=0.1)
model.fit(X_train)

# Тестирование модели
predictions = model.predict(X_test)

x_b, y_b = [], []
x_r, y_r = [], []
for i, point in enumerate(X_test):
    if predictions[i]:
        x_b.append(point[0])
        y_b.append(point[1])
    elif not predictions[i]:
        x_r.append(point[0])
        y_r.append(point[1])

plt.scatter(x_b, y_b)
plt.scatter(x_r, y_r, c='r')
plt.show()

# Вывод результатов
print("Предсказания:")
print(predictions)
