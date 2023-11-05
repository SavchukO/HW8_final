from datetime import date, datetime, timedelta


def get_birthdays_per_week(users):
    if not users:
        return {}
    current_date = date.today()
    weekdays = {
        0: 'Monday',
        1: 'Tuesday',
        2: 'Wednesday',
        3: 'Thursday',
        4: 'Friday',
        5: 'Saturday',
        6: 'Sunday'
        }
    birthdays_per_week = {day: [] for day in weekdays.values()}
    for user in users:
        name = user['name']
        birthday = user['birthday']
        next_birthday = birthday.replace(year=current_date.year)
        if next_birthday < current_date:
            next_birthday = next_birthday.replace(year=current_date.year + 1)
        # Перевіряємо, чи дата народження потрапляє в наступний тиждень
        if current_date <= next_birthday <= current_date + timedelta(days=7):
            day_of_week = next_birthday.weekday()
            day_name = weekdays[day_of_week]  # Отримуємо назву дня тижня
            # Перевірка, чи день народження падає на вихідний
            if day_name in ['Saturday', 'Sunday']:
                day_name = 'Monday'  # Переносимо на понеділок
            birthdays_per_week[day_name].append(name)
    # видаляємо дні, на які не випадає вітань
    new_dict = {}
    for key, value in birthdays_per_week.items():
        if value != []:
            new_dict[key] = value
    birthdays_per_week = new_dict
    print(birthdays_per_week)
    return birthdays_per_week
if __name__ == "__main__":
    users = []
    result = get_birthdays_per_week(users)
    # Виведення результатів
    for day_name, names in result.items():
        print (f'{day_name}: {', '.join(names)}')