import tkinter
cl = 0

root = tkinter.Tk()
root.title('Приложение на tkinter')
root.geometry('500x500')


#.ico
#root.iconbitmap(default='favicon.ico')


icon = tkinter.PhotoImage(file='img.png')
root.iconphoto(False, icon)

root.resizable(False, False)


#добавление виждетов

login_label = tkinter.Label(text='Логин', font=('Tahoma', 33), background='green', foreground='white', width=10, height=1, padx=5)
login_label.pack()
'''
0-F
rgb
fff -> белый
000 -> черный
f00 -> красный
0f0 -> зеленый
4f8
'''
entry_login = tkinter.Entry(width=10, background='#59a', font=('Tahoma', 33))
entry_login.pack()
def click():
    global cl
    cl += 1
    login_label['text'] = f'{cl}'
    print(en.get())
    print(lang.get())
    print(lang_list.curselection())
    lang_list.delete(lang_list.curselection())
    lang_list.insert(0, 'PHP')
    print(lang_list.size())



button = tkinter.Button(text='Добавить', command=click)
button.pack()




#позиционирование виждетов
#pach()
#grid()



#checkbox

en = tkinter.IntVar()

on = tkinter.Checkbutton(text='Включить',variable=en)
on.pack()


#radiobutton

lang = tkinter.StringVar()

r1 = tkinter.Radiobutton(text='Python', value='Python', variable=lang)
r1.pack()

r2 = tkinter.Radiobutton(text='JS', value='JS', variable=lang)
r2.pack()

r3 = tkinter.Radiobutton(text='Java', value='Java', variable=lang)
r3.pack()


#listbox
langs = ['Python', 'JS', 'Java']
langs_v = tkinter.Variable(value=langs)
lang_list = tkinter.Listbox(listvariable=langs_v)
lang_list.pack()



root.mainloop()
