#!venv/scripts/python
import tkinter as tk
from tkinter import ttk
from tkinter import *
def KM_open():
    import ctypes
    import re

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

    app = tk.Tk()
    app.title('Калькулятор маржи')
    app.resizable(False, False)
    app.bind("<Control-KeyPress>", keys)
    app.configure(bg='#DFFFDF')
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
            label['text'] = f'Налоговая нагрузка:{round(value)}'


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
    zahod_label.grid(row=0,column=0)

    zahod_field = tk.Entry(app, width=8, justify=CENTER)
    zahod_field.grid(row=0,column=1)

    marz_label = tk.Label(app, text='Наценка% :', bg='#DFFFDF')
    marz_label.grid(row=0,column=2)

    marz_field = tk.Entry(app, width=5, justify=CENTER)
    marz_field.grid(row=0,column=3)

    sale_price_labelname = tk.Label(app, text='Продажа :', width=9, bg='#DFFFDF')
    sale_price_labelname.grid(row=0,column=4)

    sale_price_label = ttk.Button(app, text='', width=8, command=sale_price_copy)
    sale_price_label.grid(row=0,column=5)

    clean_marz_name_label = tk.Label(app, text='Маржа :', width=6, bg='#DFFFDF')
    clean_marz_name_label.grid(row=0,column=6)

    clean_marz_label = tk.Label(app, text='', bg='#DFFFDF')
    clean_marz_label.grid(row=0,column=7)

    perсent_marz_name_label = tk.Label(app, text='% Маржи :', width=8, bg='#DFFFDF')
    perсent_marz_name_label.grid(row=3,column=2)

    perсent_marz_label = tk.Label(app, text='', bg='#DFFFDF')
    perсent_marz_label.grid(row=3,column=3)

    kredit_name_label = tk.Label(app, text='Кредитование:', bg='#DFFFDF')
    kredit_name_label.grid(row=3,column=0)

    kredit_label = tk.Label(app, text='', bg='#DFFFDF')
    kredit_label.grid(row=3,column=1)

    nalog_price_label = tk.Label(app, text='', width=25, bg='#DFFFDF')
    nalog_price_label.grid(row=3,column=4)

    # Вторая строка калькулятора маржи

    avans_value_label = tk.Label(app, text='Аванс%:', bg='#DFFFDF')
    avans_value_label.grid(row=1,column=0)


    def is_valid(newval):
        return re.match("^\\d{0,3}$", newval) is not None


    check = app.register(is_valid), "%P"

    avans_value_field = tk.Entry(app, width=4, justify=CENTER, validate="key", validatecommand=check)
    avans_value_field.grid(row=1,column=1)
    avans_value_field.insert(0, '100')

    avans_summ_name_label = tk.Label(app, text='Сумма аванса :', bg='#DFFFDF')
    avans_summ_name_label.grid(row=1,column=2)

    avans_summ_label = ttk.Button(app, text='', width=8, command=avans_price_copy)
    avans_summ_label.grid(row=1,column=3)

    ostatok_zakup_summ_label = tk.Label(app, text='', bg='#DFFFDF')
    ostatok_zakup_summ_label.grid(row=1,column=4)

    srok_postavki_label = tk.Label(app, text='Срок поставки(дней):', bg='#DFFFDF')
    srok_postavki_label.grid(row=1,column=5)

    srok_postavki_field = tk.Entry(app, width=4, justify=CENTER)
    srok_postavki_field.grid(row=1,column=6)
    srok_postavki_field.insert(0, '56')

    otsrocchka_label_name = tk.Label(app, text='Отсрочка:', bg='#DFFFDF')
    otsrocchka_label_name.grid(row=1,column=7)

    otsrochka_field = tk.Entry(app, width=4, justify=CENTER)
    otsrochka_field.grid(row=1,column=8)
    otsrochka_field.insert(0, '0')

    otsrochka_field.bind('<Return>', set_label_bind_func)
    srok_postavki_field.bind('<Return>', set_label_bind_func)
    avans_value_field.bind('<Return>', set_label_bind_func)
    zahod_field.bind('<Return>', set_label_bind_func)
    marz_field.bind('<Return>', set_label_bind_func)
    app.wm_attributes('-topmost', True)
    #app.protocol("WM_DELETE_WINDOW", on_closing)
    app.mainloop()


def KV_open():
    import requests
    import ctypes

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

    app = tk.Tk()
    app.title('Конвертер валют')
    app.resizable(False, False)
    app.bind("<Control-KeyPress>", keys)
    app.configure(bg='#DFFFDF')
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
    valutes_Button.grid(row=0, column=0)

    usd_label = tk.Label(app, width=10, text='', bg='#DFFFDF')
    usd_label.grid(row=0, column=1)

    eur_label = tk.Label(app, width=10, text='', bg='#DFFFDF')
    eur_label.grid(row=0, column=2)

    cny_label = tk.Label(app, width=10, text='', bg='#DFFFDF')
    cny_label.grid(row=0, column=3)

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
    value_choise.grid(row=1, column=1)

    value_choise2 = ttk.Combobox(app, textvariable=values_var2, values=values, width=4)
    value_choise2.current(3)
    value_choise2.grid(row=1, column=4)

    value_field = tk.Entry(app, width=10, justify=CENTER)
    value_field.grid(row=1, column=0)

    result_label = ttk.Button(app, width=10, text='', command=copy_value)
    result_label.grid(row=1, column=3)

    r_label = tk.Label(app, width=1, text=' = ', bg='#DFFFDF')
    r_label.grid(row=1, column=2)


    value_choise.bind("<<ComboboxSelected>>", result_btn)
    value_field.bind('<Return>', result_btn)
    value_choise2.bind("<<ComboboxSelected>>", result_btn)
    app.wm_attributes('-topmost', True)
    app.mainloop()






