import numpy as np

class Hopfield():
    def __init__(self, Y):
        self.L = Y.shape[0]
        self.I = np.eye(Y.shape[1])
        self.W = (2 * Y - 1).T @ (2 * Y - 1) - self.L * self.I
    
    def nextY(self, Y, W):
        return np.where(Y @ W <= 0, 0, 1)

    def sync(self, Y):
        temp = Y.copy()
        for i in range(20):
            Y = self.nextY(temp, self.W)
            if np.all(Y == self.nextY(Y, self.W)):
                return Y
            if np.all(temp == self.nextY(Y, self.W)):
                return
            temp = Y

    def async_(self, Y): 
        temp = Y.copy() 
        for i in range(14): 
            index = list(range(Y.shape[1])) 
            np.random.shuffle(index) 
            for i in index: 
                Y[0, i] = self.nextY(Y, self.W[:, i]) 
            if np.all(Y == temp): 
                return Y 
            else : 
                temp = Y.copy()

            
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