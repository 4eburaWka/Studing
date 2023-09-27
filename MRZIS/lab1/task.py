import numpy as np
from matplotlib import pyplot as plt

class Network:
    def __init__(self) -> None:
        self.W = np.array([0.33, 0.57])
        self.T = lambda x: -3 if x >= 5.5 else -9
        self.a = 0.1
        print(self.W)

    def train(self, input_data: np.array, reference_data: np.array):
        error_arr = []
        epoch = 0
        while True:
            epoch += 1
            E = 0
            for input, reference in zip(input_data, reference_data):
                output = self.T(input @ self.W)
                error = output - reference
                self.W -= self.a * input * error
                E += abs(error)
            error_arr.append(E)
            if E == 0:
                break
            
        print(f"Всего эпох {epoch}"
              )
        plt.plot(range(len(error_arr)), error_arr)
        plt.show()
    
    def sort(self, input):
        return self.T(input @ self.W)


input_data = np.array([[4, 4], [4, 7], [7, 4], [7, 7]])
reference = np.array([-9, -9, -3, -3])

NN = Network()
NN.train(input_data, reference)
print(NN.sort(np.array([4, 4])))
print(NN.sort(np.array([4, 7])))
print(NN.sort(np.array([7, 4])))
print(NN.sort(np.array([7, 7])))
print(NN.sort(np.array([9, 9])))
print(NN.sort(np.array([-1, -1])))
print(NN.sort(np.array([8, 0])))
print(NN.sort(np.array([0, 1])))