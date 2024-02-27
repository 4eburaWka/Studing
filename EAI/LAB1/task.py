import nltk
from nltk.corpus import wordnet as wn

# Функция для извлечения лексем из текста


def extract_lemmas(text):
    lemmas = []
    for token in nltk.word_tokenize(text):
        # Лемматизация
        lemma = wn.morphy(token)
        if lemma:
            lemmas.append(lemma)
    return lemmas

# Функция для формирования словаря


def create_dictionary(lemmas):
    dictionary = {}
    for lemma in lemmas:
        # Получение синонимов
        synonyms = [syn.name() for syn in wn.synsets(lemma)]
        # Получение антонимов
        antonyms = []
        for synset in wn.synsets(lemma):
            for antonym in synset.lemmas():
                antonyms.append(antonym.name())
        # Добавление информации в словарь
        dictionary[lemma] = {"synonyms": synonyms, "antonyms": antonyms}
    return dictionary

# Функция для сортировки словаря


def sort_dictionary(dictionary):
    return sorted(dictionary.items(), key=lambda x: x[0])

# Функция для вывода словаря


def print_dictionary(dictionary):
    for lemma, info in dictionary:
        print(f"{lemma}: {info}")


# Пример использования
with open('EAI/LAB1/file.txt', encoding='utf-8') as file:
    text = file.read()
lemmas = extract_lemmas(text)
dictionary = create_dictionary(lemmas)
sorted_dictionary = sort_dictionary(dictionary)
print_dictionary(sorted_dictionary)
