import tkinter as tk
from tkinter import messagebox

win = None
all_length = 0

def add_selected_items():
    global win, all_length

    selected_items = listbox.curselection()
    selected_text = ", ".join([listbox.get(idx) for idx in selected_items])
    all_length += len(selected_text)
    
    if all_length > 100:
        if win is None:
            win = tk.Tk()
            win.title("Dialog")
            win.selected_listbox = tk.Listbox(win)
            win.selected_listbox.pack()
            for idx in range(selected_listbox.size()):
                item = selected_listbox.get(idx)
                win.selected_listbox.insert(tk.END, item)

        win.selected_listbox.insert(tk.END, selected_text)
    else:
        selected_listbox.insert(tk.END, selected_text)

root = tk.Tk()
root.title("Множественный выбор элементов")

listbox = tk.Listbox(root, selectmode=tk.MULTIPLE)
listbox.pack()

elements = ["Элемент 1", "Элемент 2", "Элемент 3", "Элемент 4", "Элемент 5"]
for element in elements:
    listbox.insert(tk.END, element)

add_button = tk.Button(root, text="Добавить выбранные", command=add_selected_items)
add_button.pack()

text_widget = tk.Text(root, height=5, width=30)
text_widget.pack()

selected_listbox = tk.Listbox(root)
selected_listbox.pack()

root.mainloop()
