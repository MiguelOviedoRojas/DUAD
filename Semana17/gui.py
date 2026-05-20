import FreeSimpleGUI as sg
from datetime import date
from persintence import save_categories, save_movements
from validations import validate_required_fields, validate_amount


def save_all(finance_manager):
    save_categories(finance_manager)
    save_movements(finance_manager)


def run_gui(finance_manager):
    sg.theme("LightBlue")
    layout = [
        [sg.Text("Personal Finance Manager", font=("Arial", 16))],
        [sg.Button("Add Category")],
        [sg.Button("Add Expense")],
        [sg.Button("Add Income")],
        [sg.Button("Show Movements")],
        [sg.Button("Exit")]
    ]
    window = sg.Window("Finance Manager", layout)
    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == "Exit":
            break
        if event == "Add Category":
            add_category_window(finance_manager)
        elif event == "Add Expense":
            add_expense_window(finance_manager)
        elif event == "Add Income":
            add_income_window(finance_manager)
        elif event == "Show Movements":
            show_movements_table(finance_manager)
    window.close()


def add_category_window(finance_manager):
    sg.theme("LightBlue")
    layout = [
        [sg.Text("Add New Category")],
        [sg.Text("Category name:"), sg.Input(key="-CATEGORY-")],
        [sg.Button("Save"), sg.Button("Cancel")]
    ]
    window = sg.Window("Add Category", layout, modal=True)
    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == "Cancel":
            break
        if event == "Save":
            category_name = values["-CATEGORY-"].strip().upper()
            if not category_name:
                sg.popup("Category name cannot be empty")
                continue
            result = finance_manager.add_category(category_name)
            if result is None:
                sg.popup("Category already exists")
            else:
                sg.popup("Category added successfully")
                save_all(finance_manager)
                break
    window.close()


def add_expense_window(finance_manager):
    categories = [cat.name for cat in finance_manager.category]
    if not categories:
        sg.popup("No categories available. Please add a category first.")
        return
    layout = [
        [sg.Text("Add Expense", font=("Arial", 14))],
        [sg.Text("Title:"), sg.Input(key="-TITLE-")],
        [sg.Text("Amount:"), sg.Input(key="-AMOUNT-")],
        [sg.Text("Category:"), sg.Combo(categories, key="-CATEGORY-", readonly=True)],
        [sg.Button("Save"), sg.Button("Cancel")]
    ]
    window = sg.Window("Add Expense", layout, modal=True)
    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == "Cancel":
            break
        if event == "Save":
            title = values["-TITLE-"].strip().upper()
            amount_str = values["-AMOUNT-"].strip()
            category = values["-CATEGORY-"]
            
            if not validate_required_fields(title, amount_str, category):
                sg.popup("All fields are required")
                continue
            amount = validate_amount(amount_str)
            if amount is None:
                sg.popup("Amount mut be a valid number greater than 0")
                continue

            today = date.today()
            movement = finance_manager.add_movement(
                title, amount, category, "EXPENSE", today
            )
            if movement is None:
                sg.popup("Error adding expense")
            else:
                sg.popup("Expense added successfully")
                save_all(finance_manager)
                break
    window.close()


def add_income_window(finance_manager):
    categories = [cat.name for cat in finance_manager.category]
    if not categories:
        sg.popup("No categories available. Please add a category first.")
        return
    layout = [
        [sg.Text("Add Income", font=("Arial", 14))],
        [sg.Text("Title:"), sg.Input(key="-TITLE-")],
        [sg.Text("Amount:"), sg.Input(key="-AMOUNT-")],
        [sg.Text("Category:"), sg.Combo(categories, key="-CATEGORY-", readonly=True)],
        [sg.Button("Save"), sg.Button("Cancel")]
    ]
    window = sg.Window("Add Income", layout, modal=True)
    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == "Cancel":
            break
        if event == "Save":
            title = values["-TITLE-"].strip().upper()
            amount_str = values["-AMOUNT-"].strip()
            category = values["-CATEGORY-"]
            
            if not validate_required_fields(title, amount_str, category):
                sg.popup("All fields are required")
                continue

            amount = validate_amount(amount_str)

            if amount is None:
                sg.popup("Invalid amount")
                continue

            today = date.today()
            movement = finance_manager.add_movement(
                title, amount, category, "INCOME", today
            )
            if movement is None:
                sg.popup("Error adding income")
            else:
                sg.popup("Income added successfully")
                save_all(finance_manager)
                break
    window.close()


def show_movements_table(finance_manager):
    if not finance_manager.movement:
        sg.popup("No movements recorded yet.")
        return
    headings = ["Title", "Amount", "Category", "Type", "Date"]
    data = []
    for movement in finance_manager.movement:
        data.append([
            movement.title,
            movement.amount,
            movement.category.name,
            movement.type,
            movement.date.strftime("%Y-%m-%d")
        ])
    layout = [
        [sg.Text("Movements", font=("Arial", 14))],
        [
            sg.Table(
                values=data,
                headings=headings,
                auto_size_columns=True,
                justification="center",
                num_rows=min(len(data), 10),
                enable_events=False
            )
        ],
        [sg.Button("Close")]
    ]
    window = sg.Window("Movements Table", layout, modal=True)
    while True:
        event, _ = window.read()
        if event in (sg.WINDOW_CLOSED, "Close"):
            break
    window.close()
