import tkinter as tk
from tkinter import filedialog
import spacy
from spacy.matcher import Matcher

# Загрузить модель spaCy для русского языка
nlp = spacy.load("ru_core_news_md")

# Создать сопоставитель для поиска намерений пользователя
matcher = Matcher(nlp.vocab) 

responses = {
    "транспорт": "Я могу предложить вам следующие виды транспорта:",
    "автомобиль": "Мы предоставляем услуги аренды автомобилей различных марок и классов.",
    "поезд": "У нас имеются билеты на поезд в разные направления.",
    "самолет": "Мы предлагаем билеты на рейсы различных авиакомпаний.",
    "авиабилет": "Мы предлагаем билеты на рейсы различных авиакомпаний.",
    "такси": "Мы предоставляем услуги заказа такси на любую дистанцию.",
    "автобус": "У нас имеются билеты на автобусные маршруты различных перевозчиков.",
    "велосипед": "Мы предлагаем велосипеды для проката на любой период времени.",
    "электросамокат": "Мы предоставляем услуги аренды электросамокатов для комфортных поездок по городу.",
    "трамвай": "У нас есть билеты на трамвайные маршруты в городе.",
    "поездка": "Я могу помочь вам с планированием вашей следующей поездки.",
    "путешествие": "Я могу помочь вам с планированием вашего следующего путешествия."
}


patterns= [{"LEMMA": {"IN": [*responses.keys()]}}]
matcher.add("lemmas", [patterns])


def analyze_intent(text):
    # Проанализировать текст
    doc = nlp(text)
    print(doc)
    for token in doc:
        print(token.text,token.pos_,token.dep_,token.lemma_)
    # Найти намерение пользователя
    matches = matcher(doc)
    print(matches)
    # Получить намерение из первого совпадения (если оно есть)
    intent = ""

    if len(matches) > 0 and len(matches[0])>2:
        intent = doc[matches[0][1]].lemma_
        print(intent)
    return intent

def generate_response(intent):
    # Получить ответ из словаря ответов на основе намерения
    response = responses.get(intent, "Я не понимаю вашего запроса.")

    return response

def send_message(event):
    # Получить сообщение пользователя
    user_message = text_box.get("1.0", "end-1c")

    # Проанализировать намерение пользователя
    intent = analyze_intent(user_message)

    # Сгенерировать ответ системы
    response = generate_response(intent)

    # Очистить поле ввода
    text_box.delete("1.0", "end")

    # Отобразить ответ системы
    chat_history.insert("end", f"**Система:** {response}\n")

# Создать основное окно GUI
root = tk.Tk()
root.title("Автоматический ответчик на естественном языке")

# Создать поле ввода для сообщения пользователя
text_box = tk.Text(root)
text_box.bind("<Alt_L>", send_message)
text_box.pack()

# Создать поле вывода для чата
chat_history = tk.Text(root)
chat_history.pack()

# Запустить основное окно GUI
root.mainloop()