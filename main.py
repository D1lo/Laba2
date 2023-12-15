import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import Tk
from tkinter.ttk import Label,Entry
# from Raschet import schet
# from Raschet import schetik
from tkinter.messagebox import showerror


window = Tk()
window.title("Ипотечный калькулятор для юридических лиц")
window.geometry('750x100')

def raschet ():
    # try:
    #     znachsum

btn = ttk.Button(window, text= "Рассчитать выплаты по кредиту", command=raschet)
btn.grid(column=1, row=8)

lbl = Label(window, text="Введите сумму кредита (руб) и укажите тип платежей:")
lbl.grid(column=0, row=0)
txt = Entry(window,width=16)
txt.grid(column=1, row=0)
lbl1 = Label(window, text="Введите процентную ставку (%):")
lbl1.grid(column=0, row=1)
txt1 = Entry(window,width=16)
txt1.grid(column=1, row=1)
lbl1 = Label(window, text="Введите срок кредита:")
lbl1.grid(column=0, row=2)
txt2 = Entry(window, width=16)
txt2.grid(column=1, row=2)

# Переключатель вида даты срока кредита
viddati = BooleanVar()
viddati.set(False)
tipsrokayear = Radiobutton(text='лет (года)', variable=viddati, value=False, width=7)
tipsrokamounth = Radiobutton(text='месяцев', variable=viddati, value=True)
tipsrokayear.grid(column=2, row=2)
tipsrokamounth.grid(column=3, row=2)

# Переключатель вида кредита
vidcredita = BooleanVar()
vidcredita.set(False)
anue =
Radiobutton(text='Аннуитетный', variable=vidcredita, value=False)
differ = Radiobutton(text='Дифференцированный', variable=vidcredita, value=True)
anue.grid(column=2, row=0)
differ.grid(column=3, row=0)

window.mainloop()

