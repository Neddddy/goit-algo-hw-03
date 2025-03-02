# Завдання 2
# Не робив перевірку для введених даних в функції тому, що не знаю як запускати функцію, і вже в ній запитувати дані
import random

lottery_numbers = set()
def get_numbers_ticket(min, max, quantity):
    try:
        while len(lottery_numbers) < int(quantity):
            lottery_numbers.add(random.randint(int(min), int(max)))
        return f"Ваші лотерейні числа: {sorted(list(lottery_numbers))}"
    except ValueError:
        return "Некоректний запис даних!!!"
print(get_numbers_ticket(
input("Введіть мінімальне число для лотереї: "),
input("Введіть максимальне число для лотереї: "),
input("Введіть кількість чисел для лотереї: ")))
