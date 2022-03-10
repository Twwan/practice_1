# 1.5.1 г
import math


def get_input(a):
    while True:
        print(f'Введите значение {a}: ')
        try:
            return float(input())
        except ValueError as exc:
            print(f'Введеная строка не является числом.')


def answer(x, eps):
    summand = 1
    n = 3
    y = 0

    while eps < abs(summand):
        numerator = x**n
        denominator = math.factorial(n)
        summand = float(numerator / denominator)
        y = x + summand
        n += 2
    return y


def print_ans(y):
    print(f'Ответ: {y}')


def main():
    x = get_input('x')
    eps = get_input('eps')
    y = answer(x, eps)
    print_ans(y)

if __name__ == '__main__':
    main()