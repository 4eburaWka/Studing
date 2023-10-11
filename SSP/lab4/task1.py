import tkinter as tk

def update_light():
    red_state = red_var.get()
    yellow_state = yellow_var.get()
    green_state = green_var.get()
    
    if red_state:
        canvas.itemconfig(red_light, fill="red")
    else:
        canvas.itemconfig(red_light, fill="gray")
    
    if yellow_state:
        canvas.itemconfig(yellow_light, fill="yellow")
    else:
        canvas.itemconfig(yellow_light, fill="gray")
    
    if green_state:
        canvas.itemconfig(green_light, fill="green")
    else:
        canvas.itemconfig(green_light, fill="gray")

# Создаем главное окно
root = tk.Tk()
root.title("Световая колонна")

# Создаем холст для отображения световой колонны
canvas = tk.Canvas(root, width=100, height=300)
canvas.pack()

# Создаем фигуры для световых сигналов
red_light = canvas.create_oval(30, 50, 70, 90, fill="gray")
yellow_light = canvas.create_oval(30, 120, 70, 160, fill="gray")
green_light = canvas.create_oval(30, 190, 70, 230, fill="gray")

# Создаем флажки для управления цветами
red_var = tk.BooleanVar()
red_checkbox = tk.Checkbutton(root, text="Красный", variable=red_var, command=update_light)
red_checkbox.pack()

yellow_var = tk.BooleanVar()
yellow_checkbox = tk.Checkbutton(root, text="Желтый", variable=yellow_var, command=update_light)
yellow_checkbox.pack()

green_var = tk.BooleanVar()
green_checkbox = tk.Checkbutton(root, text="Зеленый", variable=green_var, command=update_light)
green_checkbox.pack()

# Вызываем функцию обновления состояния световой колонны
update_light()

root.mainloop()
