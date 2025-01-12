import tkinter as tk
import webbrowser
import subprocess
import ctypes
import requests
import os
import re

from tkinter import messagebox
from tkinter import filedialog
from tkinter import ttk
from tkinter import *

from Dev.pet_projects.mop_organizer.calculator import KM_open
from Dev.pet_projects.mop_organizer.calculator import KV_open


# Две функции для копирования из буфера обмена при русской раскладке клавиатуры
def is_ru_lang_keyboard():
    u = ctypes.windll.LoadLibrary("user32.dll")
    pf = getattr(u, "GetKeyboardLayout")
    return hex(pf(0)) == '0x4190419'


def keys(event):
    if is_ru_lang_keyboard():
        if event.keycode == 86:
            event.widget.event_generate("<<Paste>>")
        elif event.keycode == 67:
            event.widget.event_generate("<<Copy>>")
        elif event.keycode == 88:
            event.widget.event_generate("<<Cut>>")
        elif event.keycode == 65535:
            event.widget.event_generate("<<Clear>>")
        elif event.keycode == 65:
            event.widget.event_generate("<<SelectAll>>")


#  Основные параметры приложения

app = tk.Tk()
app.geometry("650x94+500+400")
app.resizable(True, True)
app.title("Название программы")
app.bind("<Control-KeyPress>", keys)
app.minsize(650, 99)
app.maxsize(650, 440)
app.configure(bg='#DFFFDF')

flag = 0  # Переменная только для функции clop()


def clop():
    global flag
    if flag == 1:
        app.geometry("650x99")
        flag -= 1
    elif flag == 0:
        app.geometry("650x385")
        flag += 1


def search():
    if text_field.get().strip() != "":
        if search_engine.get() == "yandex":
            webbrowser.open('https://ya.ru/search/?text=' + text_field.get())
        elif search_engine.get() == "google":
            webbrowser.open('https://www.google.com/search?q=' + text_field.get())
        elif search_engine.get() == "сбис":
            webbrowser.open('https://sbis.ru/contragents/' + text_field.get())
        elif search_engine.get() == "ebay":
            webbrowser.open(
                'https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw=' + text_field.get())
        elif search_engine.get() == "avito":
            webbrowser.open('https://www.avito.ru/moskva?q=' + text_field.get())
        elif search_engine.get() == "зчб":
            webbrowser.open('https://zachestnyibiznes.ru/search?query=' + text_field.get())
        elif search_engine.get() == "комп":
            webbrowser.open('https://companium.ru/search?query=' + text_field.get())
        elif search_engine.get() == "deal":
            webbrowser.open('https://bitrix24.i-module.ru/crm/deal/details/' + text_field.get() + '/')


def searchBtn():
    search()


def enterBtn(event):
    search()


def skladBtn():
    webbrowser.open(
        'https://docs.google.com/')


def zakupBtn():
    webbrowser.open(
        'https://docs.google.com/')


def companyBtn():
    webbrowser.open(
        'https://bitrix24.i-module.ru/crm/company/list/')


def calcBtn():
    subprocess.Popen(
        'C:\\Windows\\System32\\calc.exe')


def valutesBtn():
    webbrowser.open
    ('https://cash.rbc.ru/converter.html')


def spisokBtn():
    webbrowser.open(
        'https://bitrix24.i-module.ru/services/lists/73/view/0/?list_section_id=')


def reportBtn():
    webbrowser.open(
        'https://docs.google.com/')

def callBtn():
    webbrowser.open(
        'https://bitrix24.i-module.ru/telephony/detail.php')

def tasksBtn():
    webbrowser.open(
        'https://bitrix24.i-module.ru/company/personal/user/2490/tasks/?F_CANCEL=Y&F_SECTION=ADVANCED&F_STATE=sR')
    
def dealsBtn():
    webbrowser.open(
        'https://bitrix24.i-module.ru/crm/deal/category/0/'
    )

# Три функции для заметок

def save_file():
    filepath = filedialog.asksaveasfilename(defaultextension=".doc")
    if filepath != "":
        text = notes.get("1.0", END)
        with open(filepath, "w", encoding='utf-8') as file:
            file.write(text)


def delete_text():
    notes.delete("1.0", END)


def on_closing():
    if notes.get("1.0").strip() != "":
        if messagebox.askokcancel("Внимание", "В заметках есть данные, закрываем программу?"):
            app.destroy()
    else:
        app.destroy()


