import tkinter as tk
from tkinter import messagebox
from data_structure.PriorityQueue import PriorityQueue


class TkinterInterface:

    def __init__(self):
        self.task_list = []
        self.priority_deque = PriorityQueue()
        self.window = tk.Tk()
        self.window.geometry(f"500x500")

        self.window.title("Список задач.")
        self.window.resizable(False, False)

        self.lbl_task = tk.Label(self.window, text="Введите задачу:")
        self.lbl_task.grid(row=0, column=0, columnspan=2, sticky='ws', padx=5)

        self.ent_task = tk.Entry(self.window, width=80)
        self.ent_task.grid(row=1, column=0, columnspan=2, sticky='w', padx=5)

        self.lbl_priority = tk.Label(self.window, text="Введите приоритет задачи:")
        self.lbl_priority.grid(row=2, column=0, columnspan=2, sticky='w', padx=5)

        self.ent_priority = tk.Entry(self.window, width=40)
        self.ent_priority.grid(row=3, column=0, padx=5, sticky='w')

        self.btn_add_task = tk.Button(self.window, text="Добавить задачу в очередь", bd=2, width=30, height=1,
                                      command=self.add_task)
        self.btn_add_task.grid(row=3, column=1, sticky='n')

        self.lbl_out_task = tk.Label(self.window)
        self.lbl_out_task.grid(row=4, columnspan=2, sticky='s')

        self.lbl_line = tk.Label(self.window, text="---" * 30)
        self.lbl_line.grid(row=5, columnspan=2, pady=5)

        self.lbl_change = tk.Label(self.window, text="Изменить приоритет задачи")
        self.lbl_change.grid(row=6, columnspan=2)

        self.lbl_change_task = tk.Label(self.window, text="Введите задачу, приоритет которой хотите поменять:")
        self.lbl_change_task.grid(row=7, columnspan=2, sticky='ws', padx=5)

        self.ent_change_task = tk.Entry(self.window, width=80)
        self.ent_change_task.grid(row=8, columnspan=2, sticky='w', padx=5)

        self.lbl_change_priority = tk.Label(self.window, text="Введите новый приоритет задачи:")
        self.lbl_change_priority.grid(row=9, columnspan=2, sticky='ws', padx=5)

        self.ent_change_priority = tk.Entry(self.window, width=40)
        self.ent_change_priority.grid(row=10, column=0, sticky='w', padx=5)

        self.btn_change_task = tk.Button(self.window, text="Изменить приоритет задачи", bd=2, width=30, height=1,
                                         command=self.change_task)
        self.btn_change_task.grid(row=10, column=1, sticky='n')

        self.lbl_out_change_task = tk.Label(self.window)
        self.lbl_out_change_task.grid(row=11, columnspan=2)

        self.lbl_line = tk.Label(self.window, text="---" * 30)
        self.lbl_line.grid(row=12, columnspan=2, pady=5)

        self.btn_complete_task = tk.Button(self.window, text="Выполнить текущую задачу", bd=2, height=2,
                                           command=self.complete_task)
        self.btn_complete_task.grid(row=13, column=0, sticky='we', padx=5, pady=15)

        self.btn_show_all_task = tk.Button(self.window, text="Показать список задач", bd=2, height=2,
                                           command=self.show_all_task)
        self.btn_show_all_task.grid(row=13, column=1, sticky='we', padx=5, pady=15)

        self.lbl_complete_task = tk.Label(self.window, text="", height=2, anchor='w')
        self.lbl_complete_task.grid(row=14, columnspan=2, sticky='w', padx=5)

        self.lbl_current_task = tk.Label(self.window, text="Текущая задача: ")
        self.lbl_current_task.grid(row=15, columnspan=2, sticky='w', padx=5)

        self.lbl_current = tk.Label(self.window, text="", height=2, anchor='w')
        self.lbl_current.grid(row=16, columnspan=2, sticky='w', padx=5)

        self.btn_exit = tk.Button(self.window, text="Выход", bd=2, width=20, command=self.window.destroy)
        self.btn_exit.grid(columnspan=2)

        self.window.mainloop()

    @staticmethod
    def validate_priority(value: str):
        if value.isdigit():
            if int(value) >= 0:
                return True
        return False

    def repeat_check(self, value: str):
        if value in self.task_list:
            return True
        return False

    def add_task(self):
        if not self.ent_task.get() or not self.ent_priority.get():
            messagebox.showinfo("Внимание!",
                                "Поля 'Введите задачу' и 'Введите приоритет задачи' не должны быть пустыми.")
            return
        if not self.validate_priority(self.ent_priority.get()) and (self.ent_task.get() or self.ent_priority.get()):
            messagebox.showinfo("Внимание!",
                                "Приоритет задачи должен быть натуральным числом не меньшим нуля.")
            return
        if self.repeat_check(self.ent_task.get()):
            messagebox.showinfo("Внимание!", f"Задача '{self.ent_task.get()}' уже есть в списке задач.")
            return
        self.priority_deque.insert(self.ent_task.get(), int(self.ent_priority.get()))
        self.lbl_current.configure(text=f"{self.priority_deque.first_element()}")
        self.task_list.append(self.ent_task.get())
        self.lbl_out_task.configure(text=f"Задача '{self.ent_task.get()}' успешно добавлена в список задач.")
        self.lbl_complete_task.configure(text="")

    def change_task(self):
        if not self.ent_change_task.get() or not self.ent_change_priority.get():
            messagebox.showinfo("Внимание!", "Поля 'Введите задачу, приоритет которой хотите поменять' и 'Введите "
                                             "новый приоритет задачи' не должны быть пустыми.")
            return
        if not self.validate_priority(self.ent_change_priority.get()) and (
                self.ent_change_task.get() or self.ent_change_priority.get()):
            messagebox.showinfo("Внимание!",
                                "Приоритет задачи должен быть натуральным числом не меньшим нуля.")
            return

        found = False
        for task in self.priority_deque.items_priority_queue():
            if task.text == self.ent_change_task.get():
                found = True
                task.priority = int(self.ent_change_priority.get())
                self.priority_deque.sort_priority_queue()
                self.lbl_current.configure(text=f"{self.priority_deque.first_element()}")
                self.lbl_out_change_task.configure(text=f"Значение приоритета задачи {self.ent_change_task.get()}"
                                                        f" успешно заменено на {self.ent_change_priority.get()}")
                return
        if not found:
            messagebox.showinfo("Внимание!", f"Задача '{self.ent_change_task.get()}' в списке задач не найдена.")
            return

    def show_all_task(self):
        if not len(self.priority_deque):
            self.lbl_complete_task.configure(text="Список задач пуст, сначала добавьте задачу.")
        else:
            CurrentTasksInterface(self.priority_deque)

    def complete_task(self):
        if not self.priority_deque.is_empty():
            self.lbl_complete_task.configure(text=f"Задача '{self.priority_deque.first_element().text}' с приоритетом "
                                                  f"{self.priority_deque.first_element().priority} выполнена.")
            self.task_list.remove(self.priority_deque.first_element().text)
            self.lbl_current.configure(text=f"{self.priority_deque.first_element()}")
            self.priority_deque.delete()
            if not self.priority_deque.is_empty():
                self.lbl_current.configure(text=f"{self.priority_deque.first_element()}")
            else:
                self.lbl_current.configure(text="")
        else:
            self.lbl_complete_task.configure(text="Вы выполнили все задачи.")



