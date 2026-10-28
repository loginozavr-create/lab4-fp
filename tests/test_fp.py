"""Модульные тесты для проверки функций функционального программирования."""

import time
import unittest
from src.filter_even import filter_even_numbers
from src.pipeline_map import apply_functions_with_map
from src.time_decorator import time_it
from src.custom_reduce import my_reduce
from src.currying import curry


class TestFunctionalProgramming(unittest.TestCase):
    # --- Средняя сложность: Задание 2 ---
    def test_filter_even_numbers(self):
        self.assertEqual(filter_even_numbers([1, 2, 3, 4, 5, 6]), [2, 4, 6])
        self.assertEqual(filter_even_numbers([1, 3, 5]), [])
        self.assertEqual(filter_even_numbers([-2, -1, 0, 1]), [-2, 0])

    # --- Средняя сложность: Задание 10 ---
    def test_apply_functions_with_map(self):
        funcs = [lambda x: x + 1, lambda x: x * 2, lambda x: x ** 2]
        # Для 3: f1(3)=4, f2(3)=6, f3(3)=9
        self.assertEqual(apply_functions_with_map([3], funcs), [[4, 6, 9]])
        self.assertEqual(
            apply_functions_with_map([1, 2], [lambda x: x * 10]),
            [[10], [20]]
        )

    # --- Средняя сложность: Задание 8 ---
    def test_time_it_decorator(self):
        execution_stats = {}

        @time_it(callback=lambda name, elapsed: execution_stats.update({"name": name, "elapsed": elapsed}))
        def slow_func(delay: float):
            time.sleep(delay)
            return "done"

        result = slow_func(0.05)
        self.assertEqual(result, "done")
        self.assertEqual(execution_stats["name"], "slow_func")
        self.assertGreaterEqual(execution_stats["elapsed"], 0.04)

    # --- Повышенная сложность: Задание 10 ---
    def test_my_reduce(self):
        # Сумма без initializer
        self.assertEqual(my_reduce(lambda acc, x: acc + x, [1, 2, 3, 4]), 10)
        # Произведение с initializer
        self.assertEqual(my_reduce(lambda acc, x: acc * x, [2, 3, 4], 10), 240)
        # Один элемент без initializer
        self.assertEqual(my_reduce(lambda acc, x: acc + x, [42]), 42)
        # Пустой список без initializer вызывает TypeError
        with self.assertRaises(TypeError):
            my_reduce(lambda acc, x: acc + x, [])

    # --- Повышенная сложность: Задание 3 ---
    def test_curry(self):
        def add_three(a, b, c):
            return a + b + c

        curried_add = curry(add_three)
        self.assertEqual(curried_add(1)(2)(3), 6)
        self.assertEqual(curried_add(1, 2)(3), 6)
        self.assertEqual(curried_add(1)(2, 3), 6)
        self.assertEqual(curried_add(1, 2, 3), 6)


if __name__ == "__main__":
    unittest.main()
