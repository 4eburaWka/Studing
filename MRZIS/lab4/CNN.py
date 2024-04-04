import time
import json

from sklearn.model_selection import train_test_split
from image_reader import get_labels, read_idxfile
from models import *

class CnnFromScratch:
    def __init__(self, load_weights=False):
        self.conv1 = Conv2d(1, 1, 3, 1)
        self.conv2 = Conv2d(1, 1, 2, 2, padding=1)
        self.max_pool = Maxpool2d(2, 2, padding=1)
        self.fc1 = Linear(64, 30)
        self.fc2 = Linear(30, 10)
        self.flatten = Flatten()
        self.relu = ReLU()
        self.sigmoid1 = Sigmoid()
        self.sigmoid2 = Sigmoid()
        self.softmax = Softmax()

        if load_weights:
            with open('MRZIS/lab4/4_for_danik/weights.json') as file:
                data = json.load(file)
                self.fc1.fc_w = np.array(data['fc1']['w'])
                self.fc1.fc_b = np.array(data['fc1']['b'])
                self.fc2.fc_w = np.array(data['fc2']['w'])
                self.fc2.fc_b = np.array(data['fc2']['b'])


    def __call__(self, x):
        x = self.conv1(x)
        x = self.relu(x)
        x = self.max_pool(x)
        x = self.conv2(x)
        x = self.sigmoid1(x)
        x = self.flatten.matrices2vector(x)
        x = self.fc1(x)
        x = self.sigmoid2(x)
        x = self.fc2(x)
        x = self.softmax(x)
        return x

    def backprop(self, x, lr=0.01):
        x = self.softmax.backprop(x)
        x = self.fc2.backprop(x, lr)
        x = self.sigmoid2.backprop(x)
        x = self.fc1.backprop(x, lr)
        x = self.flatten.vector2matrices(x)
        x = self.sigmoid1.backprop(x)
        x = self.conv2.backprop(x, lr)
        x = self.max_pool.backprop(x)
        x = self.relu.backprop(x)
        x = self.conv1.backprop(x, lr)

    def change_weights_file(self):
        with open('MRZIS/lab4/4_for_danik/weights.json', 'w') as file:
            data = {
                'fc1': {
                    'w': self.fc1.fc_w.tolist(),
                    'b': self.fc1.fc_b.tolist()
                },
                'fc2': {
                    'w': self.fc2.fc_w.tolist(),
                    'b': self.fc2.fc_b.tolist()
                },
            }
            json.dump(data, file)

import cv2

def train_loop(images, labels, model, criterion, print_log_freq, lr, change_weights_file):
    loss_log = []
    acc_log = []
    start_time = time.time()
    for idx in range(len(images)):
        image = images[idx]
        target = labels[idx]

        # print(target.argmax())
        # cv2.imshow('', image)
        # cv2.waitKey(0)

        pred = model([image])
        loss = criterion(target, pred)
        x = criterion.backprop(target, pred)
        model.backprop(x, lr=lr)

        loss_log.append(loss.sum())
        acc_log.append(pred.argmax() == target.argmax())
        if idx % print_log_freq == 0:
            if change_weights_file:
                model.change_weights_file()

            loss_avg = sum(loss_log[-print_log_freq:])/print_log_freq
            acc_avg = sum(acc_log[-print_log_freq:])/print_log_freq
            loop_time = time.time() - start_time
            start_time = time.time()
            print(f'Train step {idx}, Loss: {loss_avg:.5f}, '
                  f'Acc: {acc_avg:.4f}, time: {loop_time:.1f}')

def train(model, change_weights):
    imgs = read_idxfile('MRZIS/lab4/4_for_danik/train-images.idx3-ubyte') # [[0, 255, 34, ... 784], ...]
    lbls = read_idxfile('MRZIS/lab4/4_for_danik/train-labels.idx1-ubyte') # [[0, 0, 1, 0 ... 9], ...]
    
    # Поиск картинок с 1, 4, 8
    poss = []
    for i in range(len(lbls)):
        if lbls[i] in (1, 4, 8):
            poss.append(i)
    images = []
    labels = []
    for i in poss[:1000]:
        images.append(imgs[i])
        labels.append(lbls[i])
    images = np.array(images)
    labels = get_labels(np.array(labels))
        

    train_images, test_images, train_labels, test_labels = train_test_split(images, labels, test_size=0.2)
    criterion = CrossEntropyLoss()

    for epoch in range(1):
        train_loop(train_images, train_labels, model, criterion, print_log_freq=100, lr=0.04, change_weights_file=change_weights)

if __name__ == '__main__':
    model = CnnFromScratch(load_weights=True)
    train(model, change_weights=False)
        # ^ change_weights_file нужно указывать true если нужно сохранять веса в файле при обучении ^^^^^^^^^^^^^^

