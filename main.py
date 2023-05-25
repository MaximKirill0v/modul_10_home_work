from data_structure.deque import Deque
from collections import deque


# Задание 1.
# Реализуйте структуру данных «Двусторонняя очередь» на основе
# связного списка (LinkedList)
# На ветке dev/class-10.2 в файле deque.py находится шаблон структуры.
# Протестируйте полученную структуру. Сравните работу своей
# структуры с встроенным классом deque модуля collections.


def execute_application():
    print("Работа своей структуры класса Deque: ")
    deq = Deque()
    print(f"Пустая двусторонняя очередь:")
    print(deq)
    print("Добавление элемента в начало очереди:")
    deq.add_first(1)
    print(deq)
    print("Добавление элемента в конец очереди:")
    deq.add_last(2)
    print(deq)
    print("Добавление элемента в начало очереди:")
    deq.add_first(3)
    print(deq)
    print("Добавление элемента в конец очереди:")
    deq.add_last(4)
    print(deq)
    print("Удаление элемента из конца очереди:")
    deq.remove_last()
    print(deq)
    print("Удаление элемента из начала очереди:")
    deq.remove_first()
    print(deq)
    print(f"Длина двусторонней очереди:\n{deq.__len__()}")

    print("\nРабота встроенного класса модуля collections:")
    deq = deque()
    print("Добавление элемента в начало:")
    deq.appendleft(1)
    print(deq)
    print("Добавление элемента в конец:")
    deq.append(2)
    print(deq)
    print("Добавление элемента в начало:")
    deq.appendleft(3)
    print(deq)
    print("Добавление элемента в конец:")
    deq.append(4)
    print(deq)
    print("Удаление элемента из конца очереди:")
    deq.pop()
    print(deq)
    print("Удаление элемента из начала очереди:")
    deq.popleft()
    print(deq)
    print("Добавление в конец очереди элементов итерируемого объекта:")
    deq.extend([10, 20, 30])
    print(deq)
    print("Разворот элементов очереди:")
    deq.reverse()
    print(deq)





if __name__ == '__main__':
    execute_application()
