import tkinter as tk

def toggle_led():
    led_state = led_var.get()
    if led_state:
        canvas.itemconfig(led, fill="green")
    else:
        canvas.itemconfig(led, fill="red")

# Создаем главное окно
root = tk.Tk()
root.title("Управление светодиодом")

# Создаем холст для отображения светодиода
canvas = tk.Canvas(root, width=100, height=100)
canvas.pack()

# Создаем светодиод (круг)
led = canvas.create_oval(30, 30, 70, 70, fill="red")

# Создаем флажок (Checkbutton) для управления светодиодом
led_var = tk.BooleanVar()
led_checkbox = tk.Checkbutton(root, text="Вкл/Выкл", variable=led_var, command=toggle_led)
led_checkbox.pack()

# Вызываем функцию переключения состояния светодиода
toggle_led()

root.mainloop()
