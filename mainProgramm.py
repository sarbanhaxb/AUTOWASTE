import tkinter as tk
from tkinter import ttk
import colors
import SQL

class MainProg(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.initMainMenu()
        self.DB = SQL.MainBase()

    def initMainMenu(self):
        toolbar = tk.Frame(bg=colors.WHITE, bd=2)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        btnDialogNewObject = tk.Button(toolbar,
                                       text='Добавить новый объект',
                                       command=self.openDialogNewObject,
                                       compound=tk.TOP)
        btnDialogNewObject.pack(side=tk.LEFT)

        btnDialogRedObject = tk.Button(toolbar,
                                       text='Редактировать объект',
                                       command=self.openDialogRedObject,
                                       compound=tk.TOP)
        btnDialogRedObject.pack(side=tk.LEFT)


        #дерево на главном экране
        self.tree = ttk.Treeview(self, columns=('id', 'Шифр', 'Название объекта'), height=10, show='headings')
        self.tree.column('id', width=30, anchor='nw')
        self.tree.column('Шифр', width=200, anchor='nw')
        self.tree.column('Название объекта', width=400, anchor='nw')
        self.tree.heading('id', text='id')
        self.tree.heading('Шифр', text='Шифр')
        self.tree.heading('Название объекта', text='Название объекта')
        self.tree.pack()

    def openDialogNewObject(self):
        NewObjectDialog()

    def openDialogRedObject(self):
        RedObjectDialog()


class NewObjectDialog(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.initDialog()

    def initDialog(self):
        self.title('Новый объект')
        self.geometry('350x150+400+200')
        self.resizable(False, False)

        #Поле ввода шифра
        self.label_num = ttk.Label(self, text='Шифр объекта')
        self.label_num.place(x=30, y=30)
        self.entry_number = ttk.Entry(self)
        self.entry_number.place(x=150, y=30)

        #Поле ввода наименования
        self.label_title = ttk.Label(self, text='Название объекта')
        self.label_title.place(x=30, y=55)
        self.entry_title = ttk.Entry(self)
        self.entry_title.place(x=150, y=55)

        #Кнопка закрытия
        btn_close = ttk.Button(self, text='Закрыть', command=self.destroy)
        btn_close.place(x=270, y=110)

        #Кнопка добавления
        btn_ok = ttk.Button(self, text='Добавить', command=self.destroy)
        btn_ok.place(x=190, y=110)
        btn_ok.bind('<Button-1>')

        self.grab_set()
        self.focus_set()


class RedObjectDialog(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.initDialog()

    def initDialog(self):
        self.title('Редактирование объекта')
        self.geometry('400x200+400+200')
        self.resizable(False, False)