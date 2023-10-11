import csv
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

# Загрузка данных
X, Y = [], []
with open(r"MRZIS\lab3\diabetes.csv") as file:
    reader = csv.reader(file)
    for i, row in enumerate(reader):
        X.append([float(value) for value in row[:-1]])
        Y.append(float(row[-1]))
X = np.array(X)
y = np.array(Y)


# Разбивка данных на обучающий и тестовый наборы
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Создание и обучение модели Random Forest
rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)
rf_classifier.fit(X_train, y_train)

# Прогнозирование классов на тестовом наборе данных
y_pred = rf_classifier.predict(X_test)
print(y_pred)

# Оценка точности модели
accuracy = accuracy_score(y_test, y_pred)
print(f"Точность модели: {accuracy:.2f}")

# Вывод отчета о классификации
classification_rep = classification_report(y_test, y_pred)
print("Отчет о классификации:\n", classification_rep)
