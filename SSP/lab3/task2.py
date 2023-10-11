import tkinter as tk

def select_odd():
    selected_items = listbox.curselection()
    for i in (selected_items):
        if i % 2 != 0:
            listbox.delete(i)

def select_even():
    selected_items = listbox.curselection()
    for i in (selected_items):
        if i % 2 == 0:
            item = listbox.get(i)
            listbox.delete(i)
            listbox2.insert(0, item)

def update_list():
    item = entry.get()
    listbox.insert(tk.END, item)
    entry.delete(0, tk.END)

def clear_list():
    listbox2.delete(0, tk.END)

# Создаем главное окно
root = tk.Tk()
root.title("Управление списком")

# Создаем список и добавляем элементы
listbox = tk.Listbox(root, selectmode=tk.MULTIPLE)
listbox.pack()

# Создаем флажки
odd_checkbox = tk.Checkbutton(root, text="Удалить нечетные строки", command=select_odd)
odd_checkbox.pack()

even_checkbox = tk.Checkbutton(root, text="Переместить четные строки", command=select_even)
even_checkbox.pack()

# Создаем второй список
listbox2 = tk.Listbox(root)
listbox2.pack()

# Создаем поле для ввода и кнопку для обновления списка
entry = tk.Entry(root)
entry.pack()

update_button = tk.Button(root, text="Обновить список", command=update_list)
update_button.pack()

# Кнопка для очистки второго списка
clear_button = tk.Button(root, text="Очистить второй список", command=clear_list)
clear_button.pack()

root.mainloop()
