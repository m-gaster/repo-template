import inspect
from functools import wraps
from typing import Callable

import loguru
import pandas as pd
from icecream import ic


def format_log_message(
    func: Callable,
    prev_shape: tuple[int, int],
    new_shape: tuple[int, int],
    shape_change: tuple[str, str],
    df_name: str | None,
    module_name: str,
    max_length: int = 18,
):
    formatted_prev_shape = f"{str(prev_shape):^{max_length}}"
    formatted_new_shape = f"{str(new_shape):^{max_length}}"
    formatted_change = f"{str(shape_change):^{max_length}}"

    return f"| {formatted_prev_shape} --> {formatted_new_shape} = {formatted_change} | {module_name}.{func.__name__}({df_name})"


def calculate_shape_change(
    old_shape: tuple[int, int], new_shape: tuple[int, int]
) -> tuple[str, str]:
    x_change: int = new_shape[0] - old_shape[0]
    y_change: int = new_shape[1] - old_shape[1]
    x_change_str: str = f"{x_change:+}".replace("+0", "0")
    y_change_str: str = f"{y_change:+}".replace("+0", "0")

    return (x_change_str, y_change_str)


def log_shape_change(df_name: str | None, logger):
    """
    df_name: str | None.
        if None:
            take first arg
        else (or failure on first step):
            take kwarg of `df_name`

    NOTE: piping with pandas means that the df is the first arg, but kwargs aren't passed through
    """

    def decorator(func):
        @wraps(func)
        def wrapper_log_shape_change(*args, **kwargs):
            if isinstance(df_name, str):
                # try to take
                df = kwargs.get(df_name)
            if df_name is None or df is None:
                # take first arg
                df = args[0]
                if not isinstance(df, pd.DataFrame):
                    raise ValueError()
            else:
                raise ValueError(
                    "Unexpected behaviour (possibly a variable of the wrong type)."
                )
            prev_shape = df.shape
            result = func(*args, **kwargs)
            new_shape = result.shape
            shape_change = calculate_shape_change(
                old_shape=prev_shape, new_shape=new_shape
            )
            log_msg = format_log_message(
                func=func,
                prev_shape=prev_shape,
                new_shape=new_shape,
                shape_change=shape_change,
                df_name=df_name,
                module_name=inspect.getmodule(func).__name__,
            )
            logger.info(log_msg)
            return result

        return wrapper_log_shape_change

    return decorator


def test_log_shape_change():
    logger = loguru.logger
    df = pd.DataFrame({"a": [0, 1, 2], "b": [3, 4, 5]})

    @log_shape_change(df_name="df", logger=logger)
    def t(df: pd.DataFrame) -> pd.DataFrame:
        return df.iloc[:1]

    df = df.pipe(t)


if __name__ == "__main__":
    test_log_shape_change()
