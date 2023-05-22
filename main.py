from data_structure.stack import Stack


# Задание 1.
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
    def __check_expression(expression: str) -> bool:
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
        for symbol in expression:
            if not symbol.isdigit() and symbol not in "+-*/() ":
                raise ExpressionValueError(f"Не корректный символ {symbol}, в выражении {expression}")
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
        return False

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
        # проверка на корректность выражения.
        check_expression = ExpressionConverter.__check_expression(expression)
        if check_expression:
            # учитываем отрицательные числа.
            expression = ExpressionConverter.__normalize_infix_expression(expression)
            # Вставляет символы пробелов между операндами и знаками операций
            expression = ExpressionConverter.__modification_expression(expression)
            operation_value = ExpressionConverter.operation_priority
        else:
            raise BracketError(f"Не корректно расставлены скобки в выражении: {expression}.")
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
        print(f"Выражение '{expression_1.infix_expression}' в постфиксной записи имеет вид:",
              *expression_1.postfix_expression)
        print(f"Выражение {expression_1.infix_expression} = {expression_1.get_expression_value()}")
    except (ExpressionValueError, BracketError) as e:
        print(e)


if __name__ == '__main__':
    execute_application()
