import tkinter as tk
import csv

from tkinter import ttk
from tkinter import filedialog
from tkinter import colorchooser
from tkinter.filedialog import askopenfilename, asksaveasfilename
from PIL import Image, ImageDraw
from copy import deepcopy

import numpy as np

from config import *
from functions import rgb_to_hex, hex_to_rgb, rgb_to_hex_arr


class Level:
    def __init__(self, frame: tk.Frame, selected_block: tk.IntVar, btn_icons, map: list[list[int]] = None, music = None) -> None:
        self.frame = frame
        self.btn_icons = btn_icons
        self.selected_block = selected_block
        self.canvas = tk.Canvas(self.frame, height=18 * CELL_SIZE)
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.scroll_bar = tk.Scrollbar(self.frame, orient=tk.HORIZONTAL, command=self.canvas.xview)
        self.canvas.configure(xscrollcommand=self.scroll_bar.set)
        self.scroll_bar.pack(side=tk.BOTTOM, fill=tk.X)
        self.canvas.bind("<MouseWheel>", self.on_mousewheel)
        self.canvas.bind("<Button-1>", self.on_canvas_click)
        if map is None:
            self.map = [[0 for _ in range(30)] for __ in range(18)]
            self.music = ""
        else:
            self.map = map
            self.music = music

    def on_mousewheel(self, event):
        self.canvas.xview_scroll(int(-1*(event.delta/120)), "units")  # Скроллинг колесиком мыши
    
    def on_canvas_click(self, event):
        x = int((event.x + self.canvas.xview()[0] * CELL_SIZE * len(self.map[0])) // CELL_SIZE)
        y = event.y // CELL_SIZE
        self.map[y][x] = self.selected_block.get()
        self.show()

    def clear(self):
        self.map = [[0 for _ in range(30)] for __ in range(18)]
        self.music = ""
        self.show()

    def read_csv(self, path, show_on_sreen: bool = True):
        lvl = []
        music = ""
        with open(path, newline='') as csvfile:
            trash = csv.reader(csvfile, delimiter=',')
            for i, row in enumerate(trash):
                if i < 18:
                    lvl.append(list(map(int, row)))
                if i == 19:
                    music = row[0]
                    break
        # for i in range(len(lvl)):
        #     lvl[i].remove(END)
        self.map = lvl
        self.music = music
        if show_on_sreen:
            self.show()

    
    def write_csv(self, path):
        lvl = deepcopy(self.map)
        lvl += [ [PLATFORM for _ in range(len(self.map[0]))], [self.music] ]
        with open(path, 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile, delimiter=',')
            for row in lvl:
                # row += [END]
                csvwriter.writerow(row)

    def add_space(self):
        for row in self.map:
            row += [0 for _ in range(20)]
        self.show()
    
    def add_block(self, block: int, pos: tuple):
        self.map[pos[0]][pos[1]] = block
    
    def delete_block(self, pos):
        self.map[pos[0]][pos[1]] = NOTHING
    
    def show(self):
        self.canvas.delete("blocks")
        for i in range(len(self.map)):
            for j in range(len(self.map[i])):
                x0 = j * CELL_SIZE - self.canvas.xview()[0] * CELL_SIZE
                y0 = i * CELL_SIZE
                x1 = x0 + CELL_SIZE
                y1 = y0 + CELL_SIZE
                self.canvas.create_rectangle(x0, y0, x1, y1, outline='gray', tags='blocks')
                try:
                    image = self.btn_icons[self.map[i][j]]
                    self.canvas.create_image(x0, y0, anchor='nw', image=image, tags="blocks")
                except KeyError:
                    pass
        self.canvas.config(scrollregion=self.canvas.bbox("all"))
    

class Editor:

    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.attributes('-fullscreen', True)
        self.btn_icons = {block: tk.PhotoImage(file='images/'+blocks_images[block]).subsample(2) for block in blocks_images.keys()}
        self.selected_block = tk.IntVar(value=PLATFORM)

        ### EDITOR LOGIC
        level_frame = tk.Frame(self.root, borderwidth=1, relief='solid')
        level_object = Level(level_frame, self.selected_block, btn_icons=self.btn_icons)
        level_object.read_csv(r'C:\Users\litvi\Projects\Pydash\levels\kobrin gas.csv')

        level_object.show()
        ###

        ### INTERFACE
        main_menu = tk.Menu(self.root)
        file_menu = tk.Menu(self.root)
        level_menu = tk.Menu(self.root)
        main_menu.add_cascade(label='Файл', menu=file_menu)
        main_menu.add_cascade(label='Уровень', menu=level_menu)
        file_menu.add_command(label="Новый", command=level_object.clear)
        file_menu.add_command(label="Открыть", command=lambda: level_object.read_csv(askopenfilename(
            initialdir=r"./levlels", title="Select file",
            filetypes=(("CSV files", "*.csv"), ("All files", "*.*")),
        )))
        file_menu.add_command(label="Сохранить", command=lambda: level_object.write_csv(asksaveasfilename(
            initialdir=r"levels", title="Select file",
            filetypes=(("CSV files", "*.csv"), ("All files", "*.*")),
            defaultextension='.csv'
        )))
        file_menu.add_command(label="Выход", command=self.root.destroy)
        level_menu.add_command(label='Добавить длину уровня', command=level_object.add_space)
        level_menu.add_command(label='Выбрать трек',
                               command=lambda: setattr(
                                   level_object, 'music',
                                   askopenfilename(
                                       initialdir=r"music", title="Select file",
                                       filetypes=(("MP3 files", "*.mp3"), ("WAV files", "*.wav"), ("All files", "*.*")),
                                   )
                                )
        )
        self.root.config(menu=main_menu)

        ### CONTROL
        control_frame = tk.Frame(self.root, borderwidth=1, relief='solid')

        self.delete_btn_icon = tk.PhotoImage(file='images/delete_icon.png').subsample(2)

        platform_btn = ttk.Radiobutton(control_frame, image=self.btn_icons[PLATFORM], value=PLATFORM, variable=self.selected_block, style='TButton')
        narrow_platform_btn = ttk.Radiobutton(control_frame, image=self.btn_icons[NARROW_PLATFORM], value=NARROW_PLATFORM, variable=self.selected_block, style='TButton')
        down_narrow_platform_btn = ttk.Radiobutton(control_frame, image=self.btn_icons[DOWN_NARROW_PLATFORM], value=DOWN_NARROW_PLATFORM, variable=self.selected_block, style='TButton')
        trick_btn = ttk.Radiobutton(control_frame, image=self.btn_icons[TRICK], value=TRICK, variable=self.selected_block, style='TButton')
        spike_btn = ttk.Radiobutton(control_frame, image=self.btn_icons[SPIKE], value=SPIKE, variable=self.selected_block, style='TButton')
        short_spike_btn = ttk.Radiobutton(control_frame, image=self.btn_icons[SHORT_SPIKE], value=SHORT_SPIKE, variable=self.selected_block, style='TButton')
        orb_btn = ttk.Radiobutton(control_frame, image=self.btn_icons[ORB], value=ORB, variable=self.selected_block, style='TButton')
        pad_btn = ttk.Radiobutton(control_frame, image=self.btn_icons[PAD], value=PAD, variable=self.selected_block, style='TButton') 
        pink_pad_btn = ttk.Radiobutton(control_frame, image=self.btn_icons[PINK_PAD], value=PINK_PAD, variable=self.selected_block, style='TButton') 
        gravity_portal_btn = ttk.Radiobutton(control_frame, image=self.btn_icons[GRAVITY_PORTAL], value=GRAVITY_PORTAL, variable=self.selected_block, style='TButton') 
        rocket_portal_btn = ttk.Radiobutton(control_frame, image=self.btn_icons[ROCKET_PORTAL], value=ROCKET_PORTAL, variable=self.selected_block, style='TButton') 
        cube_portal_btn = ttk.Radiobutton(control_frame, image=self.btn_icons[CUBE_PORTAL], value=CUBE_PORTAL, variable=self.selected_block, style='TButton') 
        coin_btn = ttk.Radiobutton(control_frame, image=self.btn_icons[COIN], value=COIN, variable=self.selected_block, style='TButton')
        delete_btn = ttk.Radiobutton(control_frame, image=self.delete_btn_icon, value=0, variable=self.selected_block, style='TButton')
        ###

        platform_btn.pack(side=tk.LEFT)
        narrow_platform_btn.pack(side=tk.LEFT)
        down_narrow_platform_btn.pack(side=tk.LEFT)
        trick_btn.pack(side=tk.LEFT)
        spike_btn.pack(side=tk.LEFT)
        short_spike_btn.pack(side=tk.LEFT)
        orb_btn.pack(side=tk.LEFT)
        pad_btn.pack(side=tk.LEFT)
        pink_pad_btn.pack(side=tk.LEFT)
        gravity_portal_btn.pack(side=tk.LEFT)
        rocket_portal_btn.pack(side=tk.LEFT)
        cube_portal_btn.pack(side=tk.LEFT)
        coin_btn.pack(side=tk.LEFT)
        delete_btn.pack(side=tk.RIGHT)
        control_frame.pack(side=tk.BOTTOM, fill=tk.X, padx=5, pady=5)
        
        level_frame.pack(side=tk.TOP, anchor='s', fill=tk.BOTH, padx=5, pady=5)

    def show_app(self):
        self.root.mainloop()


class PlayerEditor:    
    def __init__(self, root: tk.Tk, width=40, height=40, pixel_size=20):
        self.root = root
        self.root.attributes('-fullscreen', True)
        self.cube = [['#ffffff' for _ in range(height)] for __ in range(width)]
        self.width = width
        self.height = height
        self.pixel_size = pixel_size

        self.color = tk.StringVar(self.root, '#ff1fff')
        
        self.canvas = tk.Canvas(self.root, width=self.width * self.pixel_size, height=self.height * self.pixel_size, bg="white")
        self.canvas.pack(pady=50)
        
        self.canvas.bind("<Button-1>", self.paint_pixel)
        self.canvas.bind("<B1-Motion>", self.paint_pixel)

        self.color_btn = tk.Button(self.root, background=self.color.get(), width=20, command=self.choose_color, border=0)
        self.color_btn.pack(side='left', padx=500)
        
        self.submit_btn = tk.Button(self.root, text="Применить", width=20, command=self.submit)
        self.submit_btn.pack(side='right', anchor='e', padx=(0, 500))
        
        self.noise_btn = tk.Button(self.root, text="Добавить шум", width=20, command=self.add_noise)
        self.noise_btn.pack(side='right', anchor='e')
        # self.filter_btn = tk.Button(self.root, text="Применить фильтр", width=20, command=self.median_filter)
        # self.filter_btn.pack(side='right', anchor='e')


        menu = tk.Menu(self.root)
        self.root.config(menu=menu)
        file_menu = tk.Menu(menu)
        menu.add_cascade(label="Файл", menu=file_menu)
        file_menu.add_command(label="Новый", command=self.clear)
        file_menu.add_command(label="Сохранить", command=self.save_image)
        file_menu.add_command(label="Открыть", command=self.open_image)
        file_menu.add_command(label="Выход", command=self.root.destroy)

        self.create_grid()
    
    def add_noise(self):
        intensity = 0.05
        noisy_image = np.copy(list(map(hex_to_rgb, self.cube)))

        num_salt = np.ceil(intensity * noisy_image.size * 0.5)
        num_pepper = np.ceil(intensity * noisy_image.size * 0.5)

        salt_coords = [np.random.randint(0, i - 1, int(num_salt))
                    for i in noisy_image.shape]
        noisy_image[salt_coords[0], salt_coords[1]] = 255

        pepper_coords = [np.random.randint(
            0, i - 1, int(num_pepper)) for i in noisy_image.shape]
        noisy_image[pepper_coords[0], pepper_coords[1]] = 0
        self.cube = list(map(rgb_to_hex_arr, noisy_image))
        self.create_grid()
    
    def median_filter(self):
        center_y = 2
        center_x = 3
        window_size = 5
        image = np.copy(list(map(hex_to_rgb, self.cube)))
        filtered_image = np.copy(image)

        try:
            for index, i in enumerate(range(image.shape[0])):
                for j in range(image.shape[1]):

                    window = [
                        filtered_image[i + y][j] for y in range(-center_y+1, -center_y+1+window_size)
                    ] + [
                        filtered_image[i][j + x] for x in range(-center_x+1, -center_x+1+window_size) if x != 0
                    ]

                    window.sort(key=lambda x: sum(x))
                    
                    median_value = window[(len(window)-1)//2+1]
                    filtered_image[i, j] = median_value
        except IndexError:
            pass
        self.cube = list(map(rgb_to_hex_arr, filtered_image))
        self.create_grid()

    def horizontal(self): 
        count_column = self.size_window - 1
        image = np.copy(list(map(hex_to_rgb, self.cube)))
        for i in range(3):
            channel = []
            new_cols = count_column // 2
            arr_padded = np.pad(channel, ((0,0), (new_cols, new_cols)),mode='constant', constant_values=0 )
            empty_matrix = np.zeros_like(arr_padded)

            iter_i = arr_padded.shape[0]
            iter_j = arr_padded.shape[1] - self.size_window + 1
            for i in range(iter_i):
                for j in range(iter_j):
                    window = arr_padded[i, j : j + self.size_window]
                    median_value = np.median(window)
                    empty_matrix[i, j + self.size_window // 2] = median_value

            ready_median_matrix = empty_matrix[:, new_cols:-new_cols]
        return ready_median_matrix


    def choose_color(self):
        color = colorchooser.askcolor(self.color.get())[1]
        if color:
            self.color.set(color)
            self.color_btn.configure(background=self.color)
    
    def submit(self):
        self.save_image(file_path='images/player.png')
        self.root.destroy()
        
    def create_grid(self):
        for x in range(self.width):
            for y in range(self.height):
                x_ = x * self.pixel_size
                y_ = y * self.pixel_size
                self.canvas.create_rectangle(x_, y_, x_+self.pixel_size, y_+self.pixel_size, fill=self.cube[x][y], outline="gray")
    
    def paint_pixel(self, event):
        x = event.x // self.pixel_size
        y = event.y // self.pixel_size
        self.cube[x][y] = self.color.get()
        self.canvas.create_rectangle(x * self.pixel_size, y * self.pixel_size,
                                     (x + 1) * self.pixel_size, (y + 1) * self.pixel_size,
                                     fill=self.color.get(), outline="")

    def clear(self):
        self.cube = [['#ffffff' for _ in range(self.height)] for __ in range(self.width)]
        self.refresh_canvas()

    def save_image(self, file_path=""):
        if not file_path:
            file_path = filedialog.asksaveasfilename(defaultextension=".png")
        if file_path:
            image = Image.new("RGB", (self.width, self.height), "white")
            draw = ImageDraw.Draw(image)
            for x in range(self.width):
                for y in range(self.height):
                    color = self.cube[x][y]
                    draw.rectangle([(x, y),
                                    ((x + 1), (y + 1))],
                                   fill=color)
            draw.rectangle([(0, 0), (self.width - 1, self.height - 1)],
                           outline="black", width=1)
            image.save(file_path)


    def open_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            image = Image.open(file_path)
            image = image.rotate(90, expand=True)
            image = image.transpose(Image.FLIP_TOP_BOTTOM)
            image = image.resize((self.width, self.height))
            pixels = list(map(rgb_to_hex, image.getdata()))
            self.cube = [pixels[i:i+self.width] for i in range(0, len(pixels), self.width)]

            self.refresh_canvas()

    def refresh_canvas(self):
        self.canvas.delete("all")
        self.create_grid()
    

    def show_app(self):
        self.root.mainloop()


def show_editor(class_):
    root = tk.Tk()
    for widget in root.winfo_children():
        widget.destroy()
    
    editor = class_(root)
    editor.show_app()


if __name__ == '__main__':
    show_editor(PlayerEditor)

