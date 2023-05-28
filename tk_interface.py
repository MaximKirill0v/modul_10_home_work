import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from data_structure.Deque import Deque


class TkinterInterface:

    def __init__(self):
        self.deque = Deque()
        self.login_list = []
        self.window = tk.Tk()
        self.window.geometry(f"400x370")

        self.window.title("Класс двусторонней очереди для работы с пользователями.")
        self.window.resizable(False, False)

        self.label_length = tk.Label(self.window, text="Введите максимальный размер очереди:")
        self.label_length.grid(row=0, column=0, columnspan=2, sticky='ws', padx=5)

        self.ent_length = tk.Entry(self.window)
        self.ent_length.grid(row=1, column=0, sticky='wn', padx=5)

        self.btn_length = tk.Button(self.window, text="Подтвердить размер очереди", bd=2, command=self.clicked_btn_1)
        self.btn_length.grid(row=1, column=1, sticky='wn')

        self.label_operations = ttk.Label(self.window, text="Выберите операцию:", state=tk.DISABLED)
        self.label_operations.grid(row=2, column=0, sticky='ws', padx=5)

        self.menu_operations = (
            "Добавление пользователя в начало очереди", "Добавление пользователя в конец очереди",
            "Удаление пользователя из начала очереди", "Удаление пользователя из конца очереди",
            "Вывод количества пользователей в очереди", "Вывод всех пользователей в очереди")

        self.combo = ttk.Combobox(self.window, values=self.menu_operations, width=53, state=tk.DISABLED)
        self.combo.current(0)
        self.combo.grid(row=3, column=0, columnspan=2, sticky='w', padx=5)

        self.btn_operation = tk.Button(self.window, text="Подтвердить операцию", bd=2, state=tk.DISABLED,
                                       command=self.select)
        self.btn_operation.grid(row=4, column=0, sticky='wn', padx=5)

        self.label_login = tk.Label(self.window, text='Введите логин:', state=tk.DISABLED)
        self.label_login.grid(row=5, column=0, sticky='ws', padx=5)

        self.ent_log = tk.Entry(self.window, width=25, state=tk.DISABLED)
        self.ent_log.grid(row=6, column=0, sticky='w', padx=5)

        self.label_password = tk.Label(self.window, text='Введите пароль', state=tk.DISABLED)
        self.label_password.grid(row=5, column=1, sticky='ws', padx=5)

        self.ent_password = tk.Entry(self.window, width=29, state=tk.DISABLED)
        self.ent_password.grid(row=6, column=1, sticky='w', padx=5)

        self.btn_log_password = tk.Button(self.window, text="Подтвердить логин и пароль", bd=2,
                                          command=self.select_password_login, state=tk.DISABLED)
        self.btn_log_password.grid(row=7, column=0, sticky='w', padx=5)

        self.out_res_lbl = tk.Label(self.window)
        self.out_res_lbl.grid(row=8, column=0, columnspan=2, padx=5, pady=10, sticky='w')

        self.lbl_number_client = tk.Label(self.window, text=f"Количество пользователей в очереди: {len(self.deque)}")
        self.lbl_number_client.grid(row=9, column=0, columnspan=2, padx=5, sticky="wn")

        self.lbl_max_client = tk.Label(self.window, text=f"Максимальное количество пользователей в очереди: 0")
        self.lbl_max_client.grid(row=10, column=0, columnspan=2, padx=5, sticky="wn")

        self.quit_btn = tk.Button(self.window, text="Выход", bd=2, command=self.window.destroy)
        self.quit_btn.grid(row=11, column=0, columnspan=2, pady=5)

        self.window.grid_rowconfigure(0, minsize=15)
        self.window.grid_rowconfigure(1, minsize=30)
        self.window.grid_rowconfigure(2, minsize=30)
        self.window.grid_rowconfigure(3, minsize=12)
        self.window.grid_rowconfigure(4, minsize=12)
        self.window.grid_rowconfigure(5, minsize=40)
        self.window.grid_rowconfigure(6, minsize=20)
        self.window.grid_rowconfigure(7, minsize=30)
        self.window.grid_rowconfigure(8, minsize=70)

        self.window.grid_columnconfigure(0, minsize=100)
        self.window.grid_columnconfigure(1, minsize=100)
        self.window.grid_columnconfigure(2, minsize=100)
        self.window.grid_columnconfigure(3, minsize=100)
        self.window.grid_columnconfigure(4, minsize=100)
        self.window.grid_columnconfigure(5, minsize=100)
        self.window.grid_columnconfigure(6, minsize=100)

        self.window.mainloop()

    def clicked_btn_1(self):
        try:
            value = int(self.ent_length.get())
            self.deque.length = int(value)
            self.lbl_max_client.configure(text=f"Максимальное количество пользователей в очереди: {value}")
            self.ent_length.configure(state=tk.DISABLED)
            self.btn_length.configure(state=tk.DISABLED)
            self.label_operations.configure(state=tk.NORMAL)
            self.combo.configure(state='readonly')
            self.btn_operation.configure(state=tk.NORMAL)
        except ValueError:
            messagebox.showinfo(f"Ошибка", "Максимальный размер очереди должен быть числом!")

    def select(self):
        if self.combo.get() in ("Добавление пользователя в начало очереди", "Добавление пользователя в конец очереди"):
            self.label_login['state'] = tk.NORMAL
            self.ent_log['state'] = tk.NORMAL
            self.label_password['state'] = tk.NORMAL
            self.ent_password['state'] = tk.NORMAL
            self.btn_log_password['state'] = tk.NORMAL

        elif self.combo.get() == "Удаление пользователя из начала очереди":
            self.label_login['state'] = tk.DISABLED
            self.ent_log['state'] = tk.DISABLED
            self.label_password['state'] = tk.DISABLED
            self.ent_password['state'] = tk.DISABLED
            self.btn_log_password['state'] = tk.DISABLED
            if len(self.deque):
                remove_client = self.deque.remove_first()
                self.login_list.remove(remove_client[0])
                self.out_res_lbl.configure(
                    text=f"Пользователь с логином '{remove_client[0]}' и паролем '{remove_client[1]}'\n"
                         f"успешно удалён из начала очереди.")
                self.lbl_number_client.configure(text=f"Количество пользователей в очереди: {len(self.deque)}")
            else:
                messagebox.showinfo("Внимание",
                                    f"Очередь пуста, сначала добавьте пользователя.")

        elif self.combo.get() == "Удаление пользователя из конца очереди":
            self.label_login['state'] = tk.DISABLED
            self.ent_log['state'] = tk.DISABLED
            self.label_password['state'] = tk.DISABLED
            self.ent_password['state'] = tk.DISABLED
            self.btn_log_password['state'] = tk.DISABLED

            if len(self.deque):
                remove_client = self.deque.remove_last()
                self.login_list.remove(remove_client[0])
                self.out_res_lbl.configure(
                    text=f"Пользователь с логином '{remove_client[0]}' и паролем {remove_client[1]}\n"
                         f"успешно удалён из конца очереди.")
                self.lbl_number_client.configure(text=f"Количество пользователей в очереди: {len(self.deque)}")
            else:
                messagebox.showinfo("Внимание",
                                    f"Очередь пуста, сначала добавьте пользователя.")

        elif self.combo.get() == "Вывод всех пользователей в очереди":
            if len(self.deque) == 0:
                messagebox.showinfo("Все пользователи в очереди", f"Очередь пуста.")
            messagebox.showinfo("Все пользователи в очереди", f"{self.deque}")

        elif self.combo.get() == "Вывод количества пользователей в очереди":
            messagebox.showinfo("Количество пользователей очереди", f"Количество пользователей: {len(self.deque)}")

        else:
            self.label_login['state'] = tk.DISABLED
            self.ent_log['state'] = tk.DISABLED
            self.label_password['state'] = tk.DISABLED
            self.ent_password['state'] = tk.DISABLED
            self.btn_log_password['state'] = tk.DISABLED

    def select_password_login(self):
        log = self.ent_log.get()
        password = self.ent_password.get()
        if not log or not password:
            messagebox.showinfo("Внимание", "Заполните поля ввода логина и пароля!")
        else:
            new_client = log, password

            if len(self.deque) == int(self.ent_length.get()):
                messagebox.showinfo("Внимание", "Размер очереди достиг максимума, сначала удалите пользователя!")

            elif self.combo.get() == "Добавление пользователя в начало очереди":
                if new_client[0] in self.login_list:
                    messagebox.showinfo("Внимание.", f"Пользователь с логином '{new_client[0]}' уже есть в очереди. "
                                                     f"Повторите ввод логина.")
                else:
                    self.out_res_lbl.configure(
                        text=f"Пользователь с логином '{new_client[0]}' и паролем '{new_client[1]}'\n"
                             f"успешно добавлен в начало очереди.")
                    self.deque.add_first(new_client)
                    self.lbl_number_client.configure(text=f"Количество пользователей в очереди: {len(self.deque)}")
                    self.login_list.append(log)

            elif self.combo.get() == "Добавление пользователя в конец очереди":
                if new_client[0] in self.login_list:
                    messagebox.showinfo("Внимание", f"Пользователь с логином '{new_client[0]}' "
                                                    f"уже есть в очереди. Повторите ввод логина.")
                else:
                    self.out_res_lbl.configure(
                        text=f"Пользователь с логином '{new_client[0]}' и паролем '{new_client[1]}'\n"
                             f"успешно добавлен в конец очереди.")
                    self.deque.add_last(new_client)
                    self.lbl_number_client.configure(text=f"Количество пользователей в очереди: {len(self.deque)}")
                    self.login_list.append(log)
