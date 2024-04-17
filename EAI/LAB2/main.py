import os
from nltk.tag import pos_tag
from tkinter import Tk, Button, PanedWindow, Text, filedialog, Entry, Label
import nltk
import docx2txt
from PyPDF2 import PdfFileReader
from nltk.text import ConcordanceIndex
import textract
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords
import pymorphy3
import re
from tkinter import Frame

nltk.download('wordnet')
nltk.download('stopwords')
# Создание объекта лемматизатора
lemmatizer = WordNetLemmatizer()
nltk.download('averaged_perceptron_tagger')

class CorpusManager:
    def __init__(self):
        self.corpus = []
        self.word_frequencies = {}
        self.loaded_files = []

    def load_file(self, file_path):
        _, extension = os.path.splitext(file_path)
        text = ""
        if extension == '.txt':
            with open(file_path, 'r', encoding='utf-8') as file:
                text = file.read()
        elif extension == '.rtf':
            text = textract.process(file_path, encoding='utf-8').decode('utf-8')
        elif extension == '.pdf':
            with open(file_path, 'rb') as file:
                reader = PdfFileReader(file)
                for page_num in range(reader.numPages):
                    text += reader.getPage(page_num).extractText()
        elif extension == '.docx':
            doc = docx2txt.process(file_path)
            for paragraph in doc.paragraphs:
                text += paragraph.text
        elif extension == '.doc':
            text = textract.process(file_path).decode('utf-8')

        if text:
            self.corpus.append(text)
            self.loaded_files.append(file_path)
            print(f"Файл '{file_path}' успешно загружен.")

    def tokenize_corpus(self):
        for text in self.corpus:
            tokens = word_tokenize(text.lower())
            filtered_tokens = [word for word in tokens if word not in stopwords.words('russian')]
            self.word_frequencies.update(FreqDist(filtered_tokens))

    def analyze_pos_tags(self):
        pos_tags = []
        for text in self.corpus:
            tokens = word_tokenize(text)
            pos_tags.extend(pos_tag(tokens))
        return pos_tags

# Создание экземпляра корпусного менеджера
manager = CorpusManager()

# Загрузка файла
def load_file():
    file_path = filedialog.askopenfilename(filetypes=(("Текстовые файлы", "*.txt"), ("RTF файлы", "*.rtf"),
                                                       ("PDF файлы", "*.pdf"), ("Word файлы", "*.docx;*.doc"),
                                                       ("Все файлы", "*.*")))
    if file_path:
        manager.load_file(file_path)
        text_box_left.insert('1.0', f'Загруженный текст из файла:\n{manager.corpus[-1]}\n\n')

# Функция для вывода частотных характеристик словоформ
def word_frequencies():
    manager.tokenize_corpus()
    word_freqs = manager.word_frequencies
    text_box_right.delete('1.0', 'end')  # Очистка правой области перед выводом нового результата
   # text_box_right.insert('end', 'Частотные характеристики словоформ:\n')
    for word, freq in word_freqs.items():
        if word.isalnum():  # Проверка, является ли слово словоформой (без знаков препинания)
            text_box_right.insert('end', f'{word}: {freq}\n')

# Создаем экземпляр класса MorphAnalyzer
morph = pymorphy3.MorphAnalyzer()

# Функция для вывода частотных характеристик лексем
def lemma_frequencies(manager):
    manager.tokenize_corpus()
    lemmas = [morph.parse(word)[0].normal_form for text in manager.corpus for word in word_tokenize(text)]
    filtered_lemmas = [lemma for lemma in lemmas if lemma not in stopwords.words('russian')]
    lemma_freqs = FreqDist(filtered_lemmas)
    text_box_right.delete('1.0', 'end')  # Очистка правой области перед выводом нового результата
   # text_box_right.insert('end', 'Частотные характеристики лексем:\n')
    for lemma, freq in lemma_freqs.items():
        text_box_right.insert('end', f'{lemma}: {freq}\n')

# Функция для вывода частотных характеристик грамматических категорий
def pos_tag_frequencies():
    manager.tokenize_corpus()
    pos_tags = manager.analyze_pos_tags()
    pos_tag_freqs = FreqDist(tag for _, tag in pos_tags)
    text_box_right.delete('1.0', 'end')  # Очистка правой области перед выводом нового результата
   # text_box_right.insert('end', 'Частотные характеристики грамматических категорий:\n')
    for tag, freq in pos_tag_freqs.items():
        text_box_right.insert('end', f'{tag}: {freq}\n')

# Функция для вывода лемм
def lemmas():
    manager.tokenize_corpus()
    lemmas = []
    for text in manager.corpus:
        tokens = word_tokenize(text)
        for token in tokens:
            lemma = lemmatizer.lemmatize(token.lower())
            lemmas.append(lemma)
    filtered_lemmas = [lemma for lemma in lemmas if lemma not in stopwords.words('russian')]
    unique_lemmas = set(filtered_lemmas)
    text_box_right.delete('1.0', 'end')  # Очистка правой области перед выводом нового результата
   # text_box_right.insert('end', 'Леммы:\n')
    for lemma in unique_lemmas:
        text_box_right.insert('end', f'{lemma}\n')

