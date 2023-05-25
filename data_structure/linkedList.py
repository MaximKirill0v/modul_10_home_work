class Node:
    def __init__(self, data, link=None):
        self.data = data
        self.link = link

    # str - строковое представление
    def __str__(self):
        return f"{self.data} -> {self.link}"


"""
LinkedList или связный список – это структура данных. 
Связный список обеспечивает возможность создать двустороннюю очередь из каких-либо элементов. 
Каждый элемент такого списка считается узлом (Node). 
В каждом узле есть его значение, а также две ссылки – на предыдущий и на последующий узлы. 
То есть список «связывается» узлами, которые помогают двигаться вверх или вниз по списку. 
Из-за таких особенностей строения из связного списка можно организовать стек, очередь или двустороннюю очередь.
"""


class LinkedList:
    def __init__(self):
        self.__head = None
        self.__length = 0

    def add_first(self, item):
        """ Добавление элемента item в начало списка """
        self.__head = Node(item, self.__head)
        self.__length += 1

    def add_last(self, item):
        """ добавление элемента item в конец списка """
        if self.__head is None:
            self.__head = Node(item, self.__head)
            self.__length += 1
        else:
            current_node = self.__head
            while current_node.link is not None:
                current_node = current_node.link
            current_node.link = Node(item)
            self.__length += 1

    def remove_first(self):
        """ удаляет и возвращает первый элемент из начала списка """
        item = self.__head.data
        self.__head = self.__head.link
        self.__length -= 1
        return item

    def remove_last(self):
        """ удаляет и возвращает последний элемент из конца списка """
        if self.__head.link is None:
            item = self.__head.data
            self.__head = self.__head.link
            self.__length -= 1
            return item
        else:
            current_node = self.__head
            while current_node.link.link is not None:
                current_node = current_node.link
            item = current_node.link.data
            current_node.link = None
            self.__length -= 1
            return item

    def __len__(self):
        """ возвращает количество элементов в списке """
        return self.__length

    # str - строковое представление
    def __str__(self):
        return f"{self.__head}"


    def items(self):
        """ возвращает итератор, который последовательно возвращает каждый элемент"""
        if self.__head is not None:
            current_node = self.__head
            yield current_node.data
            while current_node.link is not None:
                current_node = current_node.link
                yield current_node.data