# Завдання 3
import re

def prepare (numbers):
    # patterns
    pattern = r'^\+380\d{9}$'
    pattern1 = r'^380\d{9}$'
    pattern2 = r'^0\d{9}$'
    # lists
    r_numbers = []
    gotovi_nomera = []
    for number in numbers:
        clean_number = "".join(re.findall(r'\d|\+', number))  # Витягуємо тільки цифри та "+"
        r_numbers.append(clean_number)
    # r_numbers v gotovi_numbers
    for number1 in r_numbers:
        if re.match(pattern, number1):
            gotovi_nomera.append(number1)
        elif re.match(pattern1, number1):
            number1 = "+" + number1
            gotovi_nomera.append(number1)
        elif re.match(pattern2, number1):
            number1 = "+38" + number1
            gotovi_nomera.append(number1)
    # perevirka na errors
    if len(gotovi_nomera) == 0:
        return "Невірний формат даних!!!"
    else:
        return gotovi_nomera
print(prepare(input("Введіть номери телефонів через кому: ").split(',')))
