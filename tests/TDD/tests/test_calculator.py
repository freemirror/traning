import os
import sys
import unittest

# Добавим возможность импорта из директории code в наш тест
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CODE_DIR_PATH = os.path.join(BASE_DIR, 'code')
sys.path.append(CODE_DIR_PATH)

from calculator import MadCalculator


class TestCalc(unittest.TestCase):
    """Тестируем Calculator."""

    @classmethod
    def setUpClass(cls):
        """Вызывается однажды перед запуском всех тестов класса."""
        # Arrange - подготавливаем данные для теста
        cls.calc = MadCalculator()

    def test_sum_string(self):
        act = TestCalc.calc.sum_string(1, 100500)
        self.assertEqual(act, 1100500, 'Метод sum_string работает неправильно.')

    def test_sum_string_first_negative_value(self):
        self.assertRaises(ValueError, TestCalc.calc.sum_string, -1, 100500)

    def test_sum_string_second_negative_value(self):
        with self.assertRaises(ValueError):
            TestCalc.calc.sum_string(1, -100500)

    def test_sum_args(self):
        act = TestCalc.calc.sum_args(3, -3, 5)
        self.assertEqual(act, 5, 'Метод sum_args работает неправильно.')


if __name__ == "__main__":
    unittest.main()