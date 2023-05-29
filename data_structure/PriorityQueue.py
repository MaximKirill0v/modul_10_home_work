class BasketballPlayer:
    def __init__(self, name: str, points: int):
        self.__name = name
        self.__points = points

    def __lt__(self, other):
        return self.__points < other.__points

    def __str__(self):
        return f"Имя баскетболиста: {self.__name}, Очков за игру: {self.__points}."


class PriorityQueue:
    def __init__(self):
        self.__queue = []

    def __str__(self):
        return ' '.join([str(i) for i in self.__queue])

    # for checking if the queue is empty
    def is_empty(self):
        return len(self.__queue) == 0

    # for inserting an element in the queue
    def insert(self, name, points):
        self.__queue.append(BasketballPlayer(name, points))
        self.__queue.sort()

    # for popping an element based on max priority
    def delete(self):
        return self.__queue.pop().name
