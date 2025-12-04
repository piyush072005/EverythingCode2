# Light-weight calculator utilities without NumPy dependency.
"""Calculator utilities using the Python standard library.

This module intentionally avoids NumPy so simple scripts and the
Tkinter GUI can run in minimal environments.
"""

from math import factorial as _fact, sin as _sin, cos as _cos, tan as _tan, radians as _radians, degrees as _degrees
from statistics import mean as _mean, median as _median, pstdev as _pstdev, pvariance as _pvariance


def _is_sequence(x):
    return isinstance(x, (list, tuple))


def _apply_elementwise(a, b, op):
    # broadcast scalar to sequence if necessary
    if _is_sequence(a) and _is_sequence(b):
        return [op(x, y) for x, y in zip(a, b)]
    if _is_sequence(a):
        return [op(x, b) for x in a]
    if _is_sequence(b):
        return [op(a, y) for y in b]
    return op(a, b)


def add(a, b):
    return _apply_elementwise(a, b, lambda x, y: x + y)


def subtract(a, b):
    return _apply_elementwise(a, b, lambda x, y: x - y)


def multiply(a, b):
    return _apply_elementwise(a, b, lambda x, y: x * y)


def divide(a, b):
    return _apply_elementwise(a, b, lambda x, y: x / y)


def power(a, b):
    return _apply_elementwise(a, b, lambda x, y: x ** y)


def sqrt(a):
    return _apply_elementwise(a, None, lambda x, _: x ** 0.5)


def log(a):
    import math
    return _apply_elementwise(a, None, lambda x, _: math.log(x))


def exp(a):
    import math
    return _apply_elementwise(a, None, lambda x, _: math.exp(x))


def mean(a):
    if _is_sequence(a):
        return _mean(a)
    return a


def median(a):
    if _is_sequence(a):
        return _median(a)
    return a


def std_dev(a):
    if _is_sequence(a):
        return _pstdev(a)
    return 0


def variance(a):
    if _is_sequence(a):
        return _pvariance(a)
    return 0


def factorial(n):
    return _fact(int(n))


def gcd(a, b):
    import math
    return math.gcd(int(a), int(b))


def lcm(a, b):
    a_i = int(a)
    b_i = int(b)
    import math
    return abs(a_i * b_i) // math.gcd(a_i, b_i)


def sin(a):
    return _apply_elementwise(a, None, lambda x, _: _sin(x))


def cos(a):
    return _apply_elementwise(a, None, lambda x, _: _cos(x))


def tan(a):
    return _apply_elementwise(a, None, lambda x, _: _tan(x))


def radians(deg):
    return _apply_elementwise(deg, None, lambda x, _: _radians(x))


def degrees(rad):
    return _apply_elementwise(rad, None, lambda x, _: _degrees(x))


def _parse_value(s):
    if s is None:
        return None
    if _is_sequence(s):
        return list(s)
    if isinstance(s, str):
        if "," in s:
            parts = [p.strip() for p in s.split(",") if p.strip()]
            try:
                return [float(p) for p in parts]
            except ValueError:
                return parts
        try:
            if "." in s:
                return float(s)
            return int(s)
        except ValueError:
            return s
    return s


def _format_out(x):
    try:
        if _is_sequence(x):
            return list(x)
        return float(x)
    except Exception:
        return x


def _demo():
    print("Calculator demo — examples:")
    a = [1, 2, 3]
    b = [4, 5, 6]
    print("a:", a)
    print("b:", b)
    print("add(a,b):", add(a, b))
    print("subtract(a,b):", subtract(a, b))
    print("multiply(a,b):", multiply(a, b))
    print("divide(b,a):", divide(b, a))
    print("power(a,2):", power(a, 2))
    print("mean(a):", mean(a))
    print("std_dev(a):", std_dev(a))


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="NumPy-backed calculator (scalars and comma-separated arrays)")
    parser.add_argument("--op", help="operation: add, sub, mul, div, pow, sqrt, log, exp, mean, median, std, var, factorial, gcd, lcm, sin, cos, tan")
    parser.add_argument("--a", help="first operand (number or comma-separated list)")
    parser.add_argument("--b", help="second operand (number or comma-separated list) - optional for unary ops")
    args = parser.parse_args()

    if not args.op:
        _demo()
    else:
        a = _parse_value(args.a)
        b = _parse_value(args.b) if args.b is not None else None
        op = args.op.lower()
        try:
            if op in ("add", "+"):
                res = add(a, b)
            elif op in ("sub", "subtract", "-"):
                res = subtract(a, b)
            elif op in ("mul", "multiply", "*"):
                res = multiply(a, b)
            elif op in ("div", "divide", "/"):
                res = divide(a, b)
            elif op in ("pow", "power"):
                res = power(a, b)
            elif op == "sqrt":
                res = sqrt(a)
            elif op == "log":
                res = log(a)
            elif op == "exp":
                res = exp(a)
            elif op in ("mean",):
                res = mean(a)
            elif op in ("median",):
                res = median(a)
            elif op in ("std", "std_dev"):
                res = std_dev(a)
            elif op in ("var", "variance"):
                res = variance(a)
            elif op == "factorial":
                res = factorial(int(a))
            elif op == "gcd":
                res = gcd(int(a), int(b))
            elif op == "lcm":
                res = lcm(int(a), int(b))
            elif op == "sin":
                res = sin(a)
            elif op == "cos":
                res = cos(a)
            elif op == "tan":
                res = tan(a)
            else:
                raise ValueError(f"Unsupported operation: {op}")
        except Exception as e:
            print("Error performing operation:", e)
        else:
            print("Result:", _format_out(res))

