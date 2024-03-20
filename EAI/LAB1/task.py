from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from collections import defaultdict

from striprtf.striprtf import rtf_to_text

import tkinter as tk
from tkinter import ttk, filedialog

def analyze_text(input_text):
    words = word_tokenize(input_text.lower())

    # Определяем части речи слов
    tagged_words = pos_tag(words)

    word_combinations = defaultdict(list)

    for i in range(len(tagged_words) - 1):
        word, pos = tagged_words[i]
        next_word, next_pos = tagged_words[i+1]
        
        # Учитываем только существительные и глаголы
        if pos.startswith('N') and next_pos.startswith(('N', 'V')):
            word_combinations[word].append(next_word)

    result = ""
    for word, combinations in sorted(word_combinations.items()):
        result += f"{word}: {', '.join(combinations)}\n"

    return result

def display_scrollable_text(text):
    # Создаем главное окно tkinter
    root = tk.Tk()
    root.title("Scrollable Text")

    # Создаем текстовое поле
    text_area = tk.Text(root, wrap="word", height=20, width=60)
    text_area.insert(tk.END, text)
    text_area.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Создаем вертикальную полосу прокрутки
    scrollbar = tk. Scrollbar(root, command=text_area.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    text_area.config(yscrollcommand=scrollbar.set)

    # Запускаем главный цикл обработки событий
    root.mainloop()


def main():
    root = tk.Tk()
    file_path = tk.StringVar(root)
    def ask_file_path():
        path = filedialog.askopenfilename()
        if path:
            file_path.set(path)

    file_path_btn = tk.Button(root, text="Выбрать файл", command=ask_file_path)
    file_path_btn.pack()


    def convert():
        if file_path.get():
            try:
                with open(file_path.get(), 'r', encoding='utf-8') as file:
                    text = file.read()
            except FileNotFoundError:
                print("Файл не найден.")
            if file_path.get().endswith('.rtf'):
                text = rtf_to_text(text)
            analysis_result = analyze_text(text)

            display_scrollable_text(analysis_result)

    convert_btn = tk.Button(root, text="Преобразовать", command=convert)
    convert_btn.pack()

    root.mainloop()


    # file_path = 'EAI/LAB1/file.txt'  #input("Введите путь к файлу с текстом: ")

if __name__ == "__main__":
    main()
