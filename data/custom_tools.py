import functools
import warnings


def ignore_warning(warning):
    """
    Ignore a given warning occurring during method execution.

    Args:
        warning (Warning): warning type to ignore.

    Returns:
        the inner function

    """

    def inner(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            with warnings.catch_warnings():
                warnings.filterwarnings("ignore", category=warning)
                return func(*args, **kwargs)

        return wrapper

    return inner
