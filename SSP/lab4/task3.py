import tkinter as tk

def change_shape(shape):
    canvas.delete("all")  # Удаляем все элементы на холсте
    if shape == "Круг":
        canvas.create_oval(50, 50, 150, 150, fill="blue")
    elif shape == "Прямоугольник":
        canvas.create_rectangle(50, 50, 150, 150, fill="green")
    elif shape == "Треугольник":
        canvas.create_polygon(50, 150, 100, 50, 150, 150, fill="red")

# Создаем главное окно
root = tk.Tk()
root.title("Смена формы фигуры")

# Создаем холст для отображения фигуры
canvas = tk.Canvas(root, width=200, height=200)
canvas.pack()

# Изначально рисуем круг
canvas.create_oval(50, 50, 150, 150, fill="blue")

# Создаем кнопки для смены формы фигуры
circle_button = tk.Button(root, text="Круг", command=lambda: change_shape("Круг"))
circle_button.pack(side=tk.LEFT, padx=10)

rectangle_button = tk.Button(root, text="Прямоугольник", command=lambda: change_shape("Прямоугольник"))
rectangle_button.pack(side=tk.LEFT, padx=10)

triangle_button = tk.Button(root, text="Треугольник", command=lambda: change_shape("Треугольник"))
triangle_button.pack(side=tk.LEFT, padx=10)

root.mainloop()
