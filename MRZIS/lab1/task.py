import csv
from matplotlib import pyplot as plt
import numpy as np


X, Y = [], []
with open(r"MRZIS\lab1\Seed_Data.csv") as file:
    reader = csv.reader(file)
    for i, row in enumerate(reader):
        X.append([float(value) for value in row[:-1]])
        Y.append([float(row[-1])])
X = np.array(X)
Y = np.array(Y)


class PCA:
    def __init__(self, n_components):
        self.n_components = n_components
        self.components = None
        self.mean = None

    def fit(self, X):
        # вычисляем среднее значение по каждому признаку
        self.mean = np.mean(X, axis=0)
        # центрируем данные
        X = X - self.mean
        # вычисляем ковариационную матрицу
        cov_matrix = np.cov(X.T)
        # вычисляем собственные векторы и собственные значения
        eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)
        # сортируем собственные векторы по убыванию собственных значений
        eigenvectors = eigenvectors.T
        idxs = np.argsort(eigenvalues)[::-1]
        eigenvectors = eigenvectors[idxs]
        # выбираем первые n_components собственных векторов
        self.components = eigenvectors[0:self.n_components]

    def transform(self, X):
        # центрируем данные
        X = X - self.mean
        # проецируем данные на главные компоненты
        return np.dot(X, self.components.T)
    

np.random.seed(0)
X = np.random.rand(10, 7)  # 10 примеров, 7 признаков

# Создаем экземпляр PCA и обучаем его на данных
pca = PCA(n_components=1)
pca.fit(X)

# Преобразуем данные в новое пространство
X_pca = pca.transform(X)

print("Original shape:", X.shape)
print("Transformed shape:", X_pca.shape)

plt.figure(figsize=(8, 4))
plt.subplot(1, 2, 1)
plt.title('Original Data')
plt.scatter(X[:, 0], X[:, 1], color='blue')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')

# Визуализация данных после PCA
plt.subplot(1, 2, 2)
plt.title('Transformed Data')
plt.scatter(X_pca, np.zeros_like(X_pca), color='red')
plt.xlabel('Principal Component 1')
plt.ylabel('Zero')

plt.tight_layout()
plt.show()