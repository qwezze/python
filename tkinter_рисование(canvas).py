#canvas
import tkinter

root = tkinter.Tk()
root.title('Canvas')
root.geometry('300x300')

canvas = tkinter.Canvas(bg='white', width=250, height=250)
canvas.pack()

canvas.create_line(10, 10, 200, 50)
canvas.create_line(0, 0, 250, 250)
canvas.create_line(250, 0, 0, 250, fill='yellow', width=5)
canvas.create_rectangle(10, 20, 200, 60, fill='#0f0', outline='red')
canvas.create_rectangle(30, 20, 200, 10, fill="#f00")


canvas.create_oval(10, 10, 200, 50, fill='#80c', outline='blue')
canvas.create_polygon(10, 10, 30, 40, 100, 20)
canvas.create_polygon(10, 30, 200, 200, 200, 30, fill='red')

canvas.create_arc((10, 10),(200, 200))

canvas.create_text(50, 50, text='hello', font=(None, 44))

image = tkinter.PhotoImage(file='img.png')
canvas.create_image(250//2, 250//2, image=image)

btn = tkinter.Button(text='Добавить')

canvas.create_window(10, 10, window=btn)
root.mainloop()