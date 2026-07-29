from validations import valid_if_category_exist_in_category_list
from category_class import Category
from movement_class import Movement

class FinanceManager:
    def __init__(self):
        self.movement = [] #Stores all movements (expenses and incomes)
        self.category = [] #Stores all categories


    def add_category(self, user_category):
        if valid_if_category_exist_in_category_list(user_category, self.category):
            new_category = Category(user_category)
            self.category.append(new_category)
            return new_category
        return None
        
    def search_category(self, user_category):
        for index in range(len(self.category)):
            if self.category[index].name.upper() == user_category.upper():
                return self.category[index]
        return None


    def add_movement(self, title, amount, category, movement_type, date):
        category_obj = self.search_category(category)
        if category_obj is None:
            return None
        else:
            movement = Movement(
                title,
                amount,
                category_obj,
                movement_type,
                date)
            self.movement.append(movement)
            return movement







