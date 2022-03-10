# 1.5.1 г
import math


def input_x():
    x = float(input('Введите значение аргумента x: '))
    return x


def input_eps():
    eps = float(input('Введите точность вычисления EPS(ε): '))
    return eps


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

    print('Ответ:', y)


def main():
    x = input_x()
    eps = input_eps()
    y = answer(x, eps)


if __name__ == "__main__":
    main()