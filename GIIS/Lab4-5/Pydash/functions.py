import csv
import os
import numpy as np
import pygame
import numba

from config import *


def get_image_by_name(img_name):
    return pygame.transform.smoothscale(
        pygame.image.load(os.path.join("images", img_name)),
        (objects_size, objects_size),
    )

def block_map(path):
    """
    :type path: rect(screen, BLACK, (0, 0, 32, 32))
    open a csv file that contains the right level map
    """
    lvl = []
    music = ""
    with open('levels/'+path, newline='') as csvfile:
        trash = csv.reader(csvfile, delimiter=',')
        for i, row in enumerate(trash):
            if i < 19:
                lvl.append(list(map(int, row + [END])))
            if i == 19:
                music = row[0]
                break
    
    return lvl, len(lvl[0]), music


def check_collide(rect1, rect2):
    if rect1.colliderect(rect2):
        # Вычисление области перекрытия
        intersection = rect1.clip(rect2)
        
        # Вычисление площадей прямоугольников и перекрытия
        area_rect1 = rect1.width * rect1.height
        area_rect2 = rect2.width * rect2.height
        area_intersection = intersection.width * intersection.height
        
        # Вычисление процента площади перекрытия
        percentage = (area_intersection / min(area_rect1, area_rect2)) * 100
        return percentage
    else:
        return 0

def rgb_to_hex(rgb, alpha=0):
    if not alpha:
        return '#{:02x}{:02x}{:02x}'.format(*rgb)
    return '#{:02x}{:02x}{:02x}{:02}'.format(*rgb, hex(alpha)[2:])

def rgb_to_hex_arr(arr):
    res = []
    for el in arr:
        res.append('#{:02x}{:02x}{:02x}'.format(*el))
    return res

def hex_to_rgb(hex):
    res = []
    for el in hex:
        r = int(el[1:3], 16)
        g = int(el[3:5], 16)
        b = int(el[5:7], 16)
        res.append((r, g, b))
    return res




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
