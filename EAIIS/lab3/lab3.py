import tkinter as tk
from tkinter import filedialog, scrolledtext, messagebox
import fitz  
from googletrans import Translator
import tempfile
import os
import threading

class PDFTranslatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Перакладчык")

        self.open_button = tk.Button(root, text="Открыть PDF", command=self.open_pdf)
        self.open_button.pack(pady=10)

        self.text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=20)
        self.text_area.pack(pady=10)

        self.translate_button = tk.Button(root, text="Перевести", command=self.start_translation_thread)
        self.translate_button.pack(pady=10)

        self.stop_button = tk.Button(root, text="Стоп", command=self.stop_translation, state=tk.DISABLED)
        self.stop_button.pack(pady=10)

        self.translated_text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=20)
        self.translated_text_area.pack(pady=10)

        self.translator = Translator()
        self.temp_file = None
        self.stop_translation_flag = False

    def open_pdf(self):
        file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
        if file_path:
            try:
                doc = fitz.open(file_path)
                self.temp_file = tempfile.NamedTemporaryFile(delete=False, mode='w+', encoding='utf-8')

                for page_num in range(doc.page_count):
                    page = doc.load_page(page_num)
                    page_text = page.get_text("text")
                    self.temp_file.write(page_text + '\n\n')

                self.temp_file.flush()
                self.temp_file.seek(0)

                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.INSERT, self.temp_file.read())

                self.translated_text_area.delete(1.0, tk.END)
                self.translate_button.config(state=tk.NORMAL)
            except Exception as e:
                messagebox.showerror("Ошибка", f"Не удалось открыть PDF: {e}")

    def start_translation_thread(self):
        """Запуск перевода в отдельном потоке"""
        self.stop_translation_flag = False
        translation_thread = threading.Thread(target=self.translate_text)
        translation_thread.start()
        self.stop_button.config(state=tk.NORMAL)
        self.translate_button.config(state=tk.DISABLED)
        self.open_button.config(state=tk.DISABLED)

    def stop_translation(self):
        self.stop_translation_flag = True
        self.stop_button.config(state=tk.DISABLED)

    def translate_text(self):
        if self.temp_file:
            try:
                self.temp_file.seek(0)
                self.translated_text_area.delete(1.0, tk.END)

                self.translate_button.config(text="Переводим...")

                for line in self.temp_file:
                    if self.stop_translation_flag:
                        break

                    if line.strip():
                        translated = self.translator.translate(line.strip(), src='en', dest='fr').text # перевод с английского на немецкий
                        self.translated_text_area.insert(tk.END, translated + '\n\n')
                        self.translated_text_area.update_idletasks()

                self.translate_button.config(state=tk.NORMAL, text="Перевести")
                self.open_button.config(state=tk.NORMAL)
                self.stop_button.config(state=tk.DISABLED)

            except Exception as e:
                messagebox.showerror("Ошибка", f"Не удалось перевести текст: {e}")
                self.translate_button.config(state=tk.NORMAL)
                self.stop_button.config(state=tk.DISABLED)
                self.open_button.config(state=tk.NORMAL)
        else:
            messagebox.showwarning("Внимание", "Сначала откройте PDF файл.")

    def __del__(self):
        """Функция для удаления временного файла при завершении программы"""
        if self.temp_file:
            try:
                os.remove(self.temp_file.name)
            except Exception as e:
                print(f"Не удалось удалить временный файл: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = PDFTranslatorApp(root)
    root.mainloop()