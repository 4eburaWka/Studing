import numpy as np

class Hopfield():
    def __init__(self, Y):
        Y = np.array(Y)
        self.L = Y.shape[0]
        self.I = np.eye(Y.shape[1])
        self.W = (2 * Y - 1).T @ (2 * Y - 1) - self.L * self.I
    
    def nextY(self, Y, W=None):
        if W is None:
            return np.where(Y @ self.W <= 0, 0, 1)
        return np.where(Y @ W <= 0, 0, 1)

    def sync(self, Y):
        prevY = Y
        for _ in range(10):
            Y = self.nextY(Y)
            nextY = self.nextY(Y)
            if np.allclose(Y, nextY, atol=0):
                return Y
            if np.allclose(prevY, nextY, atol=0):
                return "Not found!"
            prevY = Y
        return "Not found!"

    def async_(self, Y):
        Y = np.array(Y)
        for _ in range(10):
            list_idx = list(range(Y.shape[0]))
            np.random.shuffle(list_idx)
            for idx in list_idx:
                Y[idx] = self.nextY(Y, self.W[:, idx])
            if np.allclose(Y, self.nextY(Y, self.W), atol=0):
                return Y

            
reference_images = [
    [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1 ,1 ,1, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
]

model = Hopfield(reference_images)

Y_noise1 = [1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0] # № 2, 2 иск
Y_noise2 = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1] # № 4, 2 иск

Y_noise_async1 = model.async_(Y_noise2)
Y_noise_sync1 = model.sync(Y_noise2)

print(Y_noise_async1, " Async")
print(Y_noise_sync1, " Sync")