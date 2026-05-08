"""
В исходном текстовом файле (hotline.txt) после фразы «Горячая линия» добавить
фразу «Министерства образования Ростовской области», посчитать количество
произведённых добавлений. Сколько номеров телефонов заканчивается на «03»,
«50». Вывести номера телефонов горячих линий, связанных с ЕГЭ/ГИА.
"""
import re

with open('hotline.txt', 'r', encoding='utf-8') as f:
    text = f.read()
new_text, s = re.subn(r'Горячая линия', r'Горячая линия Министерства образования Ростовской области', text)
with open('hotline.txt', 'w', encoding='utf-8') as f:
    f.write(new_text)
print(f'Добавлений: {s}')
phones = re.findall(r'\d{10,12}', new_text)

count = 0
for p in phones:
    if p.endswith('03'):
        count += 1

count2 = 0
for p in phones:
    if p.endswith('50'):
        count2 += 1

print(f'На 03: {count}')
print(f'На 50: {count2}')

ege_phones = re.findall(r'(\d{10,12})(?=.*(?:ЕГЭ|ГИА))|(?:ЕГЭ|ГИА).*?(\d{10,12})', new_text)
ege_phones = sum([list(filter(None, match)) for match in ege_phones], [])
print(f'Телефоны ЕГЭ/ГИА: {ege_phones}')