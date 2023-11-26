import tkinter as tk

from prettytable import PrettyTable
from main3 import DatabaseApp


class App(DatabaseApp):
    def __init__(self, root):
        super().__init__(root)
        self.search_value = ""

    def display_table(self):

        def choose_sort():
            def f():
                self.query += f" ORDER BY [{self.var.get()}] {'ASC' if self.var2.get() else 'DESC'}"
                win2.destroy()
            win2 = tk.Tk()
            self.var = tk.StringVar(win2, columns[0].strip())
            cb = [tk.Radiobutton(win2, text=column, variable=self.var, value=column.strip()) for column in columns]
            for el in cb:
                el.pack()
            self.var2 = tk.BooleanVar(win2, False)
            but1 = tk.Radiobutton(win2, text="По убыванию", variable=self.var2, value=False)
            but2 = tk.Radiobutton(win2, text="По возрастанию", variable=self.var2, value=True)
            but1.pack()
            but2.pack()
            win2.protocol("WM_DELETE_WINDOW", f)
        
        def show():
            table = PrettyTable(columns)
            self.cursor.execute(self.query)
            for item in self.cursor.fetchall():
                table.add_row(item)
            string = self.query + "\n\n"
            string += str(table)

            win2 = tk.Tk()
            win2.title("Отчет")
            text = tk.Label(win2, text=string, font=("Consolas", 15))
            text.pack()
            win2.mainloop()

        def choose_find():
            def f():
                self.search_value = field.get()
                self.query += f" WHERE [{var.get()}] LIKE '%{self.search_value}%'"
                win2.destroy()
            win2 = tk.Tk()
            var = tk.StringVar(win2, columns[0].strip())
            cb = [tk.Radiobutton(win2, text=column, variable=var, value=column.strip()) for column in columns]
            for el in cb:
                el.pack()
            field = tk.Entry(win2)
            field.pack()
            win2.protocol("WM_DELETE_WINDOW", f)
        
        def reset():
            self.query = f"SELECT * FROM {selected_table}"

        selected_table = self.table_var.get()
        if selected_table == "Выберите таблицу":
            return
        
        columns = self.get_columns(selected_table)
        
        table = PrettyTable()
        self.query = f"SELECT * FROM {selected_table}"

        win = tk.Tk()

        sort_btn = tk.Button(win, text="Сортировка", command=choose_sort)
        show_btn = tk.Button(win, text="Вывод", command=show)
        reset_btn = tk.Button(win, text="Сброс", command=reset)
        find_btn = tk.Button(win, text="Поиск", command=choose_find)

        sort_btn.pack()
        show_btn.pack()
        reset_btn.pack()
        find_btn.pack()

        win.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()