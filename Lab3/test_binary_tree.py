# -*- coding: utf-8 -*-

"""
Тесты для функции генерации бинарного дерева.
"""

import unittest
# Предполагается, что ваша функция находится в файле binary_tree.py
from binary_tree import gen_bin_tree

class TestGenBinTree(unittest.TestCase):
    """Набор тестов для проверки функции gen_bin_tree."""

    def test_height_0(self):
        """Тестирование генерации дерева высотой 0."""
        self.assertEqual(gen_bin_tree(height=0, root=7), {'7': []})

    def test_height_1(self):
        """Тестирование генерации дерева высотой 1."""
        expected = {
            '7': [
                {'21': []},
                {'3': []}
            ]
        }
        self.assertEqual(gen_bin_tree(height=1, root=7), expected)

    def test_height_2(self):
        """Тестирование генерации дерева высотой 2."""
        expected = {
            '7': [
                {'21': [{'63': []}, {'17': []}]},
                {'3': [{'9': []}, {'-1': []}]}
            ]
        }
        self.assertEqual(gen_bin_tree(height=2, root=7), expected)
    
    def test_negative_height(self):
        """Тестирование с отрицательной высотой."""
        self.assertIsNone(gen_bin_tree(height=-1, root=7))


if __name__ == '__main__':
    # Эта строка позволяет запускать тесты в средах,
    # где стандартный запуск не работает (например, Google Colab).
    unittest.main(argv=[''], verbosity=2, exit=False)
