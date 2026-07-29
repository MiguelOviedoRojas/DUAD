class BankAccount:
    def __init__(self):
        self.balance = 0.0

    def insert_money(self, money):
        self.balance = self.balance + money
        return self.balance
        
    def subtract_money(self, subtract_money):
        self.balance = self.balance - subtract_money
        self.print_balance()
    
    def print_balance(self):
        print(f"Balance of your Account is: {self.balance}")
    

class SavingsAccount(BankAccount):
    def __init__(self):
        super().__init__()
        self.min_balance = 1000
    
    def compare_balance(self,money):
        difference = self.balance - money
        try:
            if difference < self.min_balance:
                raise(f"Error, Balance {difference} is minor than Min_Balance {self.min_balance}")
            else:
                self.subtract_money(money)
        except BaseException as ex:
            print(f"Error Balance is Minor than Min_Balance: {ex}")
            return ex

