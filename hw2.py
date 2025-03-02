# Завдання 2
import random

def get_numbers_ticket():
    lottery_numbers = set()
    try:
        minn = int(input("Введіть мінімальне число для лотереї: "))
        maxx = int(input("Введіть максимальне число для лотереї: "))
        quantityy = int(input("Введіть кількість чисел для лотереї: "))
        if minn > 0 and maxx < 1000 and quantityy < maxx:
            while len(lottery_numbers) < quantityy:
                lottery_numbers.add(random.randint(minn, maxx))
            return f"Ваші лотерейні числа: {sorted(list(lottery_numbers))}"
    except ValueError:
        return "Некоректний запис даних!!!"
print(get_numbers_ticket())
