import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

class StringCounterApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("String Counter App")

        # Переменная для хранения количества введенных строк
        self.string_count = 0

        # Создание меню
        self.menu = tk.Menu(self.root)
        self.root.config(menu=self.menu)

        # Создание пункта меню "Ввести"
        self.input_menu = tk.Menu(self.menu)
        self.menu.add_cascade(label="Ввести", menu=self.input_menu)
        self.input_menu.add_command(label="Ввести строку", command=self.input_dialog)

        # Создание пункта меню "Вывести"
        self.output_menu = tk.Menu(self.menu)
        self.menu.add_cascade(label="Вывести", menu=self.output_menu)
        self.output_menu.add_command(label="Вывести строку", command=self.output_dialog)

        # Создание метки для вывода количества введенных строк
        self.label = tk.Label(self.root, text="Количество строк: 0")
        self.label.pack(pady=10)

    def run(self):
        self.root.mainloop()

    def input_dialog(self):
        # Диалоговое окно для ввода строки
        input_str = simpledialog.askstring("Ввод строки", "Введите строку:", show='', parent=self.root)
        if input_str:
            self.string_count += 1
            self.label.config(text=f"Количество строк: {self.string_count}")

    def output_dialog(self):
        # Окно сообщения для вывода количества введенных строк
        messagebox.showinfo("Вывод строки", f"Количество строк: {self.string_count}")

if __name__ == "__main__":
    app = StringCounterApp()
    app.run()
