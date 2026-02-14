from valid_functions import is_valid_year, is_valid_month, is_valid_day, print_user_age
from user_class import User
from datetime import date


def insert_user_data():
    year = is_valid_year()
    month = is_valid_month()
    day = is_valid_day(month, year)
    my_user = User(date(year, month, day))
    print_user_age(my_user)