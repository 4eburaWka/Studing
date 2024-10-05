import os
import PyPDF2
import docx
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext, StringVar
from collections import defaultdict
import numpy as np

def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text() + "\n"
    return text

def extract_text_from_docx(docx_path):
    doc = docx.Document(docx_path)
    text = "\n".join([para.text for para in doc.paragraphs])
    return text

def index_files(directory):
    index = {}
    word_freqs = defaultdict(lambda: defaultdict(int))  # Частота слов для каждого документа
    total_words = defaultdict(int)  # Общее количество слов в каждом документе

    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.pdf'):
                path = os.path.join(root, file)
                text = extract_text_from_pdf(path)
                index[path] = text
            elif file.endswith('.docx'):
                path = os.path.join(root, file)
                text = extract_text_from_docx(path)
                index[path] = text

            # Подсчет частоты слов для каждого документа
            words = text.lower().split()
            for word in words:
                word_freqs[path][word] += 1
                total_words[path] += 1

    return index, word_freqs, total_words

def calculate_probabilities(word, word_freqs, total_words, smoothing=1):
    """
    Рассчитываем вероятность появления слова в каждом документе.
    """
    probabilities = {}
    for doc_path in word_freqs:
        word_count = word_freqs[doc_path].get(word, 0)
        doc_size = total_words[doc_path]
        # Применяем сглаживание Лапласа для обработки случаев отсутствия слова в документе
        probabilities[doc_path] = (word_count + smoothing) / (doc_size + smoothing * len(word_freqs))
    return probabilities

def search_index(index, word_freqs, total_words, query):
    query_words = query.lower().split()
    results = defaultdict(float)  # Вероятностные результаты для каждого документа

    for word in query_words:
        word_probs = calculate_probabilities(word, word_freqs, total_words)
        for doc_path, prob in word_probs.items():
            results[doc_path] += np.log(prob)  # Суммируем логарифмы вероятностей

    # Сортировка результатов по вероятности
    sorted_results = sorted(results.items(), key=lambda x: x[1], reverse=True)

    final_results = {}
    for doc_path, score in sorted_results:
        final_results[doc_path] = {'score': score, 'text': index[doc_path]}

    return final_results

def browse_directory():
    directory = filedialog.askdirectory()
    if directory:
        indexing_label.set("Индексация...")
        root.update()
        index, word_freqs, total_words = index_files(directory)
        indexing_label.set("Индексация завершена.")
        messagebox.showinfo("Индексация завершена", f"Найдено {len(index)} файлов.")
        return index, word_freqs, total_words
    return {}, None, None

def update_index():
    global index, word_freqs, total_words
    index, word_freqs, total_words = browse_directory()

def search_files():
    query = query_entry.get()
    if not query:
        messagebox.showwarning("Предупреждение", "Введите запрос для поиска.")
        return
    results = search_index(index, word_freqs, total_words, query)
    result_text.delete(1.0, tk.END)

    if results:
        for path, data in results.items():
            result_text.insert(tk.END, f"Найдено в: {path} (Релевантность: {data['score']:.4f})\nТекст:\n")
            result_text.insert(tk.END, f"{data['text'][:200]}...\n")
            result_text.insert(tk.END, "-----\n")
    else:
        result_text.insert(tk.END, "Результаты не найдены.\n")

root = tk.Tk()

frame = tk.Frame(root)
frame.pack(pady=10)

index = {}

indexing_label = StringVar()
indexing_label.set("")

browse_button = tk.Button(frame, text="Выбрать папку для индексации", command=lambda: update_index())
browse_button.pack(pady=5)

query_label = tk.Label(frame, text="Введите запрос для поиска:")
query_label.pack(pady=5)

query_entry = tk.Entry(frame, width=50)
query_entry.pack(pady=5)

search_button = tk.Button(frame, text="Поиск", command=search_files)
search_button.pack(pady=5)

indexing_status = tk.Label(frame, textvariable=indexing_label)
indexing_status.pack(pady=5)

result_text = scrolledtext.ScrolledText(root, width=80, height=20)
result_text.pack(pady=10)

root.mainloop()
