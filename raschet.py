from calendar import monthrange
from datetime import datetime

def schet(znachsum, znachproz, znachsrok, table):
# Объявление переменных, необходимых для расчета
znachdlyadati=1 # Номер месяца кредита
ezhe=round(znachsum/znachsrok, 2) #Ежемесячный платеж
obsh=znachsum #Выплаченная сумма за весь период кредита
prozdif=0 # Размер процентных платежей в месяц
obshproz=0 # Размер процентных платежей за весь период кредита
znachsum2=znachsum # Дублируем сумму кредита
monthik=1 #Номер месяца

# Алгоритм расчета и вноса расчитанных значений в таблицу
for i in range(znachsrok):

current_year = (datetime.now().year) # Получение данных о нынешнем годе
days = monthrange(current_year, monthik)[1] # Запись кол-ва дней в месяце в переменную
monthik=monthik+1 # переход к след. месяцу

prozdif=round(((znachsum*znachproz*days)/365), 2) # Формула расчета процентов
table.insert('', 'end', values=(znachdlyadati, days, znachsum, prozdif, ezhe)) # Внесение значений в таблицу

znachdlyadati=znachdlyadati+1 # переход к другому месяцу периода кредита
znachsum=round(znachsum-ezhe, 2) # Остаток по кредиту

obsh=round(obsh+prozdif,3) # Выплаченная суммая по кредиту

if i==(znachsrok-2):
ezhe=znachsum

if monthik==12:
current_year=current_year+1
monthik=1

# Расчет общего кол-ва выплаченных процентов
obshproz=round(obsh-znachsum2,3)

# Вывод данных
table.insert('', 'end', values=("Общая сумма выплат: ",obsh)) # Внесение данных об общем кол-ве платежа
table.insert('', 'end', values=("Общая сумма выплаченных %: ", obshproz)) # Внесение данных об общих выплаченных процентах

def schetik(znachsum, znachproz, znachsrok):
mounthsum=round((znachsum+(znachsum*znachproz))/znachsrok, 2) # Формула расчета ежемесячного платежа
creditsum=round(znachsum+(znachsum*znachproz), 2) # Формула расчета общей суммы кредита
proz=round(znachsum*znachproz, 2) # Расчет суммы выплаченных процентов
return mounthsum, creditsum, proz
from calendar import monthrange
from datetime import datetime

def schet(znachsum, znachproz, znachsrok, table):
# Объявление переменных, необходимых для расчета
znachdlyadati=1 # Номер месяца кредита
ezhe=round(znachsum/znachsrok, 2) #Ежемесячный платеж
obsh=znachsum #Выплаченная сумма за весь период кредита
prozdif=0 # Размер процентных платежей в месяц
obshproz=0 # Размер процентных платежей за весь период кредита
znachsum2=znachsum # Дублируем сумму кредита
monthik=1 #Номер месяца

# Алгоритм расчета и вноса расчитанных значений в таблицу
for i in range(znachsrok):

current_year = (datetime.now().year) # Получение данных о нынешнем годе
days = monthrange(current_year, monthik)[1] # Запись кол-ва дней в месяце в переменную
monthik=monthik+1 # переход к след. месяцу

prozdif=round(((znachsum*znachproz*days)/365), 2) # Формула расчета процентов
table.insert('', 'end', values=(znachdlyadati, days, znachsum, prozdif, ezhe)) # Внесение значений в таблицу

znachdlyadati=znachdlyadati+1 # переход к другому месяцу периода кредита
znachsum=round(znachsum-ezhe, 2) # Остаток по кредиту

obsh=round(obsh+prozdif,3) # Выплаченная суммая по кредиту

if i==(znachsrok-2):
ezhe=znachsum

if monthik==12:
current_year=current_year+1
monthik=1

# Расчет общего кол-ва выплаченных процентов
obshproz=round(obsh-znachsum2,3)

# Вывод данных
table.insert('', 'end', values=("Общая сумма выплат: ",obsh)) # Внесение данных об общем кол-ве платежа
table.insert('', 'end', values=("Общая сумма выплаченных %: ", obshproz)) # Внесение данных об общих выплаченных процентах

def schetik(znachsum, znachproz, znachsrok):
mounthsum=round((znachsum+(znachsum*znachproz))/znachsrok, 2) # Формула расчета ежемесячного платежа
creditsum=round(znachsum+(znachsum*znachproz), 2) # Формула расчета общей суммы кредита
proz=round(znachsum*znachproz, 2) # Расчет суммы выплаченных процентов
return mounthsum, creditsum, proz
