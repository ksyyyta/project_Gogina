import re
def date(day, month, year):
    day = int(day)
    month = int(month)
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 1 <= day <= 31
    elif month in [4, 6, 9, 11]:
        return 1 <= day <= 30
    elif month == 2:
        return 1 <= day <= 28
    else:
        return False
try:
    with open("dates.txt", "r", encoding="utf-8") as file:
        text = file.read()
    pattern = r'\b(\d{2})\.(\d{2})\.(\d{4})\b'

    for match in re.finditer(pattern, text):
        day, month, year = match.groups()
        if date(day, month, year):
            print(f"{day}.{month}.{year}")
except FileNotFoundError:
    print("Файл dates.txt не найден")