#  Виджеты основного окна

def clear_text_field():
    text_field.delete(0, END)


search_label = tk.Button(app, text='Поиск', bg='#DFFFDF', activebackground='#DFFFDF', command=clear_text_field)
search_label.place(x=0, y=0)

text_field = tk.Entry(app, width=88)
text_field.place(x=46, y=0)

search_engine = StringVar()
search_engine.set("google")

cl = tk.Button(app, text='><',
               width=3,
               command=clop
               )
cl.place(x=5, y=70)

btn_search = tk.Button(app, text='найти',
                       width=9,
                       command=searchBtn,  # bg='#C7FFFC',#activebackground='#C7FFFC'
                       )
btn_search.place(x=580, y=0)

radio_deal = tk.Radiobutton(app, text='Сделка',
                            value='deal',
                            variable=search_engine,
                            bg='#DFFFDF',
                            activebackground='#DFFFDF'
                            )
radio_deal.place(x=0, y=20)

radio_google = tk.Radiobutton(app, text='Google',
                              value='google',
                              variable=search_engine,
                              bg='#DFFFDF',
                              activebackground='#DFFFDF'
                              )
radio_google.place(x=240, y=25)

radio_yandex = tk.Radiobutton(app, text='Яндекс',
                              value='yandex',
                              variable=search_engine,
                              bg='#DFFFDF',
                              activebackground='#DFFFDF'
                              )
radio_yandex.place(x=240, y=45)

radio_sbis = tk.Radiobutton(app, text='ИНН в СБИС',
                            value='сбис',
                            variable=search_engine,
                            bg='#DFFFDF',
                            activebackground='#DFFFDF'
                            )
radio_sbis.place(x=365, y=25)

radio_zchb = tk.Radiobutton(app, text='в ЗЧБ',
                            value='зчб',
                            variable=search_engine,
                            bg='#DFFFDF',
                            activebackground='#DFFFDF'
                            )
radio_zchb.place(x=480, y=25)

button_calc = tk.Button(app, text='calc',
                        width=3,
                        command=calcBtn, bg='#DFFFDF', activebackground='#DFFFDF'
                        )
button_calc.place(x=570, y=100)

radio_comp = tk.Radiobutton(app, text='в Компаниум',
                            value='комп',
                            variable=search_engine,
                            bg='#DFFFDF',
                            activebackground='#DFFFDF'
                            )
radio_comp.place(x=365, y=45)

radio_ebay = tk.Radiobutton(app, text='eBay',
                            value='ebay',
                            variable=search_engine,
                            bg='#DFFFDF',
                            activebackground='#DFFFDF'
                            )
radio_ebay.place(x=305, y=45)

radio_avito = tk.Radiobutton(app, text='Авито',
                             value='avito',
                             variable=search_engine,
                             bg='#DFFFDF',
                             activebackground='#DFFFDF'
                             )
radio_avito.place(x=305, y=25)

btn_sklad = tk.Button(app, text='складские остатки',
                      width=15,
                      command=skladBtn,
                      bg='#DFFFDF',
                      activebackground='#DFFFDF'
                      )
btn_sklad.place(x=100, y=100)

btn_zakup = tk.Button(app, text='отчёт по закуп.',
                      command=zakupBtn, bg='#DFFFDF', activebackground='#DFFFDF'
                      )
btn_zakup.place(x=430, y=70)

btn_company = tk.Button(app, text='компании',
                        command=companyBtn, bg='#DFFFDF', activebackground='#DFFFDF'
                        )
btn_company.place(x=179, y=70)

btn_valutes = tk.Button(app, text='Р/$/CNY',
                        width=6,
                        command=valutesBtn, bg='#DFFFDF', activebackground='#DFFFDF'
                        )
# btn_valutes.place(x=410, y=70)

btn_spisok = tk.Button(app, text='список товаров', command=spisokBtn, bg='#DFFFDF',
                       activebackground='#DFFFDF')
btn_spisok.place(x=5, y=100)

btn_KM_open = tk.Button(app, text='KM', width=2, command=KM_open, bg='#DFFFDF',
                       activebackground='#DFFFDF')
# btn_KM_open.place(x=125,y=100)

btn_KV_open = tk.Button(app, text='KВ', width=2, command=KV_open, bg='#DFFFDF',
                       activebackground='#DFFFDF')
