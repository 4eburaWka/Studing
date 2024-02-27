#3 VARIK

from threading import Thread
import pygame, keyboard
import sys
import random



# Инициализация Pygame
pygame.init()
SPACE_BTN = False

# Размеры экрана
WIDTH, HEIGHT = 800, 600

# Цвета
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Создание экрана
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Облако и капелька")

# Функция для создания капельки
def create_drop(x, y):
    return pygame.Rect(x, y, 5, 10)

drops = []
cloud_x, cloud_y = 100, 100
cloud_speed_x, cloud_speed_y = 1, 0

def event_handler():
    global drops
    while True:
        keyboard.wait('space')
        drops.append(create_drop(cloud_x + 20, cloud_y + 30))

def generate_speed():
    return random.randint(-5, 5)

clock = pygame.time.Clock()
size = 50
def resize_cloud():
    global size
    while True:
        size -= 1
        clock.tick(6)

# Основной цикл программы
def main():
    global cloud_x, cloud_y, cloud_speed_x, cloud_speed_y

    # Список для хранения капелек
    Thread(target=event_handler).start()
    Thread(target=resize_cloud).start()

    running = True
    while running:
        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:                  
                running = False                    

        # Движение облака
        cloud_x += generate_speed()
        cloud_y += generate_speed()

        # Проверка выхода облака за границы экрана
        if cloud_x < 0 or cloud_x > WIDTH - 100:
            cloud_speed_x *= -1
        if cloud_y < 0 or cloud_y > HEIGHT - 100:
            cloud_speed_y *= -1

        # Отрисовка белого фона
        screen.fill(BLACK)

        # Отрисовка облака
        pygame.draw.ellipse(screen, WHITE, (cloud_x, cloud_y, size * 2, size))

        # Движение и отрисовка капелек
        for drop in drops:
            drop.y += 5
            pygame.draw.rect(screen, BLUE, drop)
            # Удаляем капельки, которые вышли за границы экрана
            if drop.y > HEIGHT:
                drops.remove(drop)

        # Обновление экрана
        pygame.display.flip()
        clock.tick(6)

    # Завершение работы Pygame
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
