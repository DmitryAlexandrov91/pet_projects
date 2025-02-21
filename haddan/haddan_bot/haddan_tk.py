"""Приложение haddan."""
import ctypes
import tkinter as tk

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from haddan_bot import glade_farm
from utils import HaddanBot


GLADE_PRICES = {
    'Мухожор': 9,
    'Подсолнух': 17,
    'Капустница': 30,
    'Мандрагора': 50,
    'Зеленая массивка': 67,
    'Колючник Черный': 101,
    'Гертаниум': 210
}


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
    f'{key}: {value}' for key, value in GLADE_PRICES.items())
price_label = tk.Label(app, text=price_dict_content, bg='#FFF4DC')
price_label.grid(row=4, column=1)


# Блок изменения цены ресурсов.
def label_update():
    price_dict_content = '\n'.join(
        f'{key}: {value}' for key, value in GLADE_PRICES.items())
    price_label['label'] = price_dict_content


def price_change(label, field):
    new_price = field.get().strip()
    if new_price:
        GLADE_PRICES[label['text']] = new_price


# Мухожор
muhozhor_label = tk.Label(
    text='Мухожор',
    bg='#FFF4DC'
)
muhozhor_label.grid(row=5, column=0)

muhozhor_field = tk.Entry(
    app, width=5
)
muhozhor_field.grid(row=5, column=1)

muhozhor_button = tk.Button(
    app,
    text='изменить',
    width=9,
    bg='#FFF4DC',
    command=price_change(muhozhor_label, muhozhor_field)
    )
muhozhor_button.grid(row=5, column=2)

# Подсолнух
podsolnuh_label = tk.Label(
    text='Подсолнух',
    bg='#FFF4DC'
)
podsolnuh_label.grid(row=6, column=0)

podsolnuh_field = tk.Entry(
    app, width=5
)
podsolnuh_field.grid(row=6, column=1)

# Капустница
kapusta_label = tk.Label(
    text='Капустница',
    bg='#FFF4DC'
)
kapusta_label.grid(row=7, column=0)

kapusta_field = tk.Entry(
    app, width=5
)
kapusta_field.grid(row=7, column=1)


# Мандрагора
mandragora_label = tk.Label(
    text='Мандрагора',
    bg='#FFF4DC'
)
mandragora_label.grid(row=8, column=0)

mandragora_field = tk.Entry(
    app, width=5
)
mandragora_field.grid(row=8, column=1)

# Зеленая Массивка
green_mass_label = tk.Label(
    text='Зеленая массивка',
    bg='#FFF4DC'
)
green_mass_label.grid(row=9, column=0)

green_mass_field = tk.Entry(
    app, width=5
)
green_mass_field.grid(row=9, column=1)

# Колючник Черный
koluchka_label = tk.Label(
    text='Колючник Черный',
    bg='#FFF4DC'
)
koluchka_label.grid(row=10, column=0)

koluchka_field = tk.Entry(
    app, width=5
)
koluchka_field.grid(row=10, column=1)

# Гертаниум
gertanium_label = tk.Label(
    text='Гертаниум',
    bg='#FFF4DC'
)
gertanium_label.grid(row=11, column=0)

gertanium_field = tk.Entry(
    app, width=5
)
gertanium_field.grid(row=11, column=1)


glade_farm_start_buttton = tk.Button(
    app,
    text='старт',
    width=9,
    bg='#FFF4DC',
    command=tk_glade_farm
    )
glade_farm_start_buttton.grid(
    row=0, column=2
)

app.wm_attributes('-topmost', True)

if __name__ == '__main__':
    app.mainloop()
