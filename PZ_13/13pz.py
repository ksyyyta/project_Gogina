"""
В исходном текстовом файле (hotline.txt) после фразы «Горячая линия» добавить
фразу «Министерства образования Ростовской области», посчитать количество
произведённых добавлений. Сколько номеров телефонов заканчивается на «03»,
«50». Вывести номера телефонов горячих линий, связанных с ЕГЭ/ГИА.

"""
import re

with open('hotline.txt', 'r', encoding='utf-8') as f:
    text = f.read()
new_text, count = re.subn(
    r'Горячая линия',
    r'Горячая линия Министерства образования Ростовской области',
    text
)

with open('hotline.txt', 'w', encoding='utf-8') as f:
    f.write(new_text)

print(f'Добавлений: {count}')
phones = re.findall(r'\d{10,12}', new_text)

end_03 = sum(1 for p in phones if p.endswith('03'))
end_50 = sum(1 for p in phones if p.endswith('50'))

print(f'На 03: {end_03}')
print(f'На 50: {end_50}')

ege_phones = re.findall(r'(\d{10,12})(?=.*(?:ЕГЭ|ГИА))|(?:ЕГЭ|ГИА).*?(\d{10,12})', new_text, re.IGNORECASE)
ege_phones = [p for match in ege_phones for p in match if p]

print(f'Телефоны ЕГЭ/ГИА: {ege_phones}')