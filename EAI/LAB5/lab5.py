import tkinter as tk
from tkinter import filedialog
import spacy
from spacy import displacy

# Загрузить модель spaCy для английского языка
nlp = spacy.load("en_core_web_sm")

def analyze_syntax(text):
    # Проанализировать текст
    doc = nlp(text)

    return doc

def display_syntax(doc):
    # Очистить поле вывода
    text_box.delete("1.0", tk.END)
    displacy.render(doc)
    # Добавить зависимости в поле вывода
    for token in doc:
        
        text_box.insert("end", f"{token.text} -> {token.head.text}\n")

    text_box.insert("end", "\n")
def open_file():
    # Открыть диалоговое окно "Открыть файл"
    file_path = filedialog.askopenfilename(filetypes=[("TXT files", "*.txt")])

    if file_path:
        # Прочитать текст из файла
        
        with open(file_path, "r") as f:
            text = f.read()
        text = text.replace(',','')
        text = text.replace('.','')
        text = text.replace('?','')
        #print(text)
        # Проанализировать синтаксис текста
        doc = analyze_syntax(text)

        # Отобразить синтаксический анализ
        display_syntax(doc)

def show_help():
    # Создать новое окно для руководства
    help_window = tk.Toplevel()
    help_window.title("Руководство")

    # Добавить текст руководства
    help_text = "**Руководство по программе**\n\n" \
                "1. Нажмите кнопку \"Открыть файл\", чтобы выбрать TXT файл для анализа.\n" \
                "2. Программа проанализирует семантику текста в файле.\n" \
                "3. Результаты анализа будут отображены в поле вывода.\n" \
                "4. Нажмите кнопку \"Помощь\", чтобы открыть это руководство.\n"

    help_label = tk.Label(help_window, text=help_text)
    help_label.pack()

# Создать основное окно GUI
root = tk.Tk()
root.title("Анализ синтаксиса spaCy")

# Создать меню
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# Создать меню "Файл"
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Открыть файл", command=open_file)
file_menu.add_separator()
file_menu.add_command(label="Выход", command=root.destroy)
menu_bar.add_cascade(label="Файл", menu=file_menu)

# Создать меню "Помощь"
help_menu = tk.Menu(menu_bar, tearoff=0)
help_menu.add_command(label="Помощь", command=show_help)
menu_bar.add_cascade(label="Помощь", menu=help_menu)

# Создать поле ввода для отображения результатов
text_box = tk.Text(root)
text_box.pack()

# Запустить основное окно GUI
root.mainloop()