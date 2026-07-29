from datetime import date


def valid_age_user(func):
    def wrapper(user):
        age = user.age
        if age >= 18:
            return func(user)
        else:
            raise ValueError("User must be at least 18 years old")
    return wrapper


@valid_age_user
def print_user_age(user):
    print(f"User is {user.age} years old")


def is_valid_year():
    today = date.today()
    while True:
        try:
            user_year = int(input("Insert Year: "))
            if user_year <= 0 or user_year > today.year:
                print("Please Insert a Valid Year")
            else:
                return user_year
        except ValueError as ex:
            print(f"Please Insert a Valid Year: {ex}")


def is_valid_month():
    while True:
        try:
            user_month = int(input("Insert Month: "))
            if user_month < 1 or user_month > 12:
                print("Please Insert a Valid Month")
            else:
                return user_month
        except ValueError as ex:
            print(f"Please Insert a Valid Month: {ex}")


def is_valid_day(month, year):
    while True:
        try:
            user_day = int(input("Insert Day: "))
            if month == 2:
                if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                    if user_day < 1 or user_day > 29:
                        print("Please Insert a Valid Day")
                    else:
                        return user_day
                elif user_day < 1 or user_day > 28:
                    print("Please Insert a Valid Day")
                else:
                    return user_day
            elif month in (4, 6, 9, 11):
                if user_day < 1 or user_day > 30:
                    print("Please Insert a Valid Day")
                else:
                    return user_day
            elif user_day < 1 or user_day > 31:
                print("Please Insert a Valid Day")
            else:
                return user_day
        except ValueError as ex:
            print(f"Please Insert a Valid Day: {ex}")
