# Завдання 2
import random

def get_numbers_ticket(min, max, quantity):
    lottery_numbers = set()
    try:
        if 1 <= min <= max <= 1000 and quantity <= max - min:
            while len(lottery_numbers) < quantity:
                lottery_numbers.add(random.randint(min, max))
            return f"Ваші лотерейні числа: {sorted(list(lottery_numbers))}"
        else:
            return list(lottery_numbers)
    except ValueError:
        return list(lottery_numbers)
print(get_numbers_ticket(2, 10, 8))
