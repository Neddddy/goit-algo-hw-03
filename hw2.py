# Завдання 2
import random

def get_numbers_ticket(min, max, quantity):
    lottery_numbers = set()
    try:
        if min >= 1 and max <= 1000 and min < quantity < max:
            while len(lottery_numbers) < quantity:
                lottery_numbers.add(random.randint(min, max))
            return f"Ваші лотерейні числа: {sorted(list(lottery_numbers))}"
        else:
            return "Некоректний запис даних!!!"
    except ValueError:
        return "Некоректний запис даних!!!"
print(get_numbers_ticket(2, 10, 20))
