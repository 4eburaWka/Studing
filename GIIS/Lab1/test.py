from email.mime import image
import numpy as np

a = []
for i in range(5):
    a.append([y+6*i for y in range(1, 7)])
a = np.array(a)


window_size = 3
center_x = 3
center_y = 3

image_shape = [len(a), len(a[0])]

filtered_image = a
filtered_image = np.pad(filtered_image, ((center_y-1, window_size-center_y), (center_x-1, window_size-center_x)), mode='constant', constant_values=0)
print(filtered_image)
filtered_image = filtered_image[center_y-1:-window_size+center_y if window_size!=center_y else image_shape[1]+center_y-1, :]
    # Удаляем первые center_x-1 столбцов и последние window_size-center_x столбцов
filtered_image = filtered_image[:, center_x-1:-window_size+center_x if window_size!=center_x else image_shape[0]+center_x]
print(filtered_image)
b = []
for i in range(center_y - 1, image_shape[0] - window_size + center_y):
    for j in range(center_x - 1, image_shape[1] - window_size + center_x):
        temp = [
            filtered_image[i + y][j] for y in range(-center_y+1, -center_y+1+window_size)
        ] + [
            filtered_image[i][j + x] for x in range(-center_x+1, -center_x+1+window_size) if x != 0
        ]
        median_value = temp[(len(temp)-1)//2+1]
        print(median_value)
        b.append(temp)

print(b)