# btn_KV_open.place(x=155,y=100)

btn_report = tk.Button(app, text='основной отчёт', command=reportBtn, bg='#DFFFDF',
                       activebackground='#DFFFDF')
btn_report.place(x=330, y=70)

btn_calls = tk.Button(app, text='звонки',
                      command=callBtn,
                      width=5,
                      bg='#DFFFDF',
                       activebackground='#DFFFDF')
btn_calls.place(x=132, y=70)

btn_tasks = tk.Button(app, text='задачи',
                      command=tasksBtn,
                      bg='#DFFFDF',
                      width=5,
                      activebackground='#DFFFDF')
btn_tasks.place(x=85, y=70)

btn_deals = tk.Button(app, text='сделки',
                      command=dealsBtn,
                      bg='#DFFFDF',
                      width=5,
                      activebackground='#DFFFDF')
btn_deals.place(x=38, y=70)
# Заметки

notes = Text(width=106,
             height=15,
             bg="#FFFFDA",
             font="TkTextFont"
             )

notes.place(x=5, y=151)

save_button = ttk.Button(text="save",
                         command=save_file,
                         width=4
                         )
save_button.place(x=5, y=126)

# Калькулятор дат
import datetime
from datetime import timedelta


tod = datetime.date.today()
today = datetime.date.strftime(tod, '%d.%m.%Y')
# today = datetime.(tod, "%d-%Y-%H")

today_label = tk.Label(app, text=f"{today}", bg='#DFFFDF')
today_label.place(x=50, y=130)

from_label = tk.Label(app, text="через", bg='#DFFFDF')
from_label.place(x=120, y=130)

def count_days(entry):
    day = get_value_days(entry)
    will_be = tod + timedelta(days=day)
    return will_be

def today_label_name(label, entry):
        val = count_days(entry)
        value = datetime.date.strftime(val, '%d.%m.%Y')
        if value is None:
            label['text'] = "none"
        else:
            label['text'] = f'{value}'
            #label['fg'] = '#DFFFDF'

def count_days_ev(event):
    today_label_name(will_be_label, days_text)




days_text = tk.Entry(app, width=3, bg='#DFFFDF')
days_text.place(x=170, y=130)

days_will_label = tk.Label(app, text="дней/дня будет ", bg='#DFFFDF')
days_will_label.place(x=200, y=130)



will_be = today


will_be_label = tk.Label(app, text=f"{will_be}", bg='#DFFFDF')
will_be_label.place(x=300, y=130)

flag2 = 0  # Переменная только для функции clop2()


def clop2():
    global flag2
    if flag2 == 1:
        app.geometry("650x385")
        flag2 -= 1
    elif flag2 == 0:
        app.geometry("650x450")
        flag2 += 1

clop2_button = tk.Button(app, text='КМ',#bg='#DFFFDF', activebackground='#DFFFDF',
               width=3,
               command=clop2
               )
clop2_button.place(x=610, y=100)

delete_button = ttk.Button(text="clear",
                           width=5,
                           command=delete_text,
                           )

delete_button.place(x=606, y=126)


#  Виджеты и методы калькулятора НДС

def get_value(Entry):
    value = Entry.get()
    try:
        return float(value)
    except ValueError:
        return None

def get_value_days(Entry):
    value = Entry.get()
    try:
        return int(value)
    except ValueError:
        return None


def convert(value):
    if value is None:
        return None
    else:
        return round((100 * value / 120), 2)


def convert2(value):
    if value is None:
        return None
    else:
        return round(get_value(nds_field) - convert(value), 2)


def set_label_text(label, entry):
    value = convert(get_value(entry))
    if value is None:
        label['text'] = "none"
    else:
        label['text'] = f'{value}'
        # app.clipboard_clear()
        # app.clipboard_append(f'{round(value,2)}')


def set_label2_text(label, entry):
    value2 = convert2(get_value(entry))
    if value2 is None:
        label['text'] = "none"
    else:
        label['text'] = f'{value2}'


def s_ndsBtn(event):
    ndsBtn()


def ndsBtn():
    set_label_text(bezndstext_label, nds_field)
    set_label2_text(nds_summ, nds_field)


def copy_nds():
    value3 = convert2(get_value(nds_field))
    app.clipboard_clear()
    app.clipboard_append(f'{round(value3, 2)}')


