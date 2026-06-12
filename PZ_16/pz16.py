"""
Создайте класс «Календарь», который имеет атрибуты год, месяц и день. Добавьте
методы для определения дня недели, проверки на високосный год и определения
количества дней в месяце.
"""
from datetime import date

class Calendar:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def is_leap_year(self, year):
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

    def days_in_month(self, year, month):
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if month == 2 and self.is_leap_year(year):
            return 29
        return days[month - 1]

    def get_weekday(self, year, month, day):
        return date(year, month, day).strftime("%A")

    def check_leap_year(self):
        return self.is_leap_year(self.year)

    def get_days_in_month(self):
        return self.days_in_month(self.year, self.month)

    def get_weekday_name(self):
        return self.get_weekday(self.year, self.month, self.day)

    def show_info(self):
        return (f"Date: {self.day}.{self.month}.{self.year}\n"
                f"Weekday: {self.get_weekday_name()}\n"
                f"Leap year: {'Yes' if self.check_leap_year() else 'No'}\n"
                f"Days in month: {self.get_days_in_month()}")

calendar = Calendar(2024, 2, 29)
print(calendar.show_info())