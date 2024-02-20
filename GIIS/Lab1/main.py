from tkinter import filedialog, ttk
from PIL import Image, ImageTk

from functions import add_noise, median_filter

import cv2
import tkinter as tk


class App:
    def __init__(self, window, window_title):
        self.window = window
        self.window.geometry('500x970+10+10')
        self.window.title(window_title)

        self.canvas = tk.Canvas(window, width=500, height=500)
        self.canvas.pack()

        self.image = None

        self.create_widgets()

        self.window.mainloop()

    def create_widgets(self):
        self.btn_load = tk.Button(
            self.window, text="Загрузить изображение", command=self.load_image, width=42)
        self.btn_load.pack()
        self.btn_save = tk.Button(
            self.window, text="Сохранить изображение", command=self.save_image, width=42)
        self.btn_save.pack(pady=5)

        separator2 = ttk.Separator(self.window, orient='horizontal')
        separator2.pack(fill='x', pady=5)

        self.scale_noise = tk.Scale(self.window, from_=0, to=1, resolution=0.01, orient=tk.HORIZONTAL,
                                    label="Интенсивность шума:", length=300)
        self.scale_noise.set(0.05)
        self.scale_noise.pack(pady=5)

        self.btn_add_noise = tk.Button(
            self.window, text="Добавить шум", command=self.add_noise, width=42)
        self.btn_add_noise.pack(pady=5)

        separator2 = ttk.Separator(self.window, orient='horizontal')
        separator2.pack(fill='x', pady=5)

        self.scale_window_size = tk.Scale(self.window, from_=3, to=151, resolution=2, orient=tk.HORIZONTAL,
                                          label="Размер окна:", length=300)
        self.scale_window_size.set(5)
        self.scale_window_size.pack(pady=5)

        self.scale_center_x = tk.Scale(self.window, from_=1, to=151, resolution=1, orient=tk.HORIZONTAL,
                                       label="X координата центра окна:", length=300)
        self.scale_center_x.set(3)
        self.scale_center_x.pack(pady=5)

        self.scale_center_y = tk.Scale(self.window, from_=1, to=151, resolution=1, orient=tk.HORIZONTAL,
                                       label="Y координата центра окна:", length=300)
        self.scale_center_y.set(2)
        self.scale_center_y.pack(pady=5)

        self.btn_apply_filter = tk.Button(
            self.window, text="Применить фильтрацию", command=self.apply_filter, width=42)
        self.btn_apply_filter.pack(pady=5)

        self.progress_bar = tk.Label(self.window, text='', width=470)
        self.progress_bar.pack(pady=5)

    def load_image(self):
        filename = filedialog.askopenfilename(initialdir=r"C:\Users\litvi\Documents\Studing\GIIS\Lab1\img", title="Select file",
                                              filetypes=(("JPEG files", "*.jpg"), ("PNG files", "*.png"),
                                                         ("All files", "*.*")))
        if filename:
            self.image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
            self.show_image()
    def save_image(self):
        if self.image is None:
            return
        filename = filedialog.asksaveasfile(initialdir='/')
        if filename:
            cv2.imwrite(filename.name, self.image)

    def add_noise(self):
        if self.image is None:
            return

        intensity = self.scale_noise.get()
        self.image = add_noise(self.image, intensity)
        self.show_image(self.image)

    def apply_filter(self):
        if self.image is None:
            return
        
        self.progress_bar.config(text='')
        self.progress_bar.update()

        window_size = self.scale_window_size.get()
        center_x = self.scale_center_x.get()
        center_y = self.scale_center_y.get()

        self.image = median_filter(self.image, window_size, center_x, center_y, self.progress_bar)
        self.show_image(self.image)

    def show_image(self, image=None):
        if image is None:
            image = self.image

        image = Image.fromarray(image)
        image = image.resize((500, 500))
        image_tk = ImageTk.PhotoImage(image)

        self.canvas.create_image(0, 0, anchor=tk.NW, image=image_tk)
        self.canvas.image = image_tk


App(tk.Tk(), "ШУМОУДАЛЯТОР-3000")
