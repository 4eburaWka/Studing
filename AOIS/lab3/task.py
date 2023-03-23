import numpy as np

class Network:
    def __init__(self, n, m, ref_img) -> None:
        self.n, self.m = n, m
        self.W = np.array(ref_img) / 2
        self.T = np.full(self.m, self.n / 2)
        Y1 = np.zeros(3)
        for i in range(self.m):
            Y1[i] = np.sum([ref_img[i][j] *  self.W[i][j] for j in range(self.n)]) - self.T[i]
        
        e = np.random.random() / 1 / self.m
        self.V = np.full((self.n, self.n), -e) # заполнить матрицу весов для НС Хопфилда е
        for i in range(self.m):
            self.V[i][i] = 1 # заполнение 1 по диагонали

    def predict(self):
        pass        
    
    def nextY(self, Y):
        return np.where(Y @ self.V <= 0, 0, 1)

    def get(self, Y):
        prevY = Y
        for _ in range(10):
            Y = self.nextY(Y)
            if np.allclose(Y, self.nextY(Y), atol=0):
                return Y
            if np.allclose(prevY, self.nextY(Y), atol=0):
                return
            prevY = Y


reference_image = [
    [1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1],
    [1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0],
    [0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1]
]

NN = Network(17, 3, reference_image)
print(NN.get([1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1]))
