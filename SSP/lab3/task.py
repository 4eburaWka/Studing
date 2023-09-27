import tkinter as tk
from tkinter import messagebox

win = None

def add_selected_items():
    global win

    selected_items = listbox.curselection()
    selected_text = " ".join([listbox.get(idx) for idx in selected_items]) + " "
    current_text = text_widget.get("1.0", "end-1c") or (win.text_widget.get("1.0", "end-1c") if win is not None else '')
    
    if len(current_text + selected_text) > 100:
        if win is None:
            win = tk.Tk()
            win.title("Dialog")
            win.text_widget = tk.Text(win, height=15, width=90)
            win.text_widget.pack()

        text_widget.delete("1.0", "end")
        win.text_widget.insert("1.0", current_text + selected_text)
    else:
        text_widget.delete("1.0", "end")
        text_widget.insert("1.0", current_text + selected_text)

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

root.mainloop()