def copy_beznds():
    value4 = convert(get_value(nds_field))
    app.clipboard_clear()
    app.clipboard_append(f'{round(value4, 2)}')


nds_field = tk.Entry(app, width=8,
                     justify=CENTER,
                     )
nds_field.place(x=45, y=45)
nds_field.insert(0, '0')

nds_label = tk.Label(app, text="С НДС:", bg='#DFFFDF')
nds_label.place(x=0, y=45)

bezndstext_label = ttk.Button(app, width=10, text='', command=copy_beznds)  # bg='#DFFFDF')
bezndstext_label.place(x=140, y=22)

bezndstext_label2 = tk.Label(app, text='Без НДС : ', bg='#DFFFDF')
bezndstext_label2.place(x=80, y=22)

bnds_button = ttk.Button(app, command=set_label_text(bezndstext_label, nds_field))

nds_summ = ttk.Button(app, width=10, text='', command=copy_nds)
nds_summ.place(x=140, y=46)

nds_summ_label = tk.Label(app, text='НДС : ', bg='#DFFFDF')
nds_summ_label.place(x=100, y=46)

nds_summ_Button = ttk.Button(app, command=set_label2_text(nds_summ, nds_field))


# Шаблоны текста

def shablons():
    root = Tk()
    root.title("Текстовые шаблоны")
    root.wm_attributes('-topmost', True)

    def example1():
        app.clipboard_clear()
        app.clipboard_append(f'Поставщик оборудования ООО"Альянс"Право" Industrial Module')

    def example3():
        app.clipboard_clear()
        app.clipboard_append(f'Актуализация контакта ООО"Альянс"Право" Industrial Module')

    def example2():
        app.clipboard_clear()
        app.clipboard_append(
            f'Наша компания ООО «Альянс «Право» ИНН 7806415758 уже более 12ти лет занимается поставками оборудования для промышленной и IT автоматизации.\n'
            f'Мы не реселлер, возим своими силами через налаженные каналы поставок.(Европа, США, Китай)\n'
            f'Среди наших постоянных клиентов такие компании, как Газпром, Сибур, Росатом, Северсталь, РусГидро, Арктик СПГ-2, МГТС.')

    def example4():
        app.clipboard_clear()
        app.clipboard_append(
            f'Ниже список оборудования по нашему профилю.\n'
            f'Из промышленного: Siemens / Mitsubishi / Bently Nevada/ Omron / Allen Bradley / ABB / Schneider /\n'
            f'Pepperl+Fuchs / MTL / Fanuc / B&R / IFM / Sick и прочее импортное оборудование.\n'
            f'Из IT: HPE / Cisco / Dell / IBM / Supermicro / Brocade / Intel / Aruba / Infortrend / Mikrotik / APC и прочее...\n'
            f'Серверы / СХД / Коммутаторы / Модули / Контроллеры / Трансиверы / Частотные преобразователи / Модули ввода вывода и тд.')

    def example5():
        app.clipboard_clear()
        app.clipboard_append(
            f'Если возникнет потребность в оборудовании, направляйте запросы. Постараемся оперативно \n'
            f'предоставить информацию по возможности поставки, цене и срокам.\n\n'
            f'Также просьба подключить нас к рассылке поставщикам на актуальные закупки, если таковая имеется.\n\n'
            f'Будем рады сотрудничеству!')

    btn_shablon1 = tk.Button(root, text='Тема письма', width=16, command=example1)
    btn_shablon1.grid(row=0, column=0)

    btn_shablon3 = tk.Button(root, text='Тема письма 2', width=16, command=example3)
    btn_shablon3.grid(row=0, column=1)

    btn_shablon2 = tk.Button(root, text='Описание компании', width=16, command=example2)
    btn_shablon2.grid(row=1, column=0)

    btn_shablon4 = tk.Button(root, text='Список оборудования', width=18, command=example4)
    btn_shablon4.grid(row=1, column=1)

    btn_shablon5 = tk.Button(root, text='Обращайтесь!', width=16, command=example5)
    btn_shablon5.grid(row=3, column=0)

