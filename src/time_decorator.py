"""Декоратор для замера времени выполнения функции."""

import functools
import time
from typing import Any, Callable, Optional


def time_it(callback: Optional[Callable[[str, float], None]] = None) -> Callable:
    """Декоратор, измеряющий время работы функции."""
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            start_time = time.perf_counter()
            result = func(*args, **kwargs)
            elapsed = time.perf_counter() - start_time
            if callback:
                callback(func.__name__, elapsed)
            else:
                print(f"Функция {func.__name__} выполнена за {elapsed:.6f} сек.")
            return result
        return wrapper
    return decorator
