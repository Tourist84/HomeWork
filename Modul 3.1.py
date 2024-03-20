from datetime import datetime

def get_days_from_today(date):
    # Перетворити рядок дати у форматі 'РРРР-ММ-ДД' у об'єкт datetime.
    input_date = datetime.strptime(date, '%Y-%m-%d')
    
    # Отримати поточну дату.
    current_date = datetime.today()
    
    # Розрахувати різницю між поточною датою та заданою датою.
    difference = current_date - input_date
    
    # Повернути різницю у днях як ціле число.
    return difference.days

# Приклад використання функції:
date = '2022-02-24'
days_difference = get_days_from_today(date)
print(f"Різниця у днях між {date} та поточною датою: {days_difference} днів.")