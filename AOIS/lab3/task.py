import numpy as np

class Network:
    def __init__(self, n, m) -> None:
        self.n, self.m = n, m

    def predict(self):
        pass

    def train(self, ref_img):
        self.W = np.array(ref_img) / 2
        self.T = np.full(self.m, self.n / 2)
        Y1 = np.zeros(3)
        for i in range(self.m):
            Y1[i] = np.sum([ref_img[i][j] *  self.W[i][j] for j in range(self.n)]) - self.T[i]
        
        e = np.random.random() / 1 / self.m
        self.V = np.full((self.m, self.m), -e) # заполнить матрицу весов для НС Хопфилда е
        for i in range(self.m):
            self.V[i][i] = 1 # заполнение 1 по диагонали
        
        print(Y1)


reference_image = [
    [1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1],
    [1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0],
    [0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1]
]

NN = Network()
NN.train(reference_image)
