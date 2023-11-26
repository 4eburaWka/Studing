import tkinter as tk
from tkinter import ttk
import pyodbc
from tkinter import messagebox
from prettytable import PrettyTable

DRIVER = "{SQL Server}"
SERVER = "VICTUS\SQLEXPRESS"
DATABASE = 'lab1'
USERNAME = 'Victus\Victus'
PASSWORD = ''
connectionString = f'DRIVER={DRIVER};SERVER={SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD}'

class DatabaseApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Database Viewer")

        # Создаем меню
        self.menu_bar = tk.Menu(root)
        root.config(menu=self.menu_bar)

        # Меню "Файл"
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Файл", menu=self.file_menu)
        self.file_menu.add_command(label="Выход", command=root.destroy)

        # Фрейм для отображения таблицы
        self.table_frame = ttk.Frame(root)
        self.table_frame.pack(pady=10)

        # Выпадающий список для выбора таблицы
        self.table_var = tk.StringVar()
        self.table_var.set("Выберите таблицу")
        self.table_dropdown = ttk.Combobox(self.table_frame, textvariable=self.table_var, state="readonly")
        self.table_dropdown.grid(row=0, column=0, padx=10, pady=10)

        # Кнопка для обновления данных
        self.refresh_button = ttk.Button(self.table_frame, text="Показать", command=self.display_table)
        self.refresh_button.grid(row=0, column=1, padx=10, pady=10)

        # Подключение к базе данных
        try:
            # self.connection = pyodbc.connect(connectionString)
            self.connection = pyodbc.connect('Driver={SQL Server};'
                      'Server=VICTUS\SQLEXPRESS;'
                      'Database=lab1;'
                      'Trusted_Connection=yes;')
            self.cursor = self.connection.cursor()
            self.populate_table_dropdown()
        except pyodbc.Error as e:
            messagebox.showerror("Ошибка подключения", f"Ошибка: {str(e)}")
            root.destroy()


        # Кнопка для добавления данных
        self.add_button = ttk.Button(root, text="Добавить", command=self.add_data)
        self.add_button.pack()

        self.del_button = ttk.Button(root, text="Удалить", command=self.del_data)
        self.del_button.pack()

        self.upd_button = ttk.Button(root, text="Изменить", command=self.upd_data)
        self.upd_button.pack()

    def add_data(self):
        def add_data_func():
            values = ", ".join([f"'{var.get()}'" for var in entries])
            query = f"INSERT INTO {selected_table} VALUES ({values})"
            print(query)
            try:
                self.cursor.execute(query)
                self.connection.commit()
                messagebox.showinfo("Успех", "Данные успешно добавлены.")
            except pyodbc.Error as e:
                messagebox.showerror("Ошибка запроса", f"Ошибка: {str(e)}")
            win.destroy()
            

        # Добавление данных в выбранную таблицу
        selected_table = self.table_var.get()
        if selected_table != "Выберите таблицу":
            columns = self.get_columns(selected_table)

            win = tk.Tk()
            win.title("Добавление данных")

            # Создание текстовых полей для ввода данных
            entries = []

            for i, label in enumerate(columns):
                ttk.Label(win, text=label).grid(row=i, column=0, padx=10, pady=5)
                entries.append(ttk.Entry(win))
                entries[-1].grid(row=i, column=1, padx=10, pady=5)

            tk.Button(win, text="Добавить", command=add_data_func).grid(row=5, column=0)

    def del_data(self):
        def del_data_func(number):
            query = f"DELETE FROM {selected_table} WHERE [{columns[0]}] = {number}"
            print(query)
            try:
                self.cursor.execute(query)
                self.connection.commit()
                messagebox.showinfo("Успех", "Данные успешно удалены.")
            except pyodbc.Error as e:
                messagebox.showerror("Ошибка запроса", f"Ошибка: {str(e)}")
            win.destroy()
        selected_table = self.table_var.get()
        if selected_table != "Выберите таблицу":
            columns = self.get_columns(selected_table)
            win = tk.Tk()
            win.title("Удалить строку")
            tk.Label(win, text="Введите номер строки:").pack()
            entry = tk.Entry(win)
            entry.pack()
            tk.Button(win, text="Удалить", command=lambda: del_data_func(entry.get())).pack()
    
    def upd_data(self):
        def upd_data_func(number):
            def upd_data_func2():
                query = f"UPDATE {selected_table}  SET [{columns[1]}] = \'{entries[1].get()}\', [{columns[2]}] = \'{entries[2].get()}\', [{columns[3]}] = \'{entries[3].get()}\' where [{columns[0]}] = {number}"
                print(query)
                try:
                    self.cursor.execute(query)
                    self.connection.commit()
                    messagebox.showinfo("Успех", "Данные успешно изменены.")
                except pyodbc.Error as e:
                    messagebox.showerror("Ошибка запроса", f"Ошибка: {str(e)}")
            query = f"SELECT * FROM {selected_table} where [{columns[0]}] = {number}"
            self.cursor.execute(query)
            values = [row for row in self.cursor.fetchone()]
            
            win2 = tk.Tk()
            win2.title("Изменение данных")

            # Создание текстовых полей для ввода данных
            entries = []

            for i, label in enumerate(columns):
                ttk.Label(win2, text=label).grid(row=i, column=0, padx=10, pady=5)
                entries.append(ttk.Entry(win2))
                entries[i].insert(0, str(values[i]).strip())
                entries[-1].grid(row=i, column=1, padx=10, pady=5)

            tk.Button(win2, text="Изменить", command=upd_data_func2).grid(row=5, column=0)
            
        selected_table = self.table_var.get()
        if selected_table != "Выберите таблицу":
            columns = self.get_columns(selected_table)
            win = tk.Tk()
            win.title("Изменить строку")
            tk.Label(win, text="Введите номер строки:").pack()
            entry = tk.Entry(win)
            entry.pack()
            tk.Button(win, text="Изменить", command=lambda: upd_data_func(entry.get())).pack()

    def get_columns(self, table_name):
        columns_query = f"SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '{table_name}'"
        self.cursor.execute(columns_query)
        return [row.COLUMN_NAME for row in self.cursor.fetchall()]

    def populate_table_dropdown(self):
        # Получаем список таблиц из базы данных
        tables = [table.table_name for table in self.cursor.tables(tableType='TABLE')]
        self.table_dropdown["values"] = tables


    def display_table(self):        
        selected_table = self.table_var.get()
        if selected_table == "Выберите таблицу":
            return
        
        table = PrettyTable(self.get_columns(selected_table))
        query = f"SELECT * FROM {selected_table}"
        self.cursor.execute(query)
        for item in self.cursor.fetchall():
            table.add_row(item)

        win = tk.Tk()
        text = tk.Label(win, text=str(table), font=("Consolas", 15))
        text.pack()
        win.mainloop()



if __name__ == "__main__":
    root = tk.Tk()
    app = DatabaseApp(root)
    root.mainloop()
