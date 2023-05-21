from data_structure.stack import Stack


# Задание 1.
# Перевести выражение из инфиксной формы в постфиксную форму
# записи.
# Говорят, что выражение записано в инфиксной форме, если знак
# операции (сложения, умножения, вычитания либо деления) стоит между
# своими аргументами, например, 5 + 7. Каждая операция имеет приоритет
# выполнения (сначала выполняются умножение и деление, затем сложение и
# вычитание).
# Для изменения приоритета выполнения операций используются
# круглые скобки. Вычислять значение выражения, записанного в инфиксной
# форме, неудобно. Проще сначала перевести его в постфиксную.
# Для перевода выражения из инфиксной формы в постфиксную с учетом
# приоритетов операций и скобок существует простой алгоритм.
# Алгоритм работает со стеком, в котором хранятся знаки операций.
# Сначала стек пуст. На вход алгоритму подается последовательность лексем
# (числа, скобки или знаки операций), представляющая некоторое
# арифметическое выражение, записанное в инфиксной форме. Результатом
# работы алгоритма является эквивалентное выражение в постфиксной форме.
# Вводятся приоритеты операций: открывающая скобка имеет приоритет
# 0, знаки + и – — приоритет 1 и знаки * и / — приоритет 2.
# 2
# Алгоритм:
# 1. Если не достигнут конец входной последовательности, прочитать
# очередную лексему.
# 1.1. Если прочитан операнд (число), записать его в выходную
# последовательность.
# 1.2. Если прочитана открывающая скобка, положить ее в стек.
# 1.3. Если прочитана закрывающая скобка, вытолкнуть из стека в
# выходную последовательность все до открывающей скобки. Сами скобки
# уничтожаются.
# 1.4. Если прочитан знак операции, вытолкнуть из стека в выходную
# последовательность все операции с большим либо равным приоритетом, а
# прочитанную операцию положить в стек.
# 2. Если достигнут конец входной последовательности, вытолкнуть все
# из стека в выходную последовательность и завершить работу.
# Реализуйте метод to_postfix класса ExpressionConverter в файле
# expression.py и протестируйте класс Expression.

class ExpressionValueError(Exception):
    def __init__(self, text: str):
        self.text = text


class ExpressionConverter:
    operation_priority = {
        '(': 0,
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2,
    }

    @staticmethod
    def __normalize_infix_expression(expression: str) -> str:
        """
        Метод, который учитывает отрицательные значения и приводит инфиксную
        запись выражения к виду пригодному для перевода в постфиксную запись.
        :param expression: str: выражение в строковом представлении.
        :return:
            str: строка представленная в инфиксной записи, в пригодном виде, для работы с отрицательными числами.
        """
        res_str = ""
        for i, symbol in enumerate(expression):
            if not symbol.isdigit() and symbol not in "+-*/() ":
                raise ExpressionValueError(f"Не корректный символ {symbol}, в выражении {expression}")
            if i == 0 and symbol == "-":
                res_str += "0-"
            elif i < len(expression) - 1 and symbol == "(" and expression[i + 1] == "-":
                res_str += "(0"
            else:
                res_str += symbol
        return res_str

    @staticmethod
    def to_postfix(expression: str) -> list:
        result_str = ""
        stack = Stack()
        expression = ExpressionConverter.__normalize_infix_expression(expression)
        operation_value = ExpressionConverter.operation_priority
        for symbol in expression:
            # 1.1. Если прочитан операнд (число), записать его в выходную
            # последовательность
            if symbol.isdigit():
                result_str += symbol

            # 1.2. Если прочитана открывающая скобка, положить ее в стек.
            elif symbol == "(":
                stack.push(symbol)
            # 1.3. Если прочитана закрывающая скобка, вытолкнуть из стека в
            # выходную последовательность все до открывающей скобки. Сами скобки
            # уничтожаются.
            elif symbol == ")":
                while stack.peek() != "(":
                    result_str += stack.peek()
                    stack.pop()
                stack.pop()

            # 1.4. Если прочитан знак операции, вытолкнуть из стека в выходную
            # последовательность все операции с большим либо равным приоритетом, а
            # прочитанную операцию положить в стек.
            elif symbol in "+-*/":
                if len(stack) == 0:
                    stack.push(symbol)
                elif operation_value[symbol] <= operation_value[stack.peek()]:
                    while not stack.is_empty() and operation_value[stack.peek()] >= operation_value[symbol]:
                        result_str += stack.peek()
                        stack.pop()
                    stack.push(symbol)
                else:
                    stack.push(symbol)

        # 2. Если достигнут конец входной последовательности, вытолкнуть все
        # из стека в выходную последовательность и завершить работу.
        while len(stack) != 0:
            result_str += stack.pop()
        return result_str.split()


class Expression:

    def __init__(self, expression: str):
        self.__infix_expression = expression
        self.__postfix_expression = ExpressionConverter.to_postfix(expression)

    @property
    def infix_expression(self):
        return self.__infix_expression

    @property
    def postfix_expression(self):
        return self.__postfix_expression

    def get_expression_value(self):
        '''
        Возвращает значение выражения, записанного в постфиксной форме в поле __postfix_expression
        :return:
        '''
        pass


def execute_application():
    expression_str = "-8+(-3)*(-2)+(-7)*(-6+3*(-4))"
    try:
        postfix_list = ExpressionConverter.to_postfix(expression_str)
        print(postfix_list)
    except ExpressionValueError as e:
        print(e)


if __name__ == '__main__':
    execute_application()
