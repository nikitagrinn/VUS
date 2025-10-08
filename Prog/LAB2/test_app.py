# test_app.py

import unittest
import os
from main import calculate, load_params

class TestCalculatorFunctions(unittest.TestCase):

    # --- Тесты для calculate ---

    def test_simple_division(self):
        """Тест простого деления 1/2."""
        self.assertAlmostEqual(calculate(1, 2, epsilon=0.01), 0.5)

    def test_division_by_zero(self):
        """Тест деления на ноль."""
        with self.assertRaises(ZeroDivisionError):
            calculate(10, 0)

    def test_epsilon_out_of_range(self):
        """Тест на epsilon вне диапазона."""
        with self.assertRaises(ValueError):
            calculate(1, 2, epsilon=0.5)

    # --- Тесты для load_params ---

    def setUp(self):
        """Создает временный файл конфигурации."""
        self.test_config_file = 'test_settings.ini'

    def tearDown(self):
        """Удаляет временный файл конфигурации."""
        if os.path.exists(self.test_config_file):
            os.remove(self.test_config_file)

    def test_load_params_success(self):
        """Тест успешного чтения из файла."""
        with open(self.test_config_file, 'w') as f:
            f.write('[Settings]\nepsilon = 0.005\n')
        self.assertEqual(load_params(self.test_config_file), 0.005)

    def test_load_params_file_not_found(self):
        """Тест на отсутствующий файл."""
        with self.assertRaises(FileNotFoundError):
            load_params('non_existent_file.ini')

    def test_bad_number_format_in_config(self):
        """Тест на неверный формат числа в файле."""
        with open(self.test_config_file, 'w') as f:
            f.write('[Settings]\nepsilon = text\n')
        with self.assertRaises(ValueError):
            load_params(self.test_config_file)

if __name__ == '__main__':
    unittest.main()
