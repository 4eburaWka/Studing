import cv2
import numpy as np


def add_noise(image, intensity=0.02):
    noisy_image = np.copy(image)

    num_salt = np.ceil(intensity * image.size * 0.5)
    num_pepper = np.ceil(intensity * image.size * 0.5)

    salt_coords = [np.random.randint(0, i - 1, int(num_salt))
                   for i in image.shape]
    noisy_image[salt_coords[0], salt_coords[1]] = 255

    pepper_coords = [np.random.randint(
        0, i - 1, int(num_pepper)) for i in image.shape]
    noisy_image[pepper_coords[0], pepper_coords[1]] = 0
    return noisy_image


def median_filter(image, window_size: int, center_x: int, center_y: int, progress_bar = None):
    filtered_image = np.copy(image)
    filtered_image = np.pad(filtered_image, ((center_y-1, window_size-center_y), (center_x-1, window_size-center_x)), mode='constant', constant_values=0)

    iter_count = image.shape[0] - window_size - 1

    for index, i in enumerate(range(image.shape[0])):
        if progress_bar is not None:
            progress_bar.config(text='#' * (index * 70 // iter_count))
            progress_bar.update()
        for j in range(image.shape[1]):

            window = [
                filtered_image[i + y][j] for y in range(-center_y+1, -center_y+1+window_size)
            ] + [
                filtered_image[i][j + x] for x in range(-center_x+1, -center_x+1+window_size) if x != 0
            ]
            
            window.sort()
            median_value = window[(len(window)-1)//2+1]
            filtered_image[i, j] = median_value

    # Удаляем первые center_y-1 строк и последние window_size-center_y строк
    filtered_image = filtered_image[center_y-1:-window_size+center_y if window_size!=center_y else image.shape[1]+center_y-1, :]
    # Удаляем первые center_x-1 столбцов и последние window_size-center_x столбцов
    filtered_image = filtered_image[:, center_x-1:-window_size+center_x if window_size!=center_x else image.shape[0]+center_x]

    return filtered_image

def median_filter2(image, window_size: int, center_x: int, center_y: int, progress_bar = None):
    filtered_image = np.copy(image)
    filtered_image = np.pad(filtered_image, ((center_y-1, window_size-center_y), (center_x-1, window_size-center_x)), mode='constant', constant_values=0)

    iter_count = image.shape[0] - window_size - 1

    for index, i in enumerate(range(center_y - 1, image.shape[0] - window_size + center_y)):
        if progress_bar is not None:
            progress_bar.config(text='#' * (index * 70 // iter_count))
            progress_bar.update()
        for j in range(center_x - 1, image.shape[1] - window_size + center_x):

            window = [
                filtered_image[i + y][j] for y in range(-center_y+1, -center_y+1+window_size)
            ] + [
                filtered_image[i][j + x] for x in range(-center_x+1, -center_x+1+window_size) if x != 0
            ]
            
            window.sort()
            median_value = window[(len(window)-1)//2+1]
            filtered_image[i, j] = median_value

    return filtered_image


if __name__ == '__main__':
    image = cv2.imread(r'C:\Users\litvi\Documents\Studing\GIIS\Lab1\img\photo.jpg', cv2.IMREAD_GRAYSCALE)

    noisy_image = add_noise(image, intensity=0.05)

    cv2.imshow('Original Image', image)
    cv2.imshow('Noisy Image', noisy_image)
    cv2.imwrite(r'C:\Users\litvi\Documents\Studing\GIIS\Lab1\img\noise.jpg', noisy_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    image = cv2.imread(r'C:\Users\litvi\Documents\Studing\GIIS\Lab1\img\noise.jpg', cv2.IMREAD_GRAYSCALE)

    window_size = 5
    center_x = 3
    center_y = 2

    filtered_image = median_filter(image, window_size, center_x, center_y)

    cv2.imshow('Original Image', image)
    cv2.imshow('Filtered Image', filtered_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
