import tkinter as tk
import docx2txt

# Функция вычисления редакционного расстояния
def edit_distance(str1, str2):
    m = len(str1) + 1
    n = len(str2) + 1
    t = [[i + j for j in range(n)] for i in range(m)]
    for i in range(1, m):
        c = i - 1
        for j in range(1, n):
            d = j - 1
            t[i][j] = min(t[c][j] + 1, t[i][d] + 1, t[c][d] + (str1[c] != str2[d]))
    return t[m - 1][n - 1]

root = tk.Tk()
root.title("Редакционное расстояние")

def load_text(filename):
    text = docx2txt.process(filename)
    return text

def get_words(text):
    words = text.split()
    return words

text = load_text('EAI/LAB3/text.docx')
words = get_words(text)

def calculate_distances():
    input_word = input_entry.get()
    max_distance = int(max_distance_entry.get())
    results = []
    for word in words:
        distance = edit_distance(input_word, word)
        if distance <= max_distance:
            results.append((word, distance))
    results.sort(key=lambda x: x[1], reverse=True)
    output_text.delete("1.0", tk.END)
    for word, distance in results:
        output_text.insert(tk.END, f"{word} ({distance})\n")

# Интерфейс
input_label = tk.Label(root, text="Введите входное слово:")
input_entry = tk.Entry(root, width=100)

max_distance_label = tk.Label(root, text="Введите максимальное расстояние:")
max_distance_entry = tk.Entry(root, width=100)

calculate_button = tk.Button(root, text="Вычислить", command=calculate_distances)

output_label = tk.Label(root, text="Результаты:")
output_text = tk.Text(root, height=10)

input_label.pack()
input_entry.pack()

max_distance_label.pack()
max_distance_entry.pack()

calculate_button.pack()

output_label.pack()
output_text.pack()

root.mainloop()