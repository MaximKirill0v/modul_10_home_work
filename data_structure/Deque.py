from data_structure.LinkedList import LinkedList


class Deque:
    def __init__(self):
        self.__data = LinkedList()

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