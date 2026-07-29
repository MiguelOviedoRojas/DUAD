import csv
from category_class import Category
from datetime import date
from movement_class import Movement


def save_categories(finance_manager):
    file_path = 'categories.csv'
    with open(file_path, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["name"])
        for category in finance_manager.category:
            writer.writerow([category.name])


def load_categories(finance_manager):
    file_path = 'categories.csv'
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader)

            for row in reader:
                category_name = row[0]
                category = Category(category_name)
                finance_manager.category.append(category)
    except FileNotFoundError:
        pass


def load_movements(finance_manager):
    file_path = 'movements.csv'
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                title = row[0]
                amount = float(row[1])
                category_name = row[2]
                movement_type = row[3]
                movement_date = date.fromisoformat(row[4])

                category_obj = finance_manager.search_category(category_name)
                if category_obj is None:
                    continue

                movement = Movement(
                    title,
                    amount,
                    category_obj,
                    movement_type,
                    movement_date
                )

                finance_manager.movement.append(movement)
    except FileNotFoundError:
        pass


def save_movements(finance_manager):
    file_path = 'movements.csv'
    with open(file_path, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["title", "amount", "category", "type", "date"])
        for movement in finance_manager.movement:
            writer.writerow([
                movement.title,
                movement.amount,
                movement.category.name,
                movement.type,
                movement.date.isoformat()
            ])
