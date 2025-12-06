"""
Дан список размера N. Переставить в обратном порядке элементы список,
расположенные между его минимальным и максимальным элементами, включая
минимальный и максимальный элементы.
"""
import random

N = int(input('введите размер списка: ' ))
lst = [random.randint(1, 100) for _ in range(N)]
print("Исходный список:", lst)

min_index = lst.index(min(lst))
max_index = lst.index(max(lst))

start = min(min_index, max_index)
end = max(min_index, max_index)

lst[start:end+1] = lst[start:end+1][::-1]

print("Результат:", lst)
