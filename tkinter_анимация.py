import tkinter
import random

class Animate:
    def __init__(self, root):
        self.root = root
        self.root.title('Animate')
        self.root.geometry('800x600')

        self.canvas = tkinter.Canvas(width=800, height=600, bg='white')
        self.canvas.pack()

        self.shapes = []  # Список для хранения фигур
        self.speeds = []  # Список для хранения скоростей

        for i in range(100):
            figure_type = random.choice(['circle', 'square', 'line'])
            x1 = random.randint(0, 700)
            y1 = random.randint(0, 500)
            size = random.randint(20, 50)

            if figure_type == 'circle':
                x2 = x1 + size
                y2 = y1 + size
                color = random.choice(['red', 'blue', 'yellow', 'orange'])
                shape = self.canvas.create_oval(x1, y1, x2, y2, fill=color)
                self.shapes.append((shape, 'circle'))

                dx = random.choice([-5, -4, -3, 3, 4, 5])
                dy = random.choice([-5, -4, -3, 3, 4, 5])
                self.speeds.append((dx, dy))

            elif figure_type == 'square':
                x2 = x1 + size
                y2 = y1 + size
                color = random.choice(['green', 'purple', 'cyan', 'pink'])
                shape = self.canvas.create_rectangle(x1, y1, x2, y2, fill=color)
                self.shapes.append((shape, 'square'))

                dx = random.choice([-5, -4, -3, 3, 4, 5])
                dy = random.choice([-5, -4, -3, 3, 4, 5])
                self.speeds.append((dx, dy))

            elif figure_type == 'line':
                print(11)
                x2 = x1 + size
                y2 = y1 + size
                color = random.choice(['black', 'gray', 'brown'])
                shape = self.canvas.create_line(x1, y1, x2, y2, fill=color, width=2)
                self.shapes.append((shape, 'line'))

                dx = random.choice([-5, -4, -3, 3, 4, 5])
                dy = random.choice([-5, -4, -3, 3, 4, 5])
                self.speeds.append((dx, dy))


        self.animate()

    def animate(self):
        for i, (shape, figure_type) in enumerate(self.shapes):
            if figure_type in ['circle','square', "line"]:

                self.canvas.move(shape, self.speeds[i][0], self.speeds[i][1])
                shape_coords = self.canvas.coords(shape)
                x1, y1, x2, y2 = shape_coords

                if x1 <= 0 or x2 >= self.canvas.winfo_width():
                    self.speeds[i] = (-self.speeds[i][0], self.speeds[i][1])
                if y1 <= 0 or y2 >= self.canvas.winfo_height():
                    self.speeds[i] = (self.speeds[i][0], -self.speeds[i][1])

        self.root.after(20, self.animate)

root = tkinter.Tk()
animate = Animate(root)
root.mainloop()








'''
добавить возможность генерации 3-х геометрических фигур (круг, квадрат, линия)
'''