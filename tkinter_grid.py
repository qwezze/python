import tkinter

root = tkinter.Tk()
root.title('grid')
#root.geometry('500x500')

'''
0 1 2 3 4 5
0 1 2 3 4 5
0 1 2 3 4 5 

button_1 = tkinter.Button(text='Button1')
button_1.grid(row=0, column=0)

button_2 = tkinter.Button(text='Button2')
button_2.grid(row=0, column=1)

button_3 = tkinter.Button(text='Button3')
button_3.grid(row=0, column=2)

button_4 = tkinter.Button(text='Button4')
button_4.grid(row=1, column=0)'''

for r in range(3):
    for c in range(3):
        btn = tkinter.Button(text=f'{r}{c}', width=30, height=5)
        btn.grid(row=r, column=c)


root.mainloop()