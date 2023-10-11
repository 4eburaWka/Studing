import tkinter as tk

def move_left():
    canvas.move(shape, -10, 0)

def move_right():
    canvas.move(shape, 10, 0)

# Создаем главное окно
root = tk.Tk()
root.title("Движение фигуры")

# Создаем холст для отображения фигуры
canvas = tk.Canvas(root, width=300, height=200)
canvas.pack()

# Изначально рисуем фигуру (прямоугольник)
shape = canvas.create_rectangle(50, 50, 100, 100, fill="blue")

# Создаем кнопки для движения фигуры
left_button = tk.Button(root, text="Влево", command=move_left)
left_button.pack(side=tk.LEFT, padx=10)

right_button = tk.Button(root, text="Вправо", command=move_right)
right_button.pack(side=tk.LEFT, padx=10)

root.mainloop()
