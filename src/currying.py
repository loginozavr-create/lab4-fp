"""Функция-карринг (Currying) для преобразования многоместных функций."""

import inspect
from functools import wraps
from typing import Any, Callable


def curry(func: Callable) -> Callable:
    """Преобразует функцию нескольких аргументов в каррированную форму."""
    sig = inspect.signature(func)
    total_args = len([
        p for p in sig.parameters.values()
        if p.kind in (inspect.Parameter.POSITIONAL_ONLY, inspect.Parameter.POSITIONAL_OR_KEYWORD)
    ])

    @wraps(func)
    def curried(*args: Any, **kwargs: Any) -> Any:
        if len(args) >= total_args:
            return func(*args, **kwargs)
        return lambda *more_args, **more_kwargs: curried(
            *(args + more_args), **{**kwargs, **more_kwargs}
        )

    return curried
