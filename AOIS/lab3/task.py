import numpy as np

class Hopfield():
    def __init__(self, Y):
        self.L = Y.shape[0]
        self.I = np.eye(Y.shape[1])
        self.W = (2 * Y - 1).T @ (2 * Y - 1) - self.L * self.I
    
    def nextY(self, Y, W):
        return np.where(Y @ W <= 0, 0, 1)

    def sync(self, Y):
        prevY = Y
        for _ in range(14):
            Y = self.nextY(Y, self.W)
            if np.allclose(Y, self.nextY(Y, self.W), atol=0):
                return Y
            if np.allclose(prevY, self.nextY(Y, self.W), atol=0):
                return
            prevY = Y

    def async_(self, Y):
        for _ in range(14):
            list_idx = list(range(Y.shape[1]))
            np.random.shuffle(list_idx)
            for idx in list_idx:
                Y[0, idx] = self.nextY(Y, self.W[:, idx])
            if np.allclose(Y, self.nextY(Y, self.W), atol=0):
                return Y

            
reference_images = np.array([
    [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
])

model = Hopfield(reference_images)

Y_noise1 = np.array([[1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0]]) # № 1, 4 иск
Y_noise2 = np.array([[1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]]) # № 4, 2 иск

Y_noise_async1 = model.async_(Y_noise1)
Y_noise_sync1 = model.sync(Y_noise1)

Y_noise_async2 = model.async_(Y_noise2)
Y_noise_sync2 = model.sync(Y_noise2)

print(Y_noise_async1, " Async")
print(Y_noise_sync1, " Sync")
print()

print(Y_noise_async2, " Async")
print(Y_noise_sync2, " Sync")