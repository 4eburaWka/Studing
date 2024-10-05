import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA


# Функция для удобства визуализации
def plot_pca(X_reduced, y):
    for class_value in np.unique(y):
        plt.scatter(X_reduced[y == class_value, 0],
                    X_reduced[y == class_value, 1],
                    label=f'Class {class_value}')
    plt.xlabel('PC1')
    plt.ylabel('PC2')
    plt.legend()
    plt.title('PCA - Проекция на плоскость первых двух главных компонент')
    plt.show()

# Функция для удобства визуализации 3д
def plot_pca_3d(X_reduced_3,y):

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    unique_classes = np.unique(y)
  
    colors = plt.get_cmap('viridis', len(unique_classes))  # Выбираем цветовую карту
    for i, class_value in enumerate(unique_classes):
        ax.scatter(X_reduced_3[y == class_value, 0],
                X_reduced_3[y == class_value, 1],
                X_reduced_3[y == class_value, 2],
                label=f'Class {class_value}',
                color=colors(i))  # Применяем цвет для текущего класса

    ax.set_xlabel('PC 1')
    ax.set_ylabel('PC 2')
    ax.set_zlabel('PC 3')

    ax.legend()

    plt.show()

data = pd.read_csv("IAD/lab1/seeds_dataset.txt", sep='\s+', header=None)


X = data.iloc[:, :-1]
y = data.iloc[:, -1]


cov_matrix = np.cov(X, rowvar=False)


eigen_values, eigen_vectors = np.linalg.eig(cov_matrix)


sorted_index = np.argsort(eigen_values)[::-1]
sorted_eigenvalue = eigen_values[sorted_index]
sorted_eigenvectors = eigen_vectors[:,sorted_index]


eigenvector_subset_2 = sorted_eigenvectors[:,0:2]
eigenvector_subset_3 = sorted_eigenvectors[:,0:3]


X_reduced_2 = np.dot(eigenvector_subset_2.transpose(), X.transpose()).transpose()
X_reduced_3 = np.dot(eigenvector_subset_3.transpose(), X.transpose()).transpose()




fig, ax = plt.subplots()
plot_pca(X_reduced_2, y)

plot_pca_3d(X_reduced_3,y)

# Визуализация результата PCA, сделанного с помощью sklearn:
pca = PCA(n_components=2) 
X_reduced_sklearn_2 = pca.fit_transform(X)

pca_3 = PCA(n_components=3) 
X_reduced_sklearn_3 = pca_3.fit_transform(X)


plot_pca(X_reduced_sklearn_2, y)

plot_pca_3d(X_reduced_sklearn_3,y)

# Вычисление потерь 
explained_variance_2 = np.sum(sorted_eigenvalue[:2]) / np.sum(sorted_eigenvalue)
print(f'Объяснённая дисперсия для 2D проекции: {explained_variance_2 * 100:.2f}%')


explained_variance_3 = np.sum(sorted_eigenvalue[:3]) / np.sum(sorted_eigenvalue)
print(f'Объяснённая дисперсия для 3D проекции: {explained_variance_3 * 100:.2f}%')