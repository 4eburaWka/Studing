import re
import nltk
import tkinter as tk
from tkinter import filedialog, Text
from sklearn.feature_extraction.text import TfidfVectorizer
from transformers import MBartForConditionalGeneration, MBart50TokenizerFast
from docx import Document
import threading

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize

# Функция для чтения текста из docx
def extract_text_from_docx(docx_file):
    doc = Document(docx_file)
    full_text = []
    for paragraph in doc.paragraphs:
        full_text.append(paragraph.text)
    return '\n'.join(full_text)

# Функция для очистки текста
def clean_text(text):
    text = re.sub(r'\s+', ' ', text)  # Удаление лишних пробелов
    text = re.sub(r'\d+', '', text)  # Удаление чисел
    return text

# Классический метод с использованием TF-IDF
def extract_sentences_tfidf(text):
    sentences = sent_tokenize(text)
    stop_words = set(stopwords.words('russian'))
    
    cleaned_sentences = [' '.join([word for word in word_tokenize(sentence.lower()) if word.isalpha() and word not in stop_words]) for sentence in sentences]
    
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(cleaned_sentences)
    
    return sentences, tfidf_matrix.sum(axis=1) #type: ignore

def generate_summary(sentences, sentence_weights, summary_length=10):
    ranked_sentences = sorted(((weight, sentence) for sentence, weight in zip(sentences, sentence_weights)), reverse=True)
    summary = ' '.join([sentence for weight, sentence in ranked_sentences[:summary_length]])
    return summary

# Метод с использованием модели mBART
def generate_ml_summary(text):
    model_name = "facebook/mbart-large-50-many-to-many-mmt"
    model = MBartForConditionalGeneration.from_pretrained(model_name)
    tokenizer = MBart50TokenizerFast.from_pretrained(model_name)

    tokenizer.src_lang = "ru_RU"
    inputs = tokenizer.encode(text, return_tensors="pt", max_length=1024, truncation=True)

    summary_ids = model.generate(inputs, max_length=250, min_length=40, length_penalty=2.0, num_beams=4, early_stopping=False, forced_bos_token_id=tokenizer.lang_code_to_id["ru_RU"])
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

    return summary

# Функция для обработки документа и вывода результата
def summarize_docx(docx_file, method):
    text = extract_text_from_docx(docx_file)
    cleaned_text = clean_text(text)

    if method == "TF-IDF":
        sentences, sentence_weights = extract_sentences_tfidf(cleaned_text)
        summary = generate_summary(sentences, sentence_weights)
    elif method == "ML":
        summary = generate_ml_summary(cleaned_text)

    return text, summary

# Функция для выбора файла
def open_file():
    filepath = filedialog.askopenfilename(filetypes=[("Document files", "*.docx")])
    if filepath:
        selected_file.set(filepath)

        text = extract_text_from_docx(filepath)
        original_text_box.delete(1.0, tk.END)
        original_text_box.insert(tk.END, text)

def run_summarize():
    threading.Thread(target=summarize).start()

def summarize():
    if selected_file.get():
        method_choice = method.get()
        original_text_box.delete(1.0, tk.END)
        summary_text_box.delete(1.0, tk.END)
        try:
            original_text, summary = summarize_docx(selected_file.get(), method_choice)
            # Выводим исходный текст
            original_text_box.insert(tk.END, original_text)
            # Выводим сводку
            summary_text_box.insert(tk.END, summary)
        except Exception as e:
            summary_text_box.insert(tk.END, f"Ошибка при создании сводки: {e}")

root = tk.Tk()
root.title("Краткость - С. Т.")

selected_file = tk.StringVar()
method = tk.StringVar(value="TF-IDF")

file_button = tk.Button(root, text="Выбрать файл .docx", command=open_file)
file_button.pack(pady=10)

file_label = tk.Label(root, textvariable=selected_file)
file_label.pack()

tfidf_radio = tk.Radiobutton(root, text="TF-IDF", variable=method, value="TF-IDF")
tfidf_radio.pack(anchor="w")
ml_radio = tk.Radiobutton(root, text="ML", variable=method, value="ML")
ml_radio.pack(anchor="w")

summarize_button = tk.Button(root, text="Сделать сводку", command=run_summarize)
summarize_button.pack(pady=10)

original_text_label = tk.Label(root, text="Исходный текст:")
original_text_label.pack()
original_text_box = Text(root, height=10, width=80)
original_text_box.pack(pady=5)

summary_text_label = tk.Label(root, text="Сводка:")
summary_text_label.pack()
summary_text_box = Text(root, height=10, width=80)
summary_text_box.pack(pady=5)

root.mainloop()