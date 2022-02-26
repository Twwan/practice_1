# Неборский Мирон 421-4 1.5.1г
import math

x = float(input('Введите значение аргумента x: '))
eps = float(input('Введите точность вычисления EPS(ε): '))

summand = 1
n = 3
y = 0
while eps < abs(summand):
    numerator = x**n
    denominator = math.factorial(n)
    summand = float(numerator / denominator)
    y = x + summand
    n += 2

print('Ответ:', y)
