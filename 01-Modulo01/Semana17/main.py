#from menu import option_menu
from finance_manager_class import FinanceManager
from persintence import load_categories, load_movements, save_categories, save_movements
from gui import run_gui

def main():
    finance_manager = FinanceManager()
    load_categories(finance_manager)
    load_movements(finance_manager)

    run_gui(finance_manager)

    save_categories(finance_manager)
    save_movements(finance_manager)

if __name__ == "__main__":
    main()
    