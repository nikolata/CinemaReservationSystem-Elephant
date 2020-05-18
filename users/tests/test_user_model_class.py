import unittest
from users.models import UserModel


class TestUserModel(unittest.TestCase):
    def test_validate_with_sort_password_returns_false(self):
        password = '123456'
        name = 'pop'

        self.assertFalse(UserModel.validate(name, password))

    def test_validate_without_capital_letter_returns_false(self):
        password = 'asdfghjk'
        name = 'pop'

        self.assertFalse(UserModel.validate(name, password))

    def test_validate_without_special_symbol_returns_false(self):
        password = 'asdfghjk'
        name = 'pop'

        self.assertFalse(UserModel.validate(name, password))

    def test_validate_with_correct_password(self):
        password = 'asdfghjkL!'
        name = 'pop'

        self.assertTrue(UserModel.validate(name, password))


if __name__ == '__main__':
    unittest.main()
