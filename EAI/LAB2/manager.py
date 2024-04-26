import os
from tkinter import filedialog
import pymorphy3
import nltk
import tkinter as tk

from nltk.tag import pos_tag
from nltk.text import ConcordanceIndex
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords

nltk.download('wordnet')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')


lemmatizer = WordNetLemmatizer()
morph = pymorphy3.MorphAnalyzer()

class TextManager:
    def __init__(self):
        self.corpus = []
        self.word_frequencies = {}
        self.loaded_files = []
        self.text = ""

    def _show_info(self, text):
        root = tk.Tk()
        root.title("Info")

        text_area = tk.Text(root, wrap="word", height=20, width=60)
        text_area.insert(tk.END, text)
        text_area.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(root, command=text_area.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        text_area.config(yscrollcommand=scrollbar.set)

        root.mainloop()

    def load_file(self):
        file_path = filedialog.askopenfilename(filetypes=(("Текстовые файлы", "*.txt"),
                                                       ("Все файлы", "*.*")))
        _, extension = os.path.splitext(file_path)
        text = ""
        if extension == '.txt':
            with open(file_path, 'r', encoding='utf-8') as file:
                text = file.read()

        if text:
            self.corpus.append(text)
            self.loaded_files.append(file_path)

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
    
    def word_frequencies_(self):
        self.tokenize_corpus()
        word_freqs = self.word_frequencies
        string = ""
        for word, freq in word_freqs.items():
            if word.isalnum():  # Проверка, является ли слово словоформой (без знаков препинания)
                string += f'{word}: {freq}\n'
        self._show_info(string)

    # Функция для вывода частотных характеристик лексем
    def lemma_frequencies(self):
        self.tokenize_corpus()
        lemmas = [morph.parse(word)[0].normal_form for text in self.corpus for word in word_tokenize(text)]
        filtered_lemmas = [lemma for lemma in lemmas if lemma not in stopwords.words('russian')]
        lemma_freqs = FreqDist(filtered_lemmas)
        string = ""
        for lemma, freq in lemma_freqs.items():
            string += f'{lemma}: {freq}\n'

        self._show_info(string)
    
    # Функция для вывода частотных характеристик грамматических категорий
    def pos_tag_frequencies(self):
        self.tokenize_corpus()
        pos_tags = self.analyze_pos_tags()
        pos_tag_freqs = FreqDist(tag for _, tag in pos_tags)
        string = ""
        for tag, freq in pos_tag_freqs.items():
            if tag not in ('.', ','):
                string += f'{tag}: {freq}\n'
        
        self._show_info(string)
    
    # Функция для вывода лемм
    def lemmas(self):
        self.tokenize_corpus()
        lemmas = []
        for text in self.corpus:
            tokens = word_tokenize(text)
            for token in tokens:
                lemma = lemmatizer.lemmatize(token.lower())
                lemmas.append(lemma)
        filtered_lemmas = [lemma for lemma in lemmas if lemma not in stopwords.words('russian')]
        unique_lemmas = set(filtered_lemmas)
        string = ""
        for lemma in unique_lemmas:
            string += f'{lemma}\n'
        self._show_info(string)
    
    # Функция для вывода морфологических характеристик словоформ и их метаданных
    def morphological_analysis(self):
        self.tokenize_corpus()
        morphological_tags = []
        for text in self.corpus:
            tokens = word_tokenize(text)
            morphological_tags.extend(pos_tag(tokens))
        string = ""
        for tag in morphological_tags:
            if tag[0] not in ('.', ','):
                string += f'{tag}\n'
        self._show_info(string)
    
    # Функция для вывода конкордансных списков
    def concordance_lists(self):
        self.tokenize_corpus()
        concordance_data = []
        for text in self.corpus:
            tokens = word_tokenize(text)
            concordance_index = ConcordanceIndex(tokens)
            for word in self.word_frequencies:
                concordance = concordance_index.offsets(word)
                if concordance:
                    concordance_data.append((word, concordance))
        string = ""
        for word, concordance in concordance_data:
            string += f'Слово: {word}, Конкордансы: {concordance}\n'
        self._show_info(string)
