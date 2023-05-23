# Дополнительное задание.
# Реализуйте класс стека для работы со строками. Стек должен иметь
# фиксированный размер (ограничение на количество элементов, которое можно
# задать при создании стека).
# Реализуйте набор операций для работы со стеком:
# Добавление строки в стек;
# Удаление и возврат строки из стека;
# Подсчет количества строк в стеке;
# Проверку пустой ли стек;
# Очистку стека;
# Получение значения на вершине стека.
# При старте приложения нужно отобразить меню с помощью, которого
# пользователь может выбрать необходимую операцию
class LengthStackError(Exception):
    def __init__(self, text: str):
        self.text = text


class StackStr:
    def __init__(self, value_length: int):
        self.__data = []
        self.__value_length = value_length

    # Подсчет количества строк в стеке
    def __len__(self):
        return len(self.__data)

    def __is_valid_length(self):
        return len(self.__data) == self.__value_length

    # Добавление строки в стек
    def push(self, value):
        if self.__is_valid_length():
            raise LengthStackError(f"Стек заполнен. Добавление не возможно.")
        self.__data.append(value)

    # Удаление и возврат строки из стека
    def pop(self):
        if self.is_empty():
            raise LengthStackError(f"Стек пуст. Удаление не возможно.")
        return self.__data.pop()

    # Проверку пустой ли стек
    def is_empty(self):
        return len(self.__data) == 0

    # Очистку стека
    def clear(self):
        self.__data.clear()

    # Получение значения на вершине стека
    def peek(self):
        return self.__data[-1]
