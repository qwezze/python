import tkinter
def add():
    new_lang = lang_enty.get()
    lang_listbox.insert(0, new_lang)


def delete():
    selection = lang_listbox.curselection()
    lang_listbox.delete(selection[0])
root = tkinter.Tk()
root.title('пример 1')

lang_enty = tkinter.Entry()
lang_enty.grid(row=0, column=0, padx=6, pady=6)
tkinter.Button(text='Добавить', command=add).grid(column=1, row=0,  padx=6, pady=6)

lang_listbox = tkinter.Listbox()
lang_listbox.grid(row=1, column=0, columnspan=2,  padx=5, pady=5)

lang_listbox.insert(tkinter.END, 'Python')
lang_listbox.insert(tkinter.END, 'C#')

tkinter.Button(text='Удалить', command=delete).grid(row=2, column=1, padx=5, pady=5)

root.mainloop()