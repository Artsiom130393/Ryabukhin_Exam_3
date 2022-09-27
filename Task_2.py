# Напишите функцию, которая возвращает True, если введенный
# текст читается одинаково слева-направо и справа-налево. Иначе – False.

def text(stroka):
    return stroka == stroka[::-1]

print(text('топот'))
print(text('cnjg'))