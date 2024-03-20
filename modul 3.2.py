import random

def get_numbers_ticket(min_num, max_num, quantity):
    # Перевірка вхідних параметрів
    if min_num < 1 or max_num > 1000 or quantity < 1 or quantity > (max_num - min_num + 1):
        return []

    # Генерування випадкових чисел
    numbers_set = set()
    while len(numbers_set) < quantity:
        numbers_set.add(random.randint(min_num, max_num))

    # Повернення відсортованого списку
    return sorted(list(numbers_set))

# Приклад використання функції:
min_num = 1
max_num = 85
quantity = 7
lottery_numbers = get_numbers_ticket(min_num, max_num, quantity)
print("Випадковий набір чисел:", lottery_numbers)