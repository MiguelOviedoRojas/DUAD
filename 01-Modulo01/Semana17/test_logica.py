import unittest
from datetime import date

from finance_manager_class import FinanceManager
from category_class import Category
from movement_class import Movement
from validations import (
    valid_input_as_a_string,
    valid_if_category_exist_in_category_list
)


class TestFinanceManager(unittest.TestCase):

    def setUp(self):
        """Se ejecuta antes de cada prueba"""
        self.fm = FinanceManager()

    # ---------- CATEGORY TESTS ----------

    def test_add_category_success(self):
        category = self.fm.add_category("HOME")
        self.assertIsNotNone(category)
        self.assertEqual(len(self.fm.category), 1)

    def test_add_category_duplicate(self):
        self.fm.add_category("HOME")
        result = self.fm.add_category("HOME")
        self.assertIsNone(result)
        self.assertEqual(len(self.fm.category), 1)

    def test_search_category_found(self):
        self.fm.add_category("FOOD")
        result = self.fm.search_category("food")
        self.assertIsNotNone(result)
        self.assertEqual(result.name, "FOOD")

    def test_search_category_not_found(self):
        result = self.fm.search_category("RENT")
        self.assertIsNone(result)

    # ---------- MOVEMENT TESTS ----------

    def test_add_expense_success(self):
        self.fm.add_category("HOME")
        movement = self.fm.add_movement(
            title="RENT",
            amount=500,
            category="HOME",
            movement_type="EXPENSE",
            date=date.today()
        )
        self.assertIsNotNone(movement)
        self.assertEqual(len(self.fm.movement), 1)

    def test_add_movement_invalid_category(self):
        movement = self.fm.add_movement(
            title="RENT",
            amount=500,
            category="HOME",
            movement_type="EXPENSE",
            date=date.today()
        )
        self.assertIsNone(movement)
        self.assertEqual(len(self.fm.movement), 0)

    # ---------- VALIDATION TESTS ----------

    def test_valid_input_as_string_valid(self):
        result = valid_input_as_a_string("TEST", "ABCDEF")
        self.assertTrue(result)

    def test_valid_input_as_string_invalid(self):
        result = valid_input_as_a_string("TEST", "ABC123")
        self.assertFalse(result)

    def test_category_existence_validation(self):
        categories = [Category("HOME")]
        result = valid_if_category_exist_in_category_list("HOME", categories)
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()