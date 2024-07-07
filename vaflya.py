# complex_calculator.py

import logging
from abc import ABC, abstractmethod

# Логирование
def setup_logger():
    logger = logging.getLogger('ComplexCalculator')
    logger.setLevel(logging.DEBUG)
    handler = logging.StreamHandler()
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger

logger = setup_logger()

# Принцип единственной ответственности (SRP): Класс для комплексных чисел отвечает только за представление комплексных чисел.
class ComplexNumber:
    def init(self, real: float, imaginary: float):
        self.real = real
        self.imaginary = imaginary

    def repr(self):
        return f"{self.real} + {self.imaginary}i"

# Принцип разделения интерфейса (ISP): Интерфейс для операций, разделённый на отдельные классы для каждой операции.
class Operation(ABC):
    @abstractmethod
    def execute(self, a: ComplexNumber, b: ComplexNumber) -> ComplexNumber:
        pass

class AddOperation(Operation):
    def execute(self, a: ComplexNumber, b: ComplexNumber) -> ComplexNumber:
        # Принцип открытости/закрытости (OCP): Мы можем добавлять новые операции, не изменяя существующий код.
        return ComplexNumber(a.real + b.real, a.imaginary + b.imaginary)

class MultiplyOperation(Operation):
    def execute(self, a: ComplexNumber, b: ComplexNumber) -> ComplexNumber:
        # Принцип открытости/закрытости (OCP): Мы можем добавлять новые операции, не изменяя существующий код.
        real = a.real * b.real - a.imaginary * b.imaginary
        imaginary = a.real * b.imaginary + a.imaginary * b.real
        return ComplexNumber(real, imaginary)

class DivideOperation(Operation):
    def execute(self, a: ComplexNumber, b: ComplexNumber) -> ComplexNumber:
        # Принцип подстановки Барбары Лисков (LSP): Подклассы должны уметь заменять базовый класс без нарушения логики программы.
        denom = b.real2 + b.imaginary2
        real = (a.real * b.real + a.imaginary * b.imaginary) / denom
        imaginary = (a.imaginary * b.real - a.real * b.imaginary) / denom
        return ComplexNumber(real, imaginary)

# Основной файл для запуска
def main():
    num1 = ComplexNumber(1, 2)
    num2 = ComplexNumber(3, 4)

    # Принцип инверсии зависимостей (DIP): Зависящие от абстракций, а не от конкретных реализаций.
    add = AddOperation()
    result_add = add.execute(num1, num2)
    logger.info(f"Addition result: {result_add}")

    multiply = MultiplyOperation()
    result_multiply = multiply.execute(num1, num2)
    logger.info(f"Multiplication result: {result_multiply}")

    divide = DivideOperation()
    result_divide = divide.execute(num1, num2)
    logger.info(f"Division result: {result_divide}")

if __name__ == "main":
    main