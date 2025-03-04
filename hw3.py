# Завдання 3
import re

def normalize_phone (phone_number):
    # patterns
    pattern = r'^\+380\d{9}$'
    pattern1 = r'^380\d{9}$'
    pattern2 = r'^0\d{9}$'
    phone_number = "".join(re.findall(r'\d|\+', phone_number))
    if re.match(pattern, phone_number):
        return phone_number
    elif re.match(pattern1, phone_number):
        phone_number = "+" + phone_number
        return phone_number
    elif re.match(pattern2, phone_number):
        phone_number = "+38" + phone_number
        return phone_number
    else:
        return "Невірний формат даних!!!"
print(normalize_phone(input("Введіть номер телефону для приведення його до стандартного вигляду: ")))