def shablons():
        app.clipboard_clear()
        app.clipboard_append(
            f'Промышленная автоматизация:   Schneider Electric / ABB / B&R / GM International / Phoenix Contact / EATON / Bently Nevada\n'
            f'Датчики, панели оператора:    Omron / Sick / Fluke/  Pepprl+Fuchs / IFM /  Siemens / Weintek / Beckhoff\n'
            f'Оборудование для спец промышленности:     Sew Eurodrive / Emerson / Honeywell / Allen-Bradley / Yokogawa / APC / Yaskawa\n'
            f'Сетевое оборудование:     Cisco / Moxa / Etherwan / HP / Hirschmann / Symanitron / Huawei\n'
            f'Серверное оборудование и АРМ:     HP / Dell / IBM / Supermicro / Advantech '
            )

btn_brends = tk.Button(app, text='бренды',
                      command=shablons,
                      width=5,
                      bg='#DFFFDF',
                       activebackground='#DFFFDF')
btn_brends.place(x=217, y=100)


# btn_shablon.place(x=435, y=100)

# Виджеты и методы курса валют

response = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
data = response.json()

valutes = (data.get('Valute'))

USD = (valutes.get('USD'))
EUR = (valutes.get('EUR'))
CNY = (valutes.get('CNY'))

usd_price = (USD.get('Value'))
eur_price = (EUR.get('Value'))
cny_price = (CNY.get('Value'))


def usd_kurs(label):
    usd_kurs = (round(usd_price, 2))
    if usd_kurs:
        label['text'] = f'USD : {usd_kurs}р'


def eur_kurs(label):
    eur_kurs = (round(eur_price, 2))
    if eur_kurs:
        label['text'] = f'EUR : {eur_kurs}р'


def cny_kurs(label):
    cny_kurs = (round(cny_price, 2))
    if cny_kurs:
        label['text'] = f'CNY : {cny_kurs}р'


def open_kurs():
    usd_kurs(usd_label)
    eur_kurs(eur_label)
    cny_kurs(cny_label)


valutes_Button = tk.Button(app, width=8, text='Курс ЦБ->',
                           command=open_kurs, )
valutes_Button.place(x=470, y=45)

usd_label = tk.Label(app, width=10, text='', bg='#DFFFDF')
usd_label.place(x=550, y=25)

eur_label = tk.Label(app, width=10, text='', bg='#DFFFDF')
eur_label.place(x=550, y=45)

cny_label = tk.Label(app, width=10, text='', bg='#DFFFDF')
cny_label.place(x=550, y=65)


#  Калькулятор маржи (кнопка на открытие файла с рабочего стола)


def get_desktop_path():
    desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    return desktop_path


def open_KM_desktop():
    file_path = get_desktop_path()
    os.system("start " + (file_path + "\калькулятор.xlsx"))



btn_KM = tk.Button(app, text='калькулятор', command=open_KM_desktop, bg='#DFFFDF',
                   activebackground='#DFFFDF')
btn_KM.place(x=248, y=70)


#  Конвертер валют

def get_my_value(Entry):
    value = Entry.get()
    try:
        return float(value)
    except ValueError:
        return None


def convert_Dollar(value):
    if value is None:
        return None
    else:
        return round(get_my_value(value_field) * round(usd_price, 2), 2)


def convert_Euro(value):
    if value is None:
        return None
    else:
        return round(get_my_value(value_field) * round(eur_price, 2), 2)


def convert_CNY(value):
    if value is None:
        return None
    else:
        return round(get_my_value(value_field) * round(cny_price, 2), 2)


def convert_RUB(value):
    if value is None:
        return None
    else:
        return get_my_value(value_field) * 1


def set_label_USD(label, entry):
    if value_choise.get() == "USD" and value_choise2.get() == "RUB":
        value = convert_Dollar(get_my_value(entry))
        if value is None:
            label['text'] = "none"
        else:
            label['text'] = f'{value}'
    elif value_choise.get() == "USD" and value_choise2.get() == "USD":
        value = get_my_value(entry)
        if value is None:
            label['text'] = "none"
        else:
            label['text'] = f'{value}'
    elif value_choise.get() == "USD" and value_choise2.get() == "EUR":
        value = round(convert_Dollar(get_my_value(entry)) / (round(eur_price, 2)), 2)
        if value is None:
            label['text'] = "none"
        else:
            label['text'] = f'{value}'
    elif value_choise.get() == "USD" and value_choise2.get() == "CNY":
        value = round(convert_Dollar(get_my_value(entry)) / (round(cny_price, 2)), 2)
        if value is None:
            label['text'] = "none"
        else:
            label['text'] = f'{value}'


