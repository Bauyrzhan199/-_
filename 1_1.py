from tkinter import *
from random import randint
from ALotOfClass import *

ostanovki = ["Талапкер", "Косшы", "Коянды", "Жибек жолы"]
main_window, y, i = Tk(), 0, 0
s = [53, 18, 29, 30]

def chose_car():
    global y
    chose = Toplevel(main_window)
    ex = print_file()
    if y < len(ex):
        Label(chose, text=f"Хороший выбор\nС вас {ex[y][4] * s[y]}").place(relx=0.5, rely=0.5, anchor= "center")
    chose.mainloop()

def click_p():
    global y
    win_click_p = Toplevel(main_window)
    Ex = print_file()
    Label(win_click_p, text="Выберите подходящую машину: ").place(relx=0.5, rely=0.3, anchor="center")
    while y < len(Ex):
        Button(win_click_p, text=Ex[y], command=chose_car).place(relx=0.5, rely=0.4 + 0.1 * y, anchor="center")
        y += 1
    win_click_p.mainloop()

def passenger():
    global i
    win_p = Toplevel(main_window)
    win_p.title("Пассажир")
    Label(win_p, text="Куда вам нужно?").place(relx=0.5, rely=0.3, anchor="center")
    while i < len(ostanovki):
        Button(win_p, text=ostanovki[i], command=click_p).place(relx=0.5, rely=0.4 + 0.1 * i, anchor="center")
        i += 1
    win_p.mainloop()

def driver():
    win_d = Toplevel(main_window)
    win_d.title("Водитель")
    Button(win_d)
    win_d.mainloop()

def boss():
    win_b = Toplevel(main_window)
    win_b.title("Хозяин")
    win_b.mainloop()

main_window.title("Таксопарк Астана")
iam_p = Button(main_window, text="Я пассажир", command=passenger)
iam_d = Button(main_window, text="Я водитель", command=driver)
iam_b = Button(main_window, text="Я хозяин", command=boss)
Label(main_window, text="Добро пожаловать в \"Таксопарк Астаны\"\nДля начала определимся, кто вы?").place(relx=0.5, rely=0.1, anchor="center")
iam_p.place(relx=0.5, rely=0.4, anchor="center")
iam_d.place(relx=0.5, rely=0.5, anchor="center")
iam_b.place(relx=0.5, rely=0.6, anchor="center")
main_window.mainloop()