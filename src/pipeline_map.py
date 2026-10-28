"""Применение нескольких функций к элементам списка через map."""

from typing import Any, Callable, Iterable, List


def apply_functions_with_map(
    items: Iterable[Any],
    functions: List[Callable[[Any], Any]],
) -> List[List[Any]]:
    """Для каждого элемента возвращает результат вызова всех переданных функций через map."""
    return list(
        map(lambda item: list(map(lambda fn: fn(item), functions)), items)
    )
