import re
from typing import Callable


def generator_numbers(text_with_numbers: str):
    only_numbers = r'\b\d+\.?\d*\b'
    for match in re.finditer(only_numbers, text_with_numbers):
        yield float(match.group())


def sum_profit(text_with_numbers: str, func: Callable) -> float:
    return sum(func(text_with_numbers))


text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
