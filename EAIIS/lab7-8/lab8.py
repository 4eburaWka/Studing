import tkinter as tk
from tkinter import ttk
import pyttsx3

class TTSApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Система синтеза речи")

        self.engine = pyttsx3.init()
        voices = self.engine.getProperty('voices')

        for index, voice in enumerate(voices):
            print(f"Voice {index}: {voice.name}")
        self.label = tk.Label(root, text="Введите текст:", font=("Arial", 16))
        self.label.pack(pady=10)

        self.text_entry = tk.Text(root, height=10, width=50)
        self.text_entry.pack(pady=10)

        self.speak_button = tk.Button(root, text="ПРОИЗНЕСИТЬ", command=self.speak_text, font=("Arial", 12))
        self.speak_button.pack(pady=10)

        self.voice_label = tk.Label(root, text="Выберите голос:", font=("Arial", 12))
        self.voice_label.pack(pady=5)

        self.voices = self.engine.getProperty('voices')
        self.voice_var = tk.StringVar(value=self.voices[0].id)  # Установка первого голоса по умолчанию

        self.voice_combobox = ttk.Combobox(root, textvariable=self.voice_var, values=[voice.name for voice in self.voices])
        self.voice_combobox.pack(pady=5)

        self.speed_label = tk.Label(root, text="Установите скорость:", font=("Arial", 12))
        self.speed_label.pack(pady=5)

        self.speed_scale = tk.Scale(root, from_=50, to=300, orient=tk.HORIZONTAL, label="Скорость (слов в минуту)", length=400)
        self.speed_scale.set(150)  # Установка значения по умолчанию
        self.speed_scale.pack(pady=10)

        self.volume_label = tk.Label(root, text="Установите громкость:", font=("Arial", 12))
        self.volume_label.pack(pady=5)

        self.volume_scale = tk.Scale(root, from_=0.0, to=1.0, resolution=0.1, orient=tk.HORIZONTAL, label="Громкость", length=400)
        self.volume_scale.set(1.0)  # Установка значения по умолчанию
        self.volume_scale.pack(pady=10)

    def speak_text(self):
        text = self.text_entry.get("1.0", tk.END).strip()  # Получаем текст
        self.engine.setProperty('voice', self.get_selected_voice_id())  # Устанавливаем выбранный голос
        self.engine.setProperty('rate', self.speed_scale.get())  # Устанавливаем скорость
        self.engine.setProperty('volume', self.volume_scale.get())  # Устанавливаем громкость

        self.engine.say(text)  # Произносим текст
        self.engine.runAndWait()  # Ждем завершения

    def get_selected_voice_id(self):
        selected_voice_name = self.voice_var.get()  # Получаем выбранное имя голоса
        for voice in self.voices:
            if voice.name == selected_voice_name:
                return voice.id  # Возвращаем ID выбранного голоса
        return self.voices[0].id  # Если ничего не найдено, возвращаем первый голос

if __name__ == '__main__':
    root = tk.Tk()
    app = TTSApp(root)
    root.mainloop()