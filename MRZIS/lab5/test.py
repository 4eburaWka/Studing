import numpy as np

# Функция для применения операции свертки
def convolution(image, kernel):
    output = np.zeros_like(image)
    image_padded = np.pad(image, ((1,1),(1,1)), mode='constant')
    for x in range(image.shape[1]):
        for y in range(image.shape[0]):
            output[y,x]=(kernel*image_padded[y:y+3,x:x+3]).sum()        
    return output

# Функция для применения операции пулинга
def pooling(image, size=(2,2)):
    output = np.zeros((image.shape[0]//size[0], image.shape[1]//size[1]))
    for y in range(0, image.shape[0], size[0]):
        for x in range(0, image.shape[1], size[1]):
            output[y//size[0],x//size[1]] = np.max(image[y:y+size[0],x:x+size[1]])
    return output

# Функция для создания кодировщика
def encoder(image):
    kernel = np.array([[1, 0, -1],
                       [2, 0, -2],
                       [1, 0, -1]])
    return convolution(image, kernel)

# Функция для создания декодировщика
def decoder(image):
    kernel = np.array([[1, 1],
                       [1, 1]])
    return convolution(image, kernel)

# Функция для обучения автоенкодера
def train_autoencoder(input_data, num_epochs=10, learning_rate=0.01):
    encoded_data = encoder(input_data)
    decoded_data = decoder(encoded_data)
    loss_history = []
    for epoch in range(num_epochs):
        loss = np.mean((input_data - decoded_data)**2)
        loss_history.append(loss)
        # Обновление весов
        gradient = 2*(decoded_data - input_data)
        decoder_kernel = np.array([[1, 1],
                                   [1, 1]])
        encoder_kernel = np.array([[1, 0, -1],
                                   [2, 0, -2],
                                   [1, 0, -1]])
        decoder_kernel -= learning_rate * convolution(encoded_data, gradient)
        encoder_kernel -= learning_rate * convolution(input_data, gradient)
        decoded_data = decoder(convolution(encoded_data, decoder_kernel))
        encoded_data = encoder(input_data, encoder_kernel)
    return decoded_data, loss_history

# Пример использования
input_data = np.random.rand(28, 28) # Пример входных данных (изображение размером 28x28)
reconstructed_data, loss_history = train_autoencoder(input_data)

print("Loss history:", loss_history)
