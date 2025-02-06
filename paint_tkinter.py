import tkinter
from tkinter import colorchooser, filedialog
from PIL import Image, ImageDraw
from tkinter import messagebox

#pillow
#pip install pillow - в терминале установка модуля

class DrawApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Рисование')

        self.last_x = None
        self.last_y = None
        self.brush_color = 'black'
        self.brush_size = 3
        self.mode = False

        self.canvas = tkinter.Canvas(bg='white', width=600, height=400)
        self.canvas.pack()


        self.toolbar = tkinter.Frame(root)
        self.toolbar.pack(fill=tkinter.X)

        self.color_btn = tkinter.Button(self.toolbar, text='Выбор цвета', command=self.choose_color)
        self.color_btn.pack(side=tkinter.LEFT)

        self.brush_size_slider = tkinter.Scale(self.toolbar, from_=1, to=20, orient=tkinter.HORIZONTAL)
        self.brush_size_slider.set(self.brush_size)
        self.brush_size_slider.pack(side=tkinter.LEFT)

        self.eraser_btn = tkinter.Button(self.toolbar, text='Ластик', command=self.toogle_eraser)
        self.eraser_btn.pack(side=tkinter.LEFT)

        self.clear_btn = tkinter.Button(self.toolbar, text='Очистить', command=self.clear_canvas)
        self.clear_btn.pack(side=tkinter.LEFT)

        self.save_btn = tkinter.Button(self.toolbar, text='Сохранить', command=self.save_canvas)
        self.save_btn.pack(side=tkinter.LEFT)


        self.image = Image.new("RGB", (600, 400), 'white')
        self.draw_image = ImageDraw.Draw(self.image)

        self.canvas.bind("<Button-1>", self.start_draw)
        self.canvas.bind("<B1-Motion>", self.draw)



    def choose_color(self):
        color = colorchooser.askcolor()[1]
        if color:
            self.brush_color = color

    def toogle_eraser(self):
        self.mode = not self.mode
        if self.mode:
            self.eraser_btn.config(relief=tkinter.SUNKEN)
        else:
            self.eraser_btn.config(relief=tkinter.RAISED)

    def clear_canvas(self):
        self.canvas.delete('all')

    def save_canvas(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", '*.png')])
        if file_path:
            self.image.save(file_path)
            messagebox.showinfo('Сохранение', 'Изображение успешно сохранено!')

    def start_draw(self, event):
        self.last_x = event.x
        self.last_y = event.y

    def draw(self, event):
        if self.last_x and self.last_y:
            if self.mode: #пользователь нажал на кнопку Ластик
                color = 'white'
            else:
                color = self.brush_color

            width = self.brush_size_slider.get()
            self.canvas.create_line(self.last_x, self.last_y, event.x, event.y, fill=color,width=width)
            self.draw_image.line([self.last_x, self.last_y, event.x, event.y], fill=color, width=width)
            self.last_x = event.x
            self.last_y = event.y







root = tkinter.Tk()
draw = DrawApp(root)


root.mainloop()


#gihub
#pygame