import math
from math import sqrt


def calc(a: int, b: int, operator: str) -> int | float:
    match operator:
        case '*':
            return a * b + sqrt(a)
        case '+':
            res = math.cos(a)
            return a + b + res
        case '-':
            return a - b
