import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import Tk
from tkinter.ttk import Label, Entry

# Таблица с данными участников команды
def anketa():

    #установка окна, названия и его параметров
    root=Tk()
    root.title("Наша команда")
    root.geometry('650x250')
    
    #создание таблицы
    table = ttk.Treeview(root, columns=("Имя","Git", "Обязанности"), show="headings") #Создание колонок
    
    # Задаем имя колонкам
    table.heading("Имя", text="Имя")
    table.heading("Git", text="GITname")
    table.heading("Обязанности", text="Обязанности")
    table.grid(column=0, row=0)
    
    # Вставка данных таблицы
    table.insert('', 'end', values=("Хабибуллин Д.Х.", "D1lo","Реализация главного класса."))
    table.insert('', 'end', values=(" ", " ","Графический интерфейс."))
    table.insert('', 'end', values=(" ", " ","Сборка проекта."))
    table.insert('', 'end', values=("Залеев А.И.", "AysIQ", "Создание алгоритма"))
    table.insert('', 'end', values=(" "," ", "расчета кредита."))
    table.insert('', 'end', values=("Фатхлисламова Я.А.", "Yana-dota", "Поиск инофрмации и"))
    table.insert('', 'end', values=(" "," ", "создание анкеты."))


    root.mainloop()
