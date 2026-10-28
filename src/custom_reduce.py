"""Собственная реализация функции reduce."""

from typing import Any, Callable, Iterable


_MISSING = object()


def my_reduce(function: Callable[[Any, Any], Any], iterable: Iterable[Any], initializer: Any = _MISSING) -> Any:
    """Аналог functools.reduce: последовательно сворачивает iterable функцией function."""
    it = iter(iterable)

    if initializer is _MISSING:
        try:
            accumulator = next(it)
        except StopIteration:
            raise TypeError("my_reduce() of empty iterable with no initial value") from None
    else:
        accumulator = initializer

    for element in it:
        accumulator = function(accumulator, element)

    return accumulator
