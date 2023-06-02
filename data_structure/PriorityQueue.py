class ProblemBook:
    def __init__(self, text: str, priority: int):
        self.text = text
        self.priority = priority

    def __lt__(self, other):
        return self.priority > other.priority

    def __str__(self):
        return f"Задача: {self.text}, Приоритет: {self.priority}.\n"


class PriorityQueue:
    def __init__(self):
        self.__queue = []

    def __str__(self):
        return ' '.join([str(i) for i in self.__queue])

    # for checking if the queue is empty
    def is_empty(self):
        return len(self.__queue) == 0

    # for inserting an element in the queue
    def insert(self, text, priority):
        self.__queue.append(ProblemBook(text, priority))
        self.__queue.sort()

    def sort_priority_queue(self):
        self.__queue.sort()

    # возвращает первый элемент очереди
    def first_element(self):
        return self.__queue[0]

    # for popping an element based on max priority
    def delete(self):
        return self.__queue.pop(0)

    # возвращает итератор, который последовательно возвращает каждый элемент
    def items_priority_queue(self):
        for item in self.__queue:
            yield item

    def __len__(self):
        return len(self.__queue)
