import tkinter as tk
from threading import Thread
from time import sleep

def inflate_ball():
    global radius
    if radius >= 10:
        radius -= 10
        canvas.coords(ball, 100 - radius, 100 - radius, 100 + radius, 100 + radius)

def enlarge_ball():
    global radius
    radius += 10
    canvas.coords(ball, 100 - radius, 100 - radius, 100 + radius, 100 + radius)

def deflate_ball():
    global radius
    while True:
        sleep(0.1)
        if radius > 10:
            radius -= 1
            canvas.coords(ball, 100 - radius, 100 - radius, 100 + radius, 100 + radius)

# Создаем главное окно
root = tk.Tk()
root.title("Надувание шарика")

# Создаем холст для отображения шарика
canvas = tk.Canvas(root, width=200, height=200)
canvas.pack()

# Изначально рисуем шарик с радиусом 50 пикселей
radius = 50
ball = canvas.create_oval(100 - radius, 100 - radius, 100 + radius, 100 + radius, fill="blue")

# Создаем кнопку для надувания шарика
inflate_button = tk.Button(root, text="Сдуть", command=inflate_ball)
inflate_button.pack()

# Создаем кнопку для увеличения радиуса
enlarge_button = tk.Button(root, text="Надуть", command=enlarge_ball)
enlarge_button.pack()

# Запускаем функцию для сдувания шарика
Thread(target=deflate_ball).start()

root.mainloop()


