

import pandas as pd
from sklearn.preprocessing import StandardScaler

import torch
import torch.nn as nn
import torch.optim as optim



data = pd.read_csv("IAD/lab2/seeds_dataset.txt", sep='\s+', header=None)
X = data.iloc[:, :-1].values  
y = data.iloc[:, -1].values   


scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)




class Autoencoder(nn.Module):
    def __init__(self, bottleneck_size):
        super(Autoencoder, self).__init__()
        self.encoder = nn.Sequential(
            nn.Linear(7, 64),
            nn.ReLU(),
            nn.Linear(64, bottleneck_size)  # Узкое место
        )
        self.decoder = nn.Sequential(
            nn.Linear(bottleneck_size, 64),
            nn.ReLU(),
            nn.Linear(64, 7)
        )

    def forward(self, x):
        encoded = self.encoder(x)
        decoded = self.decoder(encoded)
        return encoded, decoded


model = Autoencoder(bottleneck_size=2)  
criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

X_tensor = torch.FloatTensor(X_scaled)

num_epochs = 100
for epoch in range(num_epochs):
    optimizer.zero_grad()
    encoded, decoded = model(X_tensor)
    loss = criterion(decoded, X_tensor)
    loss.backward()
    optimizer.step()
    
    if epoch % 10 == 0:
        print(f'Epoch {epoch}, Loss: {loss.item()}')

import matplotlib.pyplot as plt


encoded_data, _ = model(X_tensor)
encoded_data = encoded_data.detach().numpy()


plt.figure(figsize=(8, 6))
plt.scatter(encoded_data[:, 0], encoded_data[:, 1], c=y, cmap='viridis')
plt.colorbar()
plt.title("Проекция автоэнкодера (2 компоненты)")
plt.show()




# t-SNE


from sklearn.manifold import TSNE


tsne = TSNE(n_components=2, perplexity=30, init='pca', random_state=42)
X_tsne = tsne.fit_transform(X_scaled)


plt.figure(figsize=(8, 6))
plt.scatter(X_tsne[:, 0], X_tsne[:, 1], c=y, cmap='viridis')
plt.colorbar()
plt.title("t-SNE (2 компоненты)")
plt.show()
