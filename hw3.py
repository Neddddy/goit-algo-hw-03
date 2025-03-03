# Завдання 3
import re

def prepare (number):
    # patterns
    pattern = r'^\+380\d{9}$'
    pattern1 = r'^380\d{9}$'
    pattern2 = r'^0\d{9}$'
    number = "".join(re.findall(r'\d|\+', number))
    if re.match(pattern, number):
        return number
    elif re.match(pattern1, number):
        number = "+" + number
        return number
    elif re.match(pattern2, number):
        number = "+38" + number
        return number
    else:
        return "Невірний формат даних!!!"
print(prepare(input("Введіть номер телефону для приведення його до стандартного вигляду: ")))
