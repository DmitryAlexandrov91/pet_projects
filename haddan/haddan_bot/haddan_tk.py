"""Приложение haddan."""
import ctypes
import tkinter as tk
from tkinter import ttk

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from constants import FIELD_PRICES
from haddan_bot import glade_farm
from utils import HaddanBot


def is_ru_lang_keyboard():
    """Функция для буфера обмена на англ. языке."""
    u = ctypes.windll.LoadLibrary("user32.dll")
    pf = getattr(u, "GetKeyboardLayout")
    return hex(pf(0)) == '0x4190419'


def keys(event):
    """Функция для буфера обмена на англ. языке."""
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
app.title("haddan.app")
app.bind("<Control-KeyPress>", keys)
app.configure(bg='#FFF4DC')


def tk_glade_farm():
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    char = username_field.get().strip()
    password = password_field.get().strip()

    if char is not None and password is not None:
        SwordS = HaddanBot(char=char, driver=driver)
        SwordS.login_to_game(password)

        glade_farm(driver)


# Панель запуска фарма поляны
glade__farm_lable = tk.Label(
    app,
    text='Фарм поляны.',
    bg='#FFF4DC')
glade__farm_lable.grid(row=0, column=0)

glade__farm_lable_2 = tk.Label(
    app,
    text='Введите имя и пароль от персонажа и нажмите ->',
    bg='#FFF4DC')
glade__farm_lable_2.grid(row=0, column=1)

username_label = tk.Label(app, text='имя', bg='#FFF4DC')
username_label.grid(row=1, column=0)

username_field = tk.Entry(app, width=30)
username_field.grid(row=1, column=1)


password_label = tk.Label(app, text='пароль', bg='#FFF4DC')
password_label.grid(row=2, column=0)

password_field = tk.Entry(app, width=30)
password_field.grid(row=2, column=1)

# Блок Цены ресурсов

res_price_label = tk.Label(
    app,
    text='Цена ресурсов:', bg='#FFF4DC'
)
res_price_label.grid(row=3, column=1)

# text_widget = tk.Text(app, width=20, height=7)
# for key, value in FIELD_PRICES.items():
#     text_widget.insert(tk.END, f"{key}: {value}\n")
# text_widget.grid(row=4, column=1)
price_dict_content = '\n'.join(
    f'{key}: {value}' for key, value in FIELD_PRICES.items())
label = tk.Label(app, text=price_dict_content, bg='#FFF4DC')
label.grid(row=4, column=1)


# Лэйблы ресурсов.
# muhozhor_label = tk.Label(
#     text='мухожор',
#     bg='#FFF4DC'
# )
# muhozhor_label.grid(row=5, column=0)


# podsolnuh_label = tk.Label(
#     text='подсолнух',
#     bg='#FFF4DC'
# )
# podsolnuh_label.grid(row=5, column=0)


glade_farm_start_buttton = tk.Button(
    app,
    text='старт',
    width=9,
    bg='#FFF4DC',
    command=tk_glade_farm
    )
glade_farm_start_buttton.grid(
    row=0, column=3
)




app.wm_attributes('-topmost', True)

if __name__ == '__main__':
    app.mainloop()