# Функция для вывода морфологических характеристик словоформ и их метаданных
def morphological_analysis():
    manager.tokenize_corpus()
    morphological_tags = []
    for text in manager.corpus:
        tokens = word_tokenize(text)
        morphological_tags.extend(pos_tag(tokens))
    text_box_right.delete('1.0', 'end')  # Очистка правой области перед выводом нового результата
    #text_box_right.insert('end', 'Морфологические характеристики:\n')
    for tag in morphological_tags:
        text_box_right.insert('end', f'{tag}\n')

# Функция для вывода конкордансных списков
def concordance_lists():
    manager.tokenize_corpus()
    concordance_data = []
    for text in manager.corpus:
        tokens = word_tokenize(text)
        concordance_index = ConcordanceIndex(tokens)
        for word in manager.word_frequencies:
            concordance = concordance_index.offsets(word)
            if concordance:
                concordance_data.append((word, concordance))
    text_box_right.delete('1.0', 'end')  # Очистка правой области перед выводом нового результата
    #text_box_right.insert('end', 'Конкордансные списки:\n')
    for word, concordance in concordance_data:
        text_box_right.insert('end', f'Слово: {word}, Конкордансы: {concordance}\n')

def save_text_to_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if file_path:
        text = text_box_right.get("1.0", "end-1c")
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(text)

def search_text():
    query = search_entry.get()
    text_to_search = text_box_left.get("1.0", "end-1c")
    text_box_left.tag_remove("highlight", "1.0", "end")
    if query:
        pattern = re.compile(rf"\b{re.escape(query)}\b", flags=re.IGNORECASE)
        matches = pattern.finditer(text_to_search)
        for match in matches:
            start = match.start()
            end = match.end()
            text_box_left.tag_add("highlight", f"1.0+{start}c", f"1.0+{end}c")
        text_box_left.tag_config("highlight", background="yellow")
        text_box_left.see("1.0")
    else:
        print("Введите слово для поиска.")

def filter_alphabetical():
    sorted_text = '\n'.join(sorted(text_box_right.get("1.0", "end-1c").split('\n')))
    text_box_right.delete("1.0", "end")
    text_box_right.insert("1.0", sorted_text)

def filter_word_count():
    text = text_box_right.get("1.0", "end-1c")
    word_counts = {word: text.count(word) for word in set(text.split())}
    sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
    sorted_text = '\n'.join([f"{word}: {count}" for word, count in sorted_words])
    text_box_right.delete("1.0", "end")
    text_box_right.insert("1.0", sorted_text)

# Создание графического интерфейса
root = Tk()
root.title("Корпусный менеджер")

# Создание PanedWindow для разделения окна на две области
paned_window = PanedWindow(root, orient="horizontal")
paned_window.pack(expand=True, fill="both")

# Левая область (загруженный текст)
text_box_left = Text(paned_window, height=10, width=50)
paned_window.add(text_box_left)

# Правая область (результат анализа)
text_box_right = Text(paned_window, height=10, width=50)
paned_window.add(text_box_right)

# Создание фрейма для первой колонки кнопок
left_frame = Frame(root)
left_frame.pack(side="left")

# Создание фрейма для второй колонки кнопок
right_frame = Frame(root)
right_frame.pack(side="right")

# Размещение кнопок в первой колонке
load_button = Button(left_frame, text="Загрузить файл", command=load_file, width=50)
load_button.pack()

word_freq_button = Button(left_frame, text="Частотные характеристики словоформ", command=word_frequencies, width=50)
word_freq_button.pack()

lemma_freq_button = Button(left_frame, text="Частотные характеристики лексем", command=lambda: lemma_frequencies(manager), width=50)
lemma_freq_button.pack()

pos_tag_freq_button = Button(left_frame, text="Частотные характеристики грамматических категорий", command=pos_tag_frequencies, width=50)
pos_tag_freq_button.pack()

lemma_button = Button(left_frame, text="Леммы", command=lemmas, width=50)
lemma_button.pack()

morph_analysis_button = Button(left_frame, text="Морфологический анализ", command=morphological_analysis, width=50)
morph_analysis_button.pack()

concordance_button = Button(left_frame, text="Конкордансные списки", command=concordance_lists, width=50)
concordance_button.pack()

# Размещение кнопок во второй колонке
save_button = Button(right_frame, text="Сохранить результат обработки текста", command=save_text_to_file, width=50)
save_button.pack()

search_label = Label(right_frame, text="Введите слово для поиска:")
search_label.pack()

search_entry = Entry(right_frame, width=50)
search_entry.pack()

search_button = Button(right_frame, text="Поиск", command=search_text, width=50)
search_button.pack()

alphabetical_button = Button(right_frame, text="Сортировать по алфавиту", command=filter_alphabetical, width=50)
alphabetical_button.pack()

word_count_button = Button(right_frame, text="Сортировать по количеству слов", command=filter_word_count, width=50)
word_count_button.pack()

root.mainloop()