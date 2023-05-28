from data_structure.LinkedList import LinkedList


class Deque:
    def __init__(self, length: int = 10):
        self.__data = LinkedList()
        self.__length = self.__is_valid_length(length)

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, value):
        self.__length = self.__is_valid_length(value)

    @staticmethod
    def __is_valid_length(value):
        if not isinstance(value, int):
            raise TypeError(f"Длина очереди должна быть числом!")
        if value < 1:
            raise ValueError(f"Размер очереди должен быть больше 0!")
        return value

    # add_first(item) - добавление элемента item в начало
    def add_first(self, item):
        self.__data.add_first(item)

    # add_last(item) - добавление элемента item в конец
    def add_last(self, item):
        self.__data.add_last(item)

    # remove_first() - удаляет и возвращает первый элемент
    def remove_first(self):
        return self.__data.remove_first()

    # remove_last() - удаляет и возвращает последний элемент
    def remove_last(self):
        return self.__data.remove_last()

    # len - возвращает количество элементов
    def __len__(self):
        return len(self.__data)

    # str - строковое представление
    def __str__(self):
        return f"{self.__data}"
