import numpy as np
import matplotlib.pyplot as plt

a, b, c, d = 0.3, 0.1, 0.06, 0.1

num_time_steps = 110
input_size = 1
hidden_size = 12
output_size = 1
lr = 0.0073
start = 0
time_steps = np.linspace(start, start+200, num_time_steps)
data = a * np.cos(b * time_steps) + c * np.sin(d * time_steps)

class RNN:
    def __init__(self, input_size, hidden_size, output_size):
        self.hidden_size = hidden_size
        self.W_xh = np.random.randn(hidden_size, input_size) * 0.01
        self.W_hh = np.random.randn(hidden_size, hidden_size) * 0.01
        self.W_hy = np.random.randn(output_size, hidden_size) * 0.01
        self.b_h = np.random.randn(hidden_size, 1) * 0.01
        self.b_y = np.random.randn(output_size, 1) * 0.01

    def forward(self, x, h_prev):
        h_next = np.tanh(np.dot(self.W_xh, x) + np.dot(self.W_hh, h_prev) + self.b_h)
        y = np.dot(self.W_hy, h_next) + self.b_y
        return y, h_next

rnn = RNN(input_size, hidden_size, output_size)
h_prev = np.zeros((hidden_size, 1))

errors = []
for iter in range(800):
    x = data[:-1].reshape(num_time_steps - 1, 1)
    y = data[1:].reshape(num_time_steps - 1, 1)

    dW_xh, dW_hh, dW_hy = np.zeros_like(rnn.W_xh), np.zeros_like(rnn.W_hh), np.zeros_like(rnn.W_hy)
    db_h, db_y = np.zeros_like(rnn.b_h), np.zeros_like(rnn.b_y)
    dh_next = np.zeros_like(h_prev)
    total_error = 0

    for i in range(num_time_steps - 2, -1, -1):
        x_t = x[i].reshape(1, 1)
        y_t = y[i].reshape(1, 1)
        pred, h_prev = rnn.forward(x_t, h_prev)

        dy = pred - y_t
        total_error += np.sum(dy**2)
        dW_hy += np.dot(dy, h_prev.T)
        db_y += dy
        dh = np.dot(rnn.W_hy.T, dy) + dh_next
        dh_raw = (1 - h_prev * h_prev) * dh
        db_h += dh_raw
        dW_xh += np.dot(dh_raw, x_t.T)
        dW_hh += np.dot(dh_raw, h_prev.T)
        dh_next = np.dot(rnn.W_hh.T, dh_raw)
    
    print(total_error)
    errors.append(total_error)

    for dparam in [dW_xh, dW_hh, dW_hy, db_h, db_y]:
        np.clip(dparam, -7, 7, out=dparam)

    rnn.W_xh -= lr * dW_xh
    rnn.W_hh -= lr * dW_hh
    rnn.W_hy -= lr * dW_hy
    rnn.b_h -= lr * db_h
    rnn.b_y -= lr * db_y

    if total_error < 0.1:
        print(iter, total_error)
        break

x = data[:-1].reshape(num_time_steps-1, 1)

preds = []
h_prev = np.zeros((hidden_size, 1))
for i in range(num_time_steps - 1):
    x_t = x[i].reshape(1, 1)
    pred, h_prev = rnn.forward(x_t, h_prev)
    preds.append(pred.ravel()[0])

plt.plot(range(len(errors)), errors)
plt.xlabel('Iterations')
plt.ylabel('Total Error')
plt.title('Total Error over Training')
plt.show()

plt.scatter(time_steps[:-1], x.ravel(), s=10, label='original')
plt.plot(time_steps[:-1], x.ravel())

plt.scatter(time_steps[1:], preds, label='predicted')
plt.legend()
plt.show()

