import functools
import time


def backoff(start_sleep_time=0.1, factor=2, max_sleep_time=10, max_attempts=10,
            exceptions=(Exception,)):
    """
    Декоратор для повторной попытки выполнения функции с экспоненциальной задержкой.

    :param start_sleep_time: начальное время ожидания между попытками
    :param factor: множитель для увеличения времени ожидания
    :param max_sleep_time: максимальное время ожидания между попытками
    :param max_attempts: максимальное количество попыток
    :param exceptions: кортеж исключений, при возникновении которых будет произведена повторная попытка
    """

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            sleep_time = start_sleep_time

            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    attempts += 1
                    if attempts >= max_attempts:
                        raise
                    print(f"Exception occurred: {e}. "
                          f"Retrying in {sleep_time} seconds...")
                    time.sleep(sleep_time)
                    sleep_time = min(sleep_time * factor, max_sleep_time)

        return wrapper

    return decorator
