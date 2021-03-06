# 1.5.1 г
import math


def get_input(a) -> float:
    while True:
        print(f'Введите значение {a}: ')
        try:
            return float(input())
        except ValueError as hmm:
            print(f'Введеная строка не является числом.')


def answer(x: float, eps: float):
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


def print_ans(y: float):
    print(f'Ответ: {y}')


def main():
    x = get_input('x')
    eps = get_input('eps')
    y = answer(x, eps)
    print_ans(y)

if __name__ == '__main__':
    main()