import tkinter as tk
import numpy as np

from CNN import CnnFromScratch, train



class App:    
    def __init__(self, root: tk.Tk, width=28, height=28, pixel_size=10):
        self.model = CnnFromScratch(load_weights=False)
        train(self.model, change_weights=False)

        self.root = root
        self.root.attributes('-fullscreen', True)
        self.cube = [[0 for _ in range(height)] for __ in range(width)]
        self.width = width
        self.height = height
        self.pixel_size = pixel_size

        self.color = tk.IntVar(self.root, 255)
        
        self.canvas = tk.Canvas(self.root, width=self.width * self.pixel_size, height=self.height * self.pixel_size, bg="white")
        self.canvas.pack(pady=50)
        
        self.canvas.bind("<Button-1>", self.paint_pixel)
        self.canvas.bind("<B1-Motion>", self.paint_pixel)

        self.reset = tk.Button(self.root, text="Стереть", width=20, command=self.clear)
        self.reset.pack()

        self.fit = tk.Button(self.root, text="Распознать", width=20, command=self.recognize)
        self.fit.pack()

        self.text = tk.Text(self.root)
        self.text.pack()

        self.train = tk.Button(self.root, text="Обучить", width=20, command=lambda: train(self.model, change_weights=True))
        self.train.pack()

        self.reset_model = tk.Button(self.root, text="Сбросить веса", width=20, command=self.reset_model)
        self.reset_model.pack()


        menu = tk.Menu(self.root)
        self.root.config(menu=menu)
        file_menu = tk.Menu(menu)
        menu.add_cascade(label="Файл", menu=file_menu)
        file_menu.add_command(label="Новый", command=self.clear)
        file_menu.add_command(label="Выход", command=self.root.destroy)

        self.create_grid()

    def reset_model(self):
        self.model = CnnFromScratch(load_weights=False)

    def recognize(self):
        image = np.array(self.cube).T
        res = self.model([image])
        self.text.delete('1.0', 'end')
        self.text.insert('1.0', str(res.argmax()))
    
    def create_grid(self):
        for x in range(self.width):
            for y in range(self.height):
                x_ = x * self.pixel_size
                y_ = y * self.pixel_size
                self.canvas.create_rectangle(x_, y_, x_+self.pixel_size, y_+self.pixel_size, 
                                             fill='#ffffff' if self.cube[x][y] else '#000000', 
                                             outline="gray")
    
    def paint_pixel(self, event):
        x = event.x // self.pixel_size
        y = event.y // self.pixel_size
        self.cube[x][y] = self.color.get()
        self.canvas.create_rectangle(x * self.pixel_size, y * self.pixel_size,
                                     (x + 1) * self.pixel_size, (y + 1) * self.pixel_size,
                                     fill='#ffffff', outline="")

    def clear(self):
        self.cube = [[0 for _ in range(self.height)] for __ in range(self.width)]
        self.refresh_canvas()

    def refresh_canvas(self):
        self.canvas.delete("all")
        self.create_grid()
    

    def show_app(self):
        self.root.mainloop()

if __name__ == '__main__':
    root = tk.Tk()

    app = App(root)
    app.show_app()