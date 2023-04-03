'''
Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
*Пример:*

2 2
    4
'''
number_a = int(input('введите число А '))
number_b = int(input('введите число Б '))

def func1(a, b):
    if a == 1 and b == 1:
        return 1+1
    elif a == 1 and b != 1:
        return 1+func1(a, b-1)
    elif a != 1 and b == 1:
        return 1+func1(a-1, b)
    return 1+1+func1(a-1, b-1)

print(func1(number_a, number_b))