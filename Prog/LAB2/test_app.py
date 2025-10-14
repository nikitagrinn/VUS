import unittest
import os
from main import calculate, load_params

class TestCalculatorFunctions(unittest.TestCase):

    # --- Тесты для calculate ---

    def test_another_division(self):
        """Тест деления 1/1000."""
        self.assertAlmostEqual(calculate(1, 1000, epsilon=0.0001), 0.001)

    def test_division_by_zero(self):
        """Тест деления на ноль."""
        with self.assertRaises(ZeroDivisionError):
            calculate(10, 0)

    def test_epsilon_out_of_range(self):
        """Тест на epsilon вне диапазона."""
        with self.assertRaises(ValueError):
            calculate(1, 2, epsilon=0.5) # Слишком большое значение
        with self.assertRaises(ValueError):
            calculate(1, 2, 1e-10) # Слишком маленькое значение

    # --- Тесты для load_params ---

    def setUp(self):
        """Создает временный файл конфигурации перед каждым тестом."""
        self.test_config_file = 'test_settings.ini'

    def tearDown(self):
        """Удаляет временный файл конфигурации после каждого теста."""
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
            
    def test_missing_section_or_key_in_config(self):
        """Тест на отсутствие секции или ключа в файле."""
        with open(self.test_config_file, 'w') as f:
            f.write('[WrongSection]\nepsilon = 0.01\n')
        with self.assertRaises(KeyError):
            load_params(self.test_config_file)

if __name__ == '__main__':
    # Запуск тестов
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
