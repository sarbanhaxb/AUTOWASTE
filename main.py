import tkinter as tk
import tkinter.messagebox
from tkinter import ttk
import colors
import SQL


class MainProg(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.initMainMenu()
        self.db = DATABASE
        self.view_records()

    def initMainMenu(self):
        toolbar = tk.Frame(bg=colors.WHITE, bd=2)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        # Кнопка добавления позиции
        btnDialogNewObject = tk.Button(toolbar,
                                       text='Добавить новый объект',
                                       command=self.openDialogNewObject,
                                       compound=tk.TOP)
        btnDialogNewObject.pack(side=tk.LEFT)

        # Кнопка редактирования позиции
        btnEditDialog = tk.Button(toolbar,
                                    text='Редактировать позицию',
                                    command=self.open_update_dialog,
                                    compound=tk.TOP)
        btnEditDialog.pack(side=tk.LEFT)

        # Кнопка удаления позиции
        btnDelDialog = tk.Button(toolbar,
                                    text='Удалить позицию',
                                    command=self.deletePosition,
                                    compound=tk.TOP)
        btnDelDialog.pack(side=tk.LEFT)

        #дерево на главном экране
        self.tree = ttk.Treeview(self, columns=('id', 'Шифр', 'Название объекта'), height=18, show='headings')
        self.tree.column('id', width=30, anchor='nw')
        self.tree.column('Шифр', width=200, anchor='nw')
        self.tree.column('Название объекта', width=400, anchor='nw')
        self.tree.heading('id', text='id')
        self.tree.heading('Шифр', text='Шифр')
        self.tree.heading('Название объекта', text='Название объекта')
        self.tree.pack()

    def openDialogNewObject(self):
        NewObjectDialog()

    def records(self, num, title):
        self.db.insertObject(num, title)
        self.view_records()

    def redrecords(self, num, title, id):
        self.db.update_object(num, title, id)
        self.view_records()

    def view_records(self):
        self.db.cursor.execute("SELECT id, num, title FROM objects")
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.cursor.fetchall()]

    def open_update_dialog(self):
        try:
            Update(self.tree.item(self.tree.focus())["values"][0])
        except IndexError:
            tk.messagebox.showerror('Ошибка', 'Не выбрана позиция')

    def deletePosition(self):
        try:
            self.db.deletePosition(self.tree.item(self.tree.focus())["values"][0])
        except IndexError:
            tk.messagebox.showerror('Ошибка', 'Не выбрана позиция')
        self.view_records()
        self.db.DBcommit()

class NewObjectDialog(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.initDialog()
        self.view = app

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
        self.btn_ok = ttk.Button(self, text='Добавить', command=self.destroy)
        self.btn_ok.place(x=190, y=110)
        self.btn_ok.bind('<Button-1>',
                         lambda event: self.view.records(self.entry_number.get(), self.entry_title.get()))

        self.grab_set()
        self.focus_set()


class Update(tk.Toplevel):
    def __init__(self, index):
        super().__init__()
        self.__index = index
        self.view = app
        self.db = DATABASE
        self.initEditDialog()

    def initEditDialog(self):
        self.title('Новый объект')
        self.geometry('350x150+400+200')
        self.resizable(False, False)

        #Поле с номером
        self.label_number = ttk.Label(self, text='Шифр объекта')
        self.label_number.place(x=30, y=30)
        self.entry_number = ttk.Entry(self)
        self.entry_number.insert(0, self.db.getObjectNum(self.__index))
        self.entry_number.place(x=150, y=30)

        # Поле с названием
        self.label_title = ttk.Label(self, text='Название объекта')
        self.label_title.place(x=30, y=55)
        self.entry_title = ttk.Entry(self)
        self.entry_title.insert(0, self.db.getObjectTitle(self.__index))
        self.entry_title.place(x=150, y=55)

        #Кнопка отмены
        btn_close = ttk.Button(self, text='Закрыть', command=self.destroy)
        btn_close.place(x=270, y=110)

        #Кнопка применения изменения
        self.btn_ok = ttk.Button(self, text='Применить изменения', command=self.destroy)
        self.btn_ok.place(x=132, y=110)
        self.btn_ok.bind('<Button-1>',
                         lambda event: self.view.redrecords(self.entry_number.get(), self.entry_title.get(), self.__index))

        self.grab_set()
        self.focus_set()


if __name__ == "__main__":
    root = tk.Tk()
    DATABASE = SQL.DataBase()
    app = MainProg(root)
    app.pack()
    root.title("Расчет нормативов образования отходов v.01")
    root.geometry("650x450+300+200")
    root.resizable(False, False)
    root.mainloop()