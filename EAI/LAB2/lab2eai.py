import nltk
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import wordnet as wn
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

word_freq_dist = None

def analyze_text():
    global word_freq_dist

    input_text = text_entry.get("1.0",'end-1c')

    tokens = word_tokenize(input_text)

    pos_tags = nltk.pos_tag(tokens)

    lemmatizer = nltk.WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in tokens]

    word_freq_dist = FreqDist(tokens)

    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, "Частотные характеристики словоформ:\n")
    output_text.insert(tk.END, f"{word_freq_dist}\n\n")
    output_text.insert(tk.END, "Частеречная разметка:\n")
    output_text.insert(tk.END, f"{pos_tags}\n\n")
    output_text.insert(tk.END, "Лемматизация:\n")
    output_text.insert(tk.END, f"{lemmatized_tokens}\n\n")
    output_text.insert(tk.END, "Морфологические характеристики и метаданные:\n")
    for token in tokens:
        synsets = wn.synsets(token)
        if synsets:
            output_text.insert(tk.END, f"Слово: {token}\n")
            for synset in synsets:
                output_text.insert(tk.END, f"  Определение: {synset.definition()}\n")
                output_text.insert(tk.END, f"  Примеры: {', '.join(synset.examples())}\n")
                output_text.insert(tk.END, f"  Часть речи: {synset.pos()}\n\n")
    output_text.insert(tk.END, "-----------------------------------------------------\n")

root = tk.Tk()
root.title("Кулинарный анализатор по Американски")

label = ttk.Label(root, text="Введите текст для анализа:")
label.grid(row=0, column=0, padx=10, pady=10)

text_entry = scrolledtext.ScrolledText(root, width=40, height=10)
text_entry.grid(row=1, column=0, padx=10, pady=10)

analyze_button = ttk.Button(root, text="Анализировать", command=analyze_text)
analyze_button.grid(row=2, column=0, padx=10, pady=10)

output_text = scrolledtext.ScrolledText(root, width=80, height=20)
output_text.grid(row=3, column=0, padx=10, pady=10, columnspan=2)

root.mainloop()