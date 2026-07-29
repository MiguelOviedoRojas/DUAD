class Movement:
    def __init__(self, title, amount, category, type_movement, date):
        self.title = title
        self.amount = amount
        self.category = category
        self.type = type_movement
        self.date = date
    
    def __str__(self):
        return f"{self.title} - {self.amount} - {self.category.name} - {self.type} - {self.date}"