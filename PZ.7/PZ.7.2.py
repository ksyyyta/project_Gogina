"""
Дана строка-предложение. Зашифровать ее, поместив вначале все символы,
расположенные на четных позициях строки, а затем, в обратном порядке, все
символы, расположенные на нечетных позициях (например, строка «Программа»
превратится в «ргамамроП»).
"""
def encrypt_sentence(sentence):
    even_chars = sentence[1::2]
    odd_chars_reversed = sentence[0::2][::-1]
    return even_chars + odd_chars_reversed
input_string = "Программа"
encrypted = encrypt_sentence(input_string)
print(f"Исходная строка: '{input_string}'")
print(f"Зашифрованная строка: '{encrypted}'")

test_string = "Шифрование"
test_result = encrypt_sentence(test_string)
