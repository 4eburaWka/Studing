import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

class LastNameListApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Управление списком фамилий")
        
        self.last_names = []
        
        self.listbox = tk.Listbox(self.root)
        self.listbox.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.BOTH, expand=True)
        
        self.cancel_button = tk.Button(self.root, text="Завершить", command=self.root.quit)
        self.cancel_button.pack(side=tk.RIGHT, padx=10, pady=10)
        
        self.commands_frame = tk.Frame(self.root)
        self.commands_frame.pack(side=tk.LEFT, padx=10, pady=10)
        
        self.commands_label = tk.Label(self.commands_frame, text="КОМАНДЫ \n Область добавления")
        self.commands_label.pack(fill=tk.X)
        
        self.add_entry = tk.Entry(self.commands_frame)
        self.add_entry.pack(pady=5, fill=tk.X)
        
        self.add_button = tk.Button(self.commands_frame, text="Добавить", command=self.add_lastname)
        self.add_button.pack(pady=5, fill=tk.X)
        
        self.edit_button = tk.Button(self.commands_frame, text="Изменить", command=self.edit_lastname)
        self.edit_button.pack(pady=5, fill=tk.X)
        
        self.delete_button = tk.Button(self.commands_frame, text="Удалить", command=self.delete_lastname)
        self.delete_button.pack(pady=5, fill=tk.X)
        
        self.sort_button = tk.Button(self.commands_frame, text="Сортировать", command=self.sort_lastnames)
        self.sort_button.pack(pady=5, fill=tk.X)
        
    def add_lastname(self):
        lastname = self.add_entry.get()
        if lastname:
            self.last_names.append(lastname)
            self.listbox.insert(tk.END, lastname)
            self.add_entry.delete(0, tk.END)  # Очистка поля ввода после добавления фамилии
            
    def edit_lastname(self):
        selected = self.listbox.curselection()
        if selected:
            lastname = self.add_entry.get()
            if lastname:
                self.last_names[selected[0]] = lastname
                self.listbox.delete(selected[0])
                self.listbox.insert(selected[0], lastname)
                self.add_entry.delete(0, tk.END)  # Очистка поля ввода после изменения фамилии
                
    def delete_lastname(self):
        selected = self.listbox.curselection()
        if selected:
            self.listbox.delete(selected)
            del self.last_names[selected[0]]
            
    def sort_lastnames(self):
        self.last_names.sort()
        self.listbox.delete(0, tk.END)
        for lastname in self.last_names:
            self.listbox.insert(tk.END, lastname)
            
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = LastNameListApp()
    app.run()
