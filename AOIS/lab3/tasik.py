import numpy as np

class Network:
    def __init__(self, ref_img, m):
        self.m = m
        self.n = len(ref_img[0])
        self.W = np.array(ref_img) / 2
        self.T = np.full(self.m, self.n / 2)
        Y1 = np.zeros(self.m)
        for i in range(self.m):
            Y1[i] = np.sum([ref_img[i][j] * self.W[i][j] for j in range(self.n)]) - self.T[i]
        
        e = np.random.random() / self.m
        self.V = np.full((self.m, self.m), -e)
        np.fill_diagonal(self.V, 1)
        print(np.outer(Y1, Y1))
        self.W += np.outer(Y1, Y1) - np.eye(self.m) * self.m

    def predict(self, X, max_iter=10):
        X = np.array(X)
        for i in range(max_iter):
            X_new = np.sign(np.dot(self.W, X) - self.T)
            if np.array_equal(X_new, X):
                return X_new
            X = X_new
        return X



reference_image = [
    [1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1],
    [1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0],
    [0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1]
]

NN = Network(reference_image, 3)
test_image = [1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1]
predicted_image = NN.predict(test_image)
print(predicted_image)