class CurrentTasksInterface:

    def __init__(self, priority_deque: PriorityQueue):
        self.__priority_deque = priority_deque

        self.window = tk.Tk()
        self.window.geometry()
        self.window.title("Список текущих задач.")

        self.lbl_current_priority_dis = tk.Label(self.window, text="Приоритет задачи", width=20)
        self.lbl_current_priority_dis.grid(row=0, column=0)

        self.lbl_line_dis = tk.Label(self.window, text="|", width=1)
        self.lbl_line_dis.grid(row=0, column=1)

        self.lbl_current_task_dis = tk.Label(self.window, text="Текущая задача", width=40)
        self.lbl_current_task_dis.grid(row=0, column=2)

        self.lbl_line_dis = tk.Label(self.window, text="---" * 30)
        self.lbl_line_dis.grid(row=1, columnspan=3)

        self.installation_lbl_task()

        self.btn_return_tkinter_interface = tk.Button(self.window, text="Вернуться к списку задач", width=30, bd=2,
                                                      command=self.window.destroy)
        self.btn_return_tkinter_interface.grid(columnspan=3, pady=10)

        self.window.mainloop()

    def installation_lbl_task(self):
        for row, task in enumerate(self.__priority_deque.items_priority_queue(), start=2):
            lbl_current_priority = tk.Label(self.window, text=task.priority)
            lbl_current_priority.grid(row=row, column=0)

            lbl_line = tk.Label(self.window, text="|")
            lbl_line.grid(row=row, column=1)

            lbl_current_task = tk.Label(self.window, text=task.text)
            lbl_current_task.grid(row=row, column=2)