def set_label_EUR(label, entry):
    if value_choise.get() == "EUR" and value_choise2.get() == "USD":
        value = round(convert_Euro(get_my_value(entry)) / (round(usd_price, 2)), 2)
        if value is None:
            label['text'] = "none"
        else:
            label['text'] = f'{value}'
    elif value_choise.get() == "EUR" and value_choise2.get() == "EUR":
        value = get_my_value(entry)
        if value is None:
            label['text'] = "none"
        else:
            label['text'] = f'{value}'
    elif value_choise.get() == "EUR" and value_choise2.get() == "CNY":
        value = round(convert_Euro(get_my_value(entry)) / (round(cny_price, 2)), 2)
        if value is None:
            label['text'] = "none"
        else:
            label['text'] = f'{value}'
    elif value_choise.get() == "EUR" and value_choise2.get() == "RUB":
        value = convert_Euro(get_my_value(entry))
        if value is None:
            label['text'] = "none"
        else:
            label['text'] = f'{value}'


def set_label_CNY(label, entry):
    if value_choise.get() == "CNY" and value_choise2.get() == "USD":
        value = round(convert_CNY(get_my_value(entry)) / (round(usd_price, 2)), 2)
        if value is None:
            label['text'] = "none"
        else:
            label['text'] = f'{value}'
    elif value_choise.get() == "CNY" and value_choise2.get() == "EUR":
        value = round(convert_CNY(get_my_value(entry)) / (round(eur_price, 2)), 2)
        if value is None:
            label['text'] = "none"
        else:
            label['text'] = f'{value}'
    elif value_choise.get() == "CNY" and value_choise2.get() == "CNY":
        value = get_my_value(entry)
        if value is None:
            label['text'] = "none"
        else:
            label['text'] = f'{value}'
    elif value_choise.get() == "CNY" and value_choise2.get() == "RUB":
        value = convert_CNY(get_my_value(entry))
        if value is None:
            label['text'] = "none"
        else:
            label['text'] = f'{value}'


def set_label_RUB(label, entry):
    if value_choise.get() == "RUB" and value_choise2.get() == "USD":
        value = round((get_my_value(entry)) / (round(usd_price, 2)), 2)
        if value is None:
            label['text'] = "none"
        else:
            label['text'] = f'{value}'
    elif value_choise.get() == "RUB" and value_choise2.get() == "EUR":
        value = round((get_my_value(entry)) / (round(eur_price, 2)), 2)
        if value is None:
            label['text'] = "none"
        else:
            label['text'] = f'{value}'
    elif value_choise.get() == "RUB" and value_choise2.get() == "CNY":
        value = round((get_my_value(entry)) / (round(cny_price, 2)), 2)
        if value is None:
            label['text'] = "none"
        else:
            label['text'] = f'{value}'
    elif value_choise.get() == "RUB" and value_choise2.get() == "RUB":
        value = get_my_value(entry)
        if value is None:
            label['text'] = "none"
        else:
            label['text'] = f'{value}'


def result_btn(event):
    resultBtn()


def resultBtn():
    set_label_USD(result_label, value_field)
    set_label_EUR(result_label, value_field)
    set_label_CNY(result_label, value_field)
    set_label_RUB(result_label, value_field)


def copy_value():
    value = result_label['text']
    app.clipboard_clear()
    app.clipboard_append(f'{value}')


values = ("USD", "EUR", "CNY", "RUB")
values_var = StringVar(value=values[0])
values_var2 = StringVar(value=values[0])

value_choise = ttk.Combobox(app, textvariable=values_var, values=values, width=4)
value_choise.current(0)
value_choise.place(x=365, y=100)

value_choise2 = ttk.Combobox(app, textvariable=values_var2, values=values, width=4)
value_choise2.current(3)
value_choise2.place(x=510, y=100)

value_field = tk.Entry(app, width=10, justify=CENTER)
value_field.place(x=300, y=100)

result_label = ttk.Button(app, width=10, text='', command=copy_value)
result_label.place(x=440, y=98)

r_label = tk.Label(app, width=1, text=' = ', bg='#DFFFDF')
r_label.place(x=420, y=100)


#  Нормальный калькулятор маржи


def get_price(Entry):
    value = Entry.get()
    try:
        return int(value)
    except ValueError:
        return None


