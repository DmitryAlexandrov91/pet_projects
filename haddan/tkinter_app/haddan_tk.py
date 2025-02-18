"""Приложение haddan."""
import ctypes
import tkinter as tk
import webbrowser


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


def searchBtn():
    """Задаёт действие для кнопки id_search_button."""
    search_button_func()


def enterBtn(event):
    """Задаёт действие при нажатии клавиши Enter."""
    search_button_func()


def search_button_func():
    """Основное поведение кнопки id_search_button."""
    if search_field.get().strip() != "":
        if search_engine.get() == "item_sn":
            webbrowser.open(
                'https://haddan.ru/thing.php?id=' + search_field.get()
            )


# Панель поиска.
search_label = tk.Label(app, text='Поиск', bg='#FFF4DC')
search_label.grid(row=0, column=0)

search_field = tk.Entry(app, width=50)
search_field.grid(row=0, column=1)


search_button = tk.Button(
    app,
    text='Найти',
    command=searchBtn,
    bg='#FFF4DC')
search_button.grid(row=0, column=2)

search_engine = tk.StringVar()
search_engine.set("item_sn")

# Опции поисковика.
# Поиск вещи по SN.
radio_sn = tk.Radiobutton(
    app,
    text='SN',
    value='item_sn',
    variable=search_engine,
    bg='#FFF4DC'
)
radio_sn.grid(row=1, column=0)

# Поиск вещи на базаре.
radio_market = tk.Radiobutton(
    app,
    text='Поиск по базару',
    value='market_search',
    variable=search_engine,
    bg='#FFF4DC'
)
radio_market.grid(row=1, column=1)


# Дополнительные параметры приложения.
search_field.bind('<Return>', enterBtn)
app.wm_attributes('-topmost', True)

if __name__ == '__main__':
    app.mainloop()
