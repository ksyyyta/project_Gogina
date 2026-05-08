"""
Дан список размера N. Найти номер его последнего локального максимума
(локальный максимум — это элемент, который больше любого из своих соседей).
"""
import random


def find_last_local_max_index(arr):
    n = len(arr)
    if n == 0:
        return None
    elif n == 1:
        return 0

    last_local_max_index = -1

    if arr[0] > arr[1]:
        last_local_max_index = 0

    for i in range(1, n - 1):
        if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
            last_local_max_index = i
    if arr[n - 1] > arr[n - 2]:
        last_local_max_index = n - 1

    return last_local_max_index if last_local_max_index != -1 else None


N = 10
random_list = [random.randint(1, 100) for _ in range(N)]

print("Сгенерированный список:", random_list)
result = find_last_local_max_index(random_list)

if result is not None:
    print(f"Номер последнего локального максимума: {result}")
    print(f"Значение последнего локального максимума: {random_list[result]}")
else:
    print("В списке нет локальных максимумов")
