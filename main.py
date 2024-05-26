import tkinter as tk
from mainProgramm import MainProg

if __name__ == "__main__":
    root = tk.Tk()
    app = MainProg(root)
    app.pack()
    root.title("Название программы")
    root.geometry("650x450+300+200")
    root.resizable(False, False)
    root.mainloop()