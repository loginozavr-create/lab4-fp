"""Фильтрация чётных чисел с использованием функционального стиля."""

from typing import Iterable, List


def filter_even_numbers(numbers: Iterable[int]) -> List[int]:
    """Возвращает список только чётных чисел с помощью filter."""
    return list(filter(lambda x: x % 2 == 0, numbers))
