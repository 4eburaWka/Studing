import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, mean_absolute_error

class PCA:
    def standardize_data(self, X):
        mean = np.mean(X, axis=0)
        std = np.std(X, axis=0)
        scaled_X = (X - mean) / std
        return scaled_X, mean, std

    def fit(self, X, n_components):
        # Стандартизация данных
        scaled_X, self.mean, self.std = self.standardize_data(X)
        
        # Вычисление матрицы ковариации
        covariance_matrix = np.cov(scaled_X.T)
        
        # Вычисление собственных векторов и собственных значений
        eigen_values, eigen_vectors = np.linalg.eig(covariance_matrix)
        
        # Сортировка собственных значений и векторов
        eigen_pairs = [(np.abs(eigen_values[i]), eigen_vectors[:,i]) for i in range(len(eigen_values))]
        eigen_pairs.sort(key=lambda x: x[0], reverse=True)
        
        # Выбор компонент для проекции
        self.components = np.hstack([eigen_pairs[i][1].reshape(-1,1) for i in range(n_components)])
        
        # Вычисление объясненной дисперсии
        total_variance = np.sum(eigen_values)
        self.explained_variance = [(i / total_variance) * 100 for i in eigen_values]
        
    def transform(self, X):
        # Проецирование данных на главные компоненты
        return np.dot((X - self.mean) / self.std, self.components)

    def inverse_transform(self, X_transformed):
        # Обратное преобразование PCA
        return np.dot(X_transformed, self.components.T) * self.std + self.mean
    
# Загрузка данных Seed_Data
seed_data = pd.read_csv(r"C:\Users\litvi\Documents\Studing\MRZIS\lab1\Seed_Data.csv", header=None)

# Разделение признаков и меток классов
X = seed_data.iloc[:, :-1].values  # Признаки
y = seed_data.iloc[:, -1].values   # Метки классов

pca = PCA()
pca.fit(X, n_components=3)

# Преобразование данных
X_transormed = pca.transform(X)

# Применение обратного преобразования PCA
X_reconstructed = pca.inverse_transform(X_transormed)

mse = mean_squared_error(X, X_reconstructed)
mae = mean_absolute_error(X, X_reconstructed)

print("Mean Squared Error (MSE):", mse)
print("Mean Absolute Error (MAE):", mae)

# График Scree plot
labels = ['PC' + str(x) for x in range(1, len(pca.explained_variance) + 1)]
plt.bar(x=range(1, len(pca.explained_variance) + 1), height=pca.explained_variance, tick_label=labels)
print(len(pca.explained_variance))
plt.ylabel('Percentage of Explained Variance')
plt.xlabel('Principal Component')
plt.title('Scree Plot')
plt.show()

# График PCA scatter plot
plt.scatter(-X_transormed[:, 0], -X_transormed[:, 1], c=y)
plt.title('PCA Scatter Plot (PC1 vs PC2)')
plt.xlabel('PC1 - {}%'.format(pca.explained_variance[0]))
plt.ylabel('PC2 - {}%'.format(pca.explained_variance[1]))
plt.show()
