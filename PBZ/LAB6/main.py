import time

import keyboard


def wait(secs):
    time.sleep(secs)

def mixing(direction, secs):
    if direction == 'A':
        print(f"Двигатель вращается в направлении А на протяжении {secs} сек")
        time.sleep(secs)
        print("Двигатель остановлен")
    elif direction == 'B':
        print(f"Двигатель вращается в направлении B на протяжении {secs} сек")
        time.sleep(secs)
        print("Двигатель остановлен")

def main_switch_on():
    print("Включен главный выключатель")
    for cycle in range(3):
        print(f"Начался цикл {cycle + 1}")
        mixing('A', 8)
        wait(3)
        mixing('B', 15)
        wait(3)
    print("Звуковой сигнал на протяжении 10 сек")

while True:
    if keyboard.is_pressed('space'):
        main_switch_on()
    elif keyboard.is_pressed('esc'):
        break