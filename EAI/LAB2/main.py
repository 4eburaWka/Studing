import tkinter as tk

from customtkinter import CTk as Tk, CTkButton as Button, CTkFrame as Frame

from manager import TextManager

# Создание экземпляра корпусного менеджера
manager = TextManager()
  
# Создание графического интерфейса
root = Tk()
root.title("Программа")

menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

menu_bar.add_command(label="Открыть файл", command=manager.load_file)

# Создание фрейма для первой колонки кнопок
left_frame = Frame(root)
left_frame.pack(side="left")


word_freq_button = Button(left_frame, text="Частотные характеристики словоформ", command=manager.word_frequencies_)
word_freq_button.pack(fill='x', pady=5)

lemma_freq_button = Button(left_frame, text="Частотные характеристики лексем", command=manager.lemma_frequencies)
lemma_freq_button.pack(fill='x', pady=5)

pos_tag_freq_button = Button(left_frame, text="Частотные характеристики грамматических категорий", command=manager.pos_tag_frequencies)
pos_tag_freq_button.pack(fill='x', pady=5)

lemma_button = Button(left_frame, text="Леммы", command=manager.lemmas)
lemma_button.pack(fill='x', pady=5)

morph_analysis_button = Button(left_frame, text="Морфологический анализ", command=manager.morphological_analysis)
morph_analysis_button.pack(fill='x', pady=5)

concordance_button = Button(left_frame, text="Конкордансные списки", command=manager.concordance_lists)
concordance_button.pack(fill='x', pady=5)


root.mainloop()