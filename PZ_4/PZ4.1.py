"""
Дано вещественное число — цена 1 кг конфет. Вывести стоимость 0.1, 0.2, ..., 1 кг
конфет.
"""
price_kg = float(input("Введите цену за 1 кг конфет: "))

print(f"\nЦена за 1 кг: {price_kg} руб.")
print("Вес (кг) | Стоимость (руб.)")
print("-" * 25)

weight = 0.1
while weight <= 1.0:
    cost = price_kg * weight
    print(f"{weight:6.1f}   | {cost:10.2f}")
    weight += 0.1