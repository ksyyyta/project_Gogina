"""
Дан первый член A и знаменатель D геометрической прогрессии. Сформировать и
вывести список размера 10, содержащий 10 первых членов данной прогрессии: A,
A* D, A* D2, A*D3, ... .
"""
import random
A = random.randint(1, 10)
D = random.randint(1, 10)

progression = []
for i in range(10):
    progression.append(A * (D ** i))

print(progression)
