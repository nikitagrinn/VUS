# -*- coding: utf-8 -*-

"""
Этот модуль предоставляет функциональность для генерации и отображения
бинарного дерева заданной высоты и с заданным значением в корне.
"""

from typing import Dict, List, Any, Optional

def gen_bin_tree(height: int, root: int) -> Optional[Dict[str, List[Any]]]:
    """
    Рекурсивно генерирует бинарное дерево в виде вложенных словарей.

    Args:
        height (int): Высота дерева. Дерево с высотой 0 имеет только корень.
        root (int): Значение в корневом узле.

    Returns:
        Optional[Dict[str, List[Any]]]: Словарь, представляющий бинарное
        дерево, или None, если высота отрицательна.
    """
    # Базовый случай рекурсии: если высота стала отрицательной,
    # это означает, что мы вышли за пределы листьев дерева.
    if height < 0:
        return None

    # Формулы для вычисления потомков согласно варианту:
    # Root = 7; height = 4, left_leaf = root*3, right_leaf = root-4
    left_child_val = root * 3
    right_child_val = root - 4

    # Рекурсивный вызов для построения левого и правого поддеревьев
    left_subtree = gen_bin_tree(height - 1, left_child_val)
    right_subtree = gen_bin_tree(height - 1, right_child_val)

    # Формирование списка дочерних узлов.
    # Если поддерево не None, оно добавляется в список.
    children = []
    if left_subtree:
        children.append(left_subtree)
    if right_subtree:
        children.append(right_subtree)
        
    # Если высота равна 0, у узла не должно быть видимых потомков
    if height == 0:
        return {str(root): []}

    return {str(root): children}


# Пример использования с вашими параметрами:
if __name__ == '__main__':
    # Параметры для генерации дерева
    ROOT_NODE = 7
    TREE_HEIGHT = 4

    # Генерация и вывод дерева
    generated_tree = gen_bin_tree(height=TREE_HEIGHT, root=ROOT_NODE)

    # Для красивого вывода можно использовать модуль pprint
    import pprint
    pp = pprint.PrettyPrinter(indent=4)
    print(f"Сгенерированное дерево с высотой {TREE_HEIGHT} и корнем {ROOT_NODE}:")
    pp.pprint(generated_tree)
