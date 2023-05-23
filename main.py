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
# Дополнительное задание 1.
# Стандартный алгоритм перевода из инфиксной формы в постфиксную
# форму записи не учитывает, что в выражении могут участвовать
# отрицательные числа. Напишите метод, который приводит инфиксную форму
# к виду пригодному для перевода в постфиксную форму. Отрицательные числа
# в арифметическом выражение заключаются в круглые скобки, кроме случая
# когда выражение начинается с отрицательного значения.
# Дополнительное задание 2.
# Напишите метод, который проверяет, правильно ли расставлены скобки
# внутри инфиксной записи арифметического выражения.

# Задание 2.
# Реализовать алгоритм вычисления выражения по постфиксной
# (обратной польской) записи.
# Обратная польская нотация или постфиксная нотация — форма записи
# математических и логических выражений, в которой операнды расположены
# перед знаками операций. Выражение читается слева направо.
# Когда в выражении встречается знак операции, выполняется
# соответствующая операция над двумя ближайшими операндами,
# находящимися слева от знака операции. Результат операции заменяет в
# выражении последовательность её операндов и знак, после чего выражение
# вычисляется дальше по тому же правилу. Таким образом, результатом
# вычисления всего выражения становится результат последней вычисленной
# операции.
# Например, выражение (1 + 2) * 4 + 3 в постфиксной нотации будет
# выглядеть так: 1 2 + 4 * 3 +, а результат: 15.
# Реализуйте метод get_expression_value() класса Expression, который
# принимает список, каждый элемент которого содержит неотрицательное
# число или знак операции (+, -, *, /).
# Функция должна вернуть результат вычисления по обратной польской
# записи.
# 2
# Для вычисления значения выражения, записанного в постфиксной
# форме, можно использовать описанный далее алгоритм. На вход подается
# последовательность лексем (числа или знаки операций), представляющая
# некоторое арифметическое выражение, записанное в постфиксной форме.
# Результатом работы алгоритма является значение этого выражения.
# 1. Если не достигнут конец входной последовательности, прочитать
# очередную лексему.
# 2. Если прочитан операнд (число), положить его в стек.
# 3. Если прочитан знак операции, вытолкнуть из стека два операнда и
# положить в стек результат применения прочитанной операции к этим
# операндам, взятым в обратном порядке.
# 4. Если достигнут конец входной последовательности, завершить
# работу. В стеке останется единственное число — значение выражения.


class ExpressionValueError(Exception):
    def __init__(self, text: str):
        self.text = text


class BracketError(Exception):
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
    def __modification_expression(expression: str) -> str:
        """
        Вставляет символы пробелов между операндами и знаками операций.
        :param expression: str: строка, математическое выражение.
        :return:
            str: строка, математическое выражение с расставленными символами пробелов.
        """
        res_str = ""
        for symbol in expression:
            if symbol.isdigit():
                res_str += symbol
            elif symbol in "+-*/()":
                res_str += " " + symbol + " "
        return res_str

    @staticmethod
    def to_postfix(expression: str) -> list:
        result_str = ""
        stack = Stack()
        # учитываем отрицательные числа.
        expression = ExpressionConverter.__normalize_infix_expression(expression)
        # Вставляет символы пробелов между операндами и знаками операций
        expression = ExpressionConverter.__modification_expression(expression)
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
                    result_str += " " + stack.peek()
                    stack.pop()
                stack.pop()
            elif symbol == " ":
                result_str += symbol
            # 1.4. Если прочитан знак операции, вытолкнуть из стека в выходную
            # последовательность все операции с большим либо равным приоритетом, а
            # прочитанную операцию положить в стек.
            elif symbol in "+-*/":
                if len(stack) == 0:
                    stack.push(symbol)
                elif operation_value[symbol] <= operation_value[stack.peek()]:
                    while not stack.is_empty() and operation_value[stack.peek()] >= operation_value[symbol]:
                        result_str += " " + stack.peek()
                        stack.pop()
                    stack.push(symbol)
                else:
                    stack.push(symbol)

        # 2. Если достигнут конец входной последовательности, вытолкнуть все
        # из стека в выходную последовательность и завершить работу.
        while len(stack) != 0:
            result_str += " " + stack.pop()
        return result_str.split()


class Expression:

    def __init__(self, expression: str):
        self.__infix_expression = expression
        self.__postfix_expression = ExpressionConverter.to_postfix(expression)

    @staticmethod
    def __is_valid_expression(expression: str) -> bool:
        """
        Проверяет математическое выражение на корректность ввода.
        :param expression: str: строка, математическое выражение.
        :return:
            True: выражение корректно.
            False: выражение не корректно.
        """
        brackets = {
            "(": ")",
        }
        stack = Stack()
        for i, symbol in enumerate(expression):
            if not symbol.isdigit() and symbol not in "+-*/() ":
                raise ExpressionValueError(f"Не корректный символ {symbol}, в выражении {expression}")
            if symbol in "+-*/" and expression[i + 1] in "+-*/" and i != len(expression) - 1:
                return False
            if symbol in brackets.keys():
                stack.push(symbol)
            elif not stack.is_empty() and symbol == brackets[stack.peek()]:
                stack.pop()
            elif symbol.isdigit() or symbol in "+-*/ ":
                continue
            else:
                return False

        if stack.is_empty():
            return True
        raise BracketError(f"Не корректно расставлены скобки в выражении {expression}")

    def __setattr__(self, key, value):
        if key == "_Expression__infix_expression" and not self.__is_valid_expression(value):
            raise ExpressionValueError(f"Выражение: {value} записано не корректно.")
        else:
            object.__setattr__(self, key, value)

    @property
    def infix_expression(self):
        return self.__infix_expression

    @property
    def postfix_expression(self):
        return self.__postfix_expression

    def get_expression_value(self):
        """
        Возвращает значение выражения, записанного в постфиксной форме в поле __postfix_expression
        :return:
            float: результат математического выражения.
        """
        stack = Stack()
        for symbol in self.postfix_expression:
            if symbol.isdigit():
                stack.push(symbol)

            elif symbol in "+-*/":
                a = int(stack.pop())
                b = int(stack.pop())
                if symbol == "+":
                    stack.push(b + a)
                elif symbol == "-":
                    stack.push(b - a)
                elif symbol == "*":
                    stack.push(b * a)
                else:
                    stack.push(b / a)

        return stack.pop()


def execute_application():
    try:
        expression_1 = Expression("-8 - 3 * (-2) - 7 * (-6 - 3 * (-4))")
        expression_2 = Expression("8 + 3 * 2 + 7 * (6 + 3 * 4)")
        print(f"Выражение: {expression_1.infix_expression} в постфиксной записи имеет вид:",
              *expression_1.postfix_expression)
        print(f"Выражение: {expression_1.infix_expression} = {expression_1.get_expression_value()}")
        print(f"\nВыражение: {expression_2.infix_expression} в постфиксной записи имеет вид:",
              *expression_2.postfix_expression)
        print(f"Выражение: {expression_2.infix_expression} = {expression_2.get_expression_value()}")
    except (ExpressionValueError, BracketError) as e:
        print(e)


if __name__ == '__main__':
    execute_application()
