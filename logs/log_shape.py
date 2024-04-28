import inspect
from functools import wraps
from typing import Callable

import loguru
import pandas as pd


def format_log_message(
    func: Callable,
    prev_shape: tuple[int, int],
    new_shape: tuple[int, int],
    shape_change: tuple[str, str],
    df_name: str | None,
    module_name: str,
    max_length: int = 18,
) -> str:
    """
    Formats a log message to indicate changes in data frame shape after a function execution.

    Parameters:
        func (Callable): The function that modified the data frame.
        prev_shape (tuple[int, int]): The shape of the data frame before the function execution.
        new_shape (tuple[int, int]): The shape of the data frame after the function execution.
        shape_change (tuple[str, str]): The numerical change in shape, expressed as strings.
        df_name (str | None): The name of the data frame variable, if applicable.
        module_name (str): The name of the module where the function is defined.
        max_length (int, optional): The fixed width to which shape descriptions should be formatted. Defaults to 18.

    Returns:
        str: A formatted string containing all the information above.
    """
    formatted_prev_shape = f"{str(prev_shape):^{max_length}}"
    formatted_new_shape = f"{str(new_shape):^{max_length}}"
    formatted_change = f"{str(shape_change):^{max_length}}"

    return f"| {formatted_prev_shape} --> {formatted_new_shape} = {formatted_change} | {module_name}.{func.__name__}({df_name})"


def calculate_shape_change(
    old_shape: tuple[int, int], new_shape: tuple[int, int]
) -> tuple[str, str]:
    """
    Calculates the change in shape between two shapes of a pandas DataFrame.

    Parameters:
        old_shape (tuple[int, int]): The original shape of the DataFrame.
        new_shape (tuple[int, int]): The new shape of the DataFrame after some operation.

    Returns:
        tuple[str, str]: A tuple containing the changes in the number of rows and columns, formatted as strings.
    """
    x_change: int = new_shape[0] - old_shape[0]
    y_change: int = new_shape[1] - old_shape[1]
    x_change_str: str = f"{x_change:+}".replace("+0", "0")
    y_change_str: str = f"{y_change:+}".replace("+0", "0")

    return (x_change_str, y_change_str)


def log_shape_change(df_name: str | None, logger):
    """
    Decorator for logging changes in DataFrame shape before and after a function call that modifies the DataFrame.

    Parameters:
        df_name (str | None): The name of the DataFrame parameter if specified; otherwise, assumes DataFrame is the first argument.
        logger: The logger instance used to log the messages.

    Returns:
        function: A decorated function that logs the before and after shapes of the DataFrame.
    """

    def decorator(func):
        """."""

        @wraps(func)
        def wrapper_log_shape_change(*args, **kwargs):
            """."""
            if isinstance(df_name, str):
                df = kwargs.get(df_name)
            if df_name is None or df is None:
                df = args[0]
                if not isinstance(df, pd.DataFrame):
                    raise ValueError("Expected a DataFrame as the first argument")
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
    """
    Test function to demonstrate the functionality of the `log_shape_change` decorator.
    """
    logger = loguru.logger
    df = pd.DataFrame({"a": [0, 1, 2], "b": [3, 4, 5]})

    @log_shape_change(df_name="df", logger=logger)
    def t(df: pd.DataFrame) -> pd.DataFrame:
        """."""
        return df.iloc[:1]

    df = df.pipe(t)


if __name__ == "__main__":
    test_log_shape_change()
