class Stack:
    def __init__(self):
        self.__data = []

    # push – добавление нового элемента в стек.
    def push(self, value):
        self.__data.append(value)

    # pop – удаление и возврат очередного элемента в порядке «последним пришел, первым вышел» (Last In First Out – LIFO)
    def pop(self):
        return self.__data.pop()

    # peek – возврат очередного элемента в порядке «последним пришел, первым вышел» (LIFO).
    def peek(self):
        return self.__data[-1]

    # size  –  возврат количества элементов в стеке (будет использоваться метод __len__).
    def __len__(self):
        return len(self.__data)

    # is_empty – возврат True, если в стеке нет элементов, иначе возврат False
    def is_empty(self):
        return len(self.__data) == 0

    # строковое представление стека
    def __str__(self):
        return "".join(self.__data)
