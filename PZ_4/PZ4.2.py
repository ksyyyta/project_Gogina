"""
Дано целое число N (> 0). Используя операции деления нацело и взятия остатка от
деления, найти число, полученное при прочтении числа N справа налево.

"""

N = int(input("Введите целое число N (> 0): "))

if N <= 0:
    print("Ошибка: число должно быть больше 0")
else:
    print(f"\nПереворачиваем число {N}:")
    reversed_num = 0
    temp = N

    while temp > 0:
        digit = temp % 10
        reversed_num = reversed_num * 10 + digit
        print(f"Взяли цифру {digit}, перевернутое число стало: {reversed_num}")
        temp = temp // 10

    print(f"\nРезультат: {reversed_num}")