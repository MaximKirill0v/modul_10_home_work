import tkinter as tk
from tkinter import ttk


def tk_interface():
    menu_operations = (
        "Добавление пользователя в начало очереди", "Удаление пользователя из очереди",
        "Вывод количества пользователей в очереди", "Вывод всех пользователей в очереди")

    window = tk.Tk()
    window.geometry(f"400x600")
    window.title("Класс двусторонней очереди для работы с пользователями.")
    window.resizable(False, False)

    label_length = tk.Label(window, text="Введите максимальный размер очереди:")
    label_length.grid(row=0, column=0, columnspan=2, sticky='ws', padx=5)

    ent_length = tk.Entry(window)
    ent_length.grid(row=1, column=0, sticky='wn', padx=5)

    btn_1 = tk.Button(window, text="Подтвердить размер очереди", bd=2)
    btn_1.grid(row=1, column=1, sticky='wn')

    label_operations = ttk.Label(window, text="Выберите операцию:")
    label_operations.grid(row=2, column=0, sticky='ws', padx=5)

    combo = ttk.Combobox(window, values=menu_operations, width=53)
    combo.current(0)
    combo.grid(row=3, column=0, columnspan=2, sticky='w', padx=5)

    btn_2 = tk.Button(window, text="Подтвердить операцию", bd=2)
    btn_2.grid(row=4, column=0, sticky='wn', padx=5)

    label_login = tk.Label(window, text='Введите логин:')
    label_login.grid(row=5, column=0, sticky='ws', padx=5)

    ent_log = tk.Entry(window, width=25)
    ent_log.grid(row=6, column=0, sticky='w', padx=5)

    label_password = tk.Label(window, text='Введите пароль')
    label_password.grid(row=5, column=1, sticky='ws', padx=5)

    ent_log = tk.Entry(window, width=29)
    ent_log.grid(row=6, column=1, sticky='w', padx=5)

    window.grid_rowconfigure(0, minsize=15)
    window.grid_rowconfigure(1, minsize=30)
    window.grid_rowconfigure(2, minsize=30)
    window.grid_rowconfigure(3, minsize=12)
    window.grid_rowconfigure(4, minsize=12)
    window.grid_rowconfigure(5, minsize=40)
    window.grid_rowconfigure(6, minsize=20)

    window.grid_columnconfigure(0, minsize=100)
    window.grid_columnconfigure(1, minsize=100)
    window.grid_columnconfigure(2, minsize=100)
    window.grid_columnconfigure(3, minsize=100)
    window.grid_columnconfigure(4, minsize=100)
    window.grid_columnconfigure(5, minsize=100)
    window.grid_columnconfigure(6, minsize=100)
    window.mainloop()