def sale_price(value):
    if value is None:
        return None
    else:
        return get_price(zahod_field) + (get_price(zahod_field) * value / 100)


def nalog_price(value):
    if value is None:
        return None
    else:
        return ((get_price(zahod_field) + (get_price(zahod_field) * value / 100)) - get_price(zahod_field)) / 1.2 * 0.2


def durty_marz_price(value):
    if value is None:
        return None
    else:
        return (get_price(zahod_field) + (get_price(zahod_field) * value / 100)) - get_price(zahod_field)


def clean_marz_price(value):
    if value is None:
        return None
    else:
        return ((get_price(zahod_field) + (get_price(zahod_field) * value / 100)) - get_price(
            zahod_field)) - nalog_price(value)


def marz_price_percent(value):
    if value is None:
        return None
    else:
        return (((get_price(zahod_field) + (get_price(zahod_field) * value / 100)) - get_price(
            zahod_field)) - nalog_price(value)) / sale_price(value)


def set_label_bind_func(event):
    set_label_bind()


def set_label_bind():
    set_end_price_label(sale_price_label, marz_field)
    set_nalog_price_label(nalog_price_label, marz_field)
    set_clean_marz_label(clean_marz_label, marz_field)
    set_percent_marz_label(perсent_marz_label, marz_field)
    set_avans_ostatok_summ_label(avans_summ_label, ostatok_zakup_summ_label, avans_value_field, marz_field, zahod_field)
    set_kredit_label(kredit_label, clean_marz_label, perсent_marz_label, avans_value_field, marz_field, zahod_field)


def set_end_price_label(label, entry):
    value = int(sale_price(get_price(entry)))
    if value is None:
        label['text'] = "none"
    else:
        label['text'] = f'{value}'


def set_nalog_price_label(label, entry):
    value = nalog_price(get_price(entry))
    if value is None:
        label['text'] = "none"
    else:
        label['text'] = f'Налог:{round(value)}'


def set_clean_marz_label(label, entry):
    value = (durty_marz_price(get_price(entry))) - nalog_price(get_price(entry))
    if value is None:
        label['text'] = "none"
    else:
        label['text'] = f'{round(value)}'


def set_percent_marz_label(label, entry):
    value = ((durty_marz_price(get_price(entry))) - nalog_price(get_price(entry))) / (
        sale_price(get_price(entry))) * 100
    if value is None:
        label['text'] = "none"
    else:
        if round(value, 1) < 20.0:
            label['text'] = f'{round(value, 1)}'
            label['fg'] = '#E60000'
        else:
            label['text'] = f'{round(value, 1)}'
            label['fg'] = '#000000'


def set_avans_ostatok_summ_label(label, label2, Entry, Entry2, Entry3):
    value = get_price(Entry) * sale_price(get_price(Entry2)) / 100
    value2 = get_price(Entry3) - value
    if value is None:
        label['text'] = "none"
        label2['text'] = "none"
    else:
        label['text'] = f'{int(value)}'
        if int(value2) > 0:
            label2['text'] = f'< закупки на {int(value2)}'
            label2['fg'] = '#E60000'
        else:
            label2['text'] = f'перекрывает закупку'
            label2['fg'] = '#000000'


def set_kredit_label(label, label2, label3, Entry, Entry2, Entry3):
    value = get_price(Entry) * sale_price(get_price(Entry2)) / 100
    value2 = get_price(Entry3) - value
    if get_price(otsrochka_field) > 0:
        value3 = value2 * 0.36 / 365 * (get_price(srok_postavki_field) + get_price(otsrochka_field) + 3)
    else:
        value3 = value2 * 0.36 / 365 * (get_price(srok_postavki_field) + get_price(otsrochka_field))
    value4 = ((durty_marz_price(get_price(marz_field))) - nalog_price(get_price(marz_field))) - value3
    value5 = value4 / (sale_price(get_price(marz_field))) * 100
    if value is None:
        label['text'] = "0"
    else:
        if int(value3) > 0:
            label['text'] = f'{round(value3)}'
            label2['text'] = f'{round(value4)}'
            if round(value5, 1) < 20.0:
                label3['text'] = f'{round(value5, 1)}'
                label3['fg'] = '#E60000'
            else:
                label3['text'] = f'{round(value5, 1)}'
                label3['fg'] = '#000000'

        else:
            label['text'] = "0"


