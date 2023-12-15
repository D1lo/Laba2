# загрузка библиотек и модулей
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import Tk
from tkinter.ttk import Label, Entry
from Raschet import schet
from Raschet import schetik
from tkinter.messagebox import showerror
from anketa import anketa

# Окно приложения
window = Tk()
window.title("Ипотечный калькулятор для юридических лиц")
window.geometry('850x200')

# Функция расчета
def raschet():

    # Извлечение введенных данных, преобразование их в нужные нам типы
    # Проверка данных на правильность ввода
    try:
        znachsum=int(txt.get())
        znachproz=float(txt1.get())
        znachsrok=int(txt2.get())
    except ValueError:
        showerror("ОШИБКА!", "Данные введены некорректно!")
        return [None]
    
    # Проверка данных на правильность ввода
    if znachsum < 0:
        showerror("ОШИБКА!", "Сумма кредита не должна быть меньше нуля!")
        return [None]
    
    if znachproz < 0:
        showerror("ОШИБКА!", "Значение процента не должно быть меньше нуля!")
        return [None]
    
    if znachproz < 0:
        showerror("ОШИБКА!", "Значение срока кредита не должно быть меньше нуля!")
        return [None]
    
    # переводим проценты в десятичную дробь
    znachproz=znachproz/100

    # превращаем года в месяцы, если выбрана первая радиокнопка
    if viddati.get() == False:
        znachsrok=znachsrok*12
    
    # Считывание вида платежа с радиокнопки и его расчет
    if vidcredita.get() == True:

    # Дифференциальный платеж
    
        # Создание окна вывода информации и таблицы
        root=Tk()
        root.title("Таблица дифференцированных платежей (Общие выплаты в конце)")
        root.geometry('850x250')
        table = ttk.Treeview(root, columns=("Месяц", "Дней", "Остаток по кредиту", "Проценты", "Ежемесячная выплата (без %)"), show="headings")
        table.heading("Месяц", text="Месяц")
        table.heading("Дней", text="Дней в месяце")
        table.heading("Остаток по кредиту", text="Остаток по кредиту (руб)")
        table.heading("Проценты", text="Выплаченные проценты (руб)")
        table.heading("Ежемесячная выплата (без %)", text="Ежемесячная выплата (без %)")
        table.grid(column=0, row=0)

        (schet(znachsum, znachproz, znachsrok, table))

    else:
    # Аннуитетный платеж
        # Создание окна вывода информации
        root2=tk.Tk()
        root2.title("Результаты расчетов по аннуитетным платежам")
        root2.geometry("500x70")

        # Расчет данных по кредиту
        (schetik(znachsum, znachproz, znachsrok))

        mounthsum, creditsum, proz = schetik(znachsum, znachproz, znachsrok)

        # Вывод данных по аннуитетному виду платежа
        lblmounth1=ttk.Label(root2, text=f"Размер ежемесячного платежа (руб): {mounthsum}")
        lblmounth1.grid(column=0, row=5)
        lblmounth=ttk.Label(root2, width=16)
        lblmounth.grid(column=1, row=5)

        lblcreditsum1=ttk.Label(root2, text=f"Общий размер выплат по кредиту (руб): {creditsum}")
        lblcreditsum1.grid(column=0, row=6)
        lblcreditsum=ttk.Label(root2, width=16)
        lblcreditsum.grid(column=1, row=6)

        lblprozsum1=ttk.Label(root2, text=f"Процентные выплаты за весь срок (руб): {proz}")
        lblprozsum1.grid(column=0, row=7)
        lblprozsum=ttk.Label(root2, width=16)
        lblprozsum.grid(column=1, row=7)

# Кнопка расчета выплат
btn = ttk.Button(window, text="Рассчитать выплаты по кредиту", command=raschet)
btn.grid(column=1, row=8)

# Поля ввода значений
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
anue = Radiobutton(text='Аннуитетный', variable=vidcredita, value=False)
differ = Radiobutton(text='Дифференцированный', variable=vidcredita, value=True)
anue.grid(column=2, row=0)
differ.grid(column=3, row=0)

btninfo = ttk.Button(window, text="Информация о разработчиках", command=anketa)
btninfo.grid(column=2, row=9)

window.mainloop()
