class calculator:
    def multiply(self): return a*b
    def divide(self): return a/b
    def plus(self): return a+b
    def minus(self): return a-b
calc = calculator()
while True:
    a = int(input('Введите число а: '))
    b = int(input('Введите число b: '))
    operator = input('Введите оператор +-*/: ')
    if operator == '+':
        print('a + b = ', calc.plus())
    elif operator == '-':
        print('a - b = ', calc.minus())
    elif operator == '*':
        print('a * b = ', calc.multiply())
    elif operator == '/' and b != 0:
        print('a / b = ', calc.divide())
    elif operator == '/' and b == 0:
        try:
            a / b
        except ZeroDivisionError:
            print('Деление на 0 запрещено')
    else:
        print('Программа завершена')
        break

