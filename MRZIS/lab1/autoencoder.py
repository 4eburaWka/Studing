import torch
import torch.nn as nn
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, mean_absolute_error

class Autoencoder(nn.Module):
    def __init__(self):
        super(Autoencoder, self).__init__()
        self.encoder = nn.Sequential(
            nn.Linear(60, 30),
            nn.ReLU(),
            nn.Linear(30, 15),
            nn.ReLU(),
            nn.Linear(15, 7),
            nn.ReLU()
        )
        self.decoder = nn.Sequential(
            nn.Linear(7, 15),
            nn.ReLU(),
            nn.Linear(15, 30),
            nn.ReLU(),
            nn.Linear(30, 60),
            nn.Sigmoid()  # Применяем сигмоид для ограничения значений в диапазоне [0, 1]
        )

    def forward(self, x):
        x = self.encoder(x)
        x = self.decoder(x)
        return x
    
data = pd.read_csv("sonar.all-data.csv", header=None)
X = data.iloc[:, :-1].values

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Конвертация данных в тензоры PyTorch
X_tensor = torch.tensor(X_scaled, dtype=torch.float32)

model = Autoencoder()
criterion = nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.003)

num_epochs = 190
for epoch in range(num_epochs):
    model.train()
    optimizer.zero_grad()
    outputs = model(X_tensor)
    loss = criterion(outputs, X_tensor)
    loss.backward()
    optimizer.step()
    
    if (epoch+1) % 10 == 0:
        print(f'Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item():.4f}')

# Применение модели для восстановления данных
model.eval()
with torch.no_grad():
    decoded_data = model(X_tensor)

# Восстановление данных и их обратное масштабирование
decoded_data = decoded_data.numpy()
decoded_data = scaler.inverse_transform(decoded_data)


mse = mean_squared_error(X, decoded_data)
# Вычисление средней абсолютной ошибки
mae = mean_absolute_error(X, decoded_data)

print("Mean Squared Error (MSE):", mse)
print("Mean Absolute Error (MAE):", mae)