def sale_price_copy():
    value = sale_price_label['text']
    app.clipboard_clear()
    app.clipboard_append(f'{value}')


def avans_price_copy():
    value = avans_summ_label['text']
    app.clipboard_clear()
    app.clipboard_append(f'{value}')


zahod_label = tk.Label(app, text='Закупка:', bg='#DFFFDF')
zahod_label.place(x=5, y=390)

zahod_field = tk.Entry(app, width=8, justify=CENTER)
zahod_field.place(x=60, y=390)

marz_label = tk.Label(app, text='Наценка% :', bg='#DFFFDF')
marz_label.place(x=110, y=390)

marz_field = tk.Entry(app, width=5, justify=CENTER)
marz_field.place(x=180, y=390)

sale_price_labelname = tk.Label(app, text='Продажа :', width=9, bg='#DFFFDF')
sale_price_labelname.place(x=210, y=390)

sale_price_label = ttk.Button(app, text='', width=8, command=sale_price_copy)
sale_price_label.place(x=275, y=388)

clean_marz_name_label = tk.Label(app, text='Маржа :', width=6, bg='#DFFFDF')
clean_marz_name_label.place(x=340, y=390)

clean_marz_label = tk.Label(app, text='', bg='#DFFFDF')
clean_marz_label.place(x=390, y=390)

perсent_marz_name_label = tk.Label(app, text='% Маржи :', width=8, bg='#DFFFDF')
perсent_marz_name_label.place(x=450, y=390)

perсent_marz_label = tk.Label(app, text='', bg='#DFFFDF')
perсent_marz_label.place(x=510, y=390)

kredit_name_label = tk.Label(app, text='Кредит:', bg='#DFFFDF')
kredit_name_label.place(x=550, y=390)

kredit_label = tk.Label(app, text='', bg='#DFFFDF')
kredit_label.place(x=600, y=390)

nalog_price_label = tk.Label(app, text='', width=10, bg='#DFFFDF')
#nalog_price_label.place(x=530, y=390)

# Вторая строка калькулятора маржи

avans_value_label = tk.Label(app, text='Аванс%:', bg='#DFFFDF')
avans_value_label.place(x=5, y=415)


def is_valid(newval):
    return re.match("^\\d{0,3}$", newval) is not None


check = app.register(is_valid), "%P"

avans_value_field = tk.Entry(
    app, width=4, justify=CENTER, validate="key", validatecommand=check)
avans_value_field.place(x=60, y=415)
avans_value_field.insert(0, '100')

avans_summ_name_label = tk.Label(app, text='Сумма аванса :', bg='#DFFFDF')
avans_summ_name_label.place(x=90, y=415)

avans_summ_label = ttk.Button(app, text='', width=8, command=avans_price_copy)
avans_summ_label.place(x=185, y=413)

ostatok_zakup_summ_label = tk.Label(app, text='', bg='#DFFFDF')
ostatok_zakup_summ_label.place(x=250, y=415)

srok_postavki_label = tk.Label(app, text='Срок поставки(дней):', bg='#DFFFDF')
srok_postavki_label.place(x=380, y=415)

srok_postavki_field = tk.Entry(app, width=4, justify=CENTER)
srok_postavki_field.place(x=505, y=415)
srok_postavki_field.insert(0, '56')

otsrocchka_label_name = tk.Label(app, text='Отсрочка:', bg='#DFFFDF')
otsrocchka_label_name.place(x=540, y=415)

otsrochka_field = tk.Entry(app, width=4, justify=CENTER)
otsrochka_field.place(x=603, y=415)
otsrochka_field.insert(0, '0')

otsrochka_field.bind('<Return>', set_label_bind_func)
srok_postavki_field.bind('<Return>', set_label_bind_func)
avans_value_field.bind('<Return>', set_label_bind_func)
zahod_field.bind('<Return>', set_label_bind_func)
marz_field.bind('<Return>', set_label_bind_func)
value_choise.bind("<<ComboboxSelected>>", result_btn)
value_field.bind('<Return>', result_btn)
value_choise2.bind("<<ComboboxSelected>>", result_btn)
nds_field.bind('<Return>', s_ndsBtn)
days_text.bind('<Return>', count_days_ev)
text_field.bind('<Return>', enterBtn)
app.wm_attributes('-topmost', True)
app.protocol("WM_DELETE_WINDOW", on_closing)

if __name__ == '__main__':
    app.mainloop()
