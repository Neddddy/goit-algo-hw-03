# Завдання 1
from datetime import datetime

def get_days_from_today(date_string):
    try:
        string_to_date = datetime.strptime(date_string, "%Y-%m-%d").date()
        diff = string_to_date - datetime.today().date()
        return diff.days
    except ValueError:
        return "Некоректний запис дати або даних!!!"
    

print(get_days_from_today(input("Введіть дату: ")))