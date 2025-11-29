# using NumPy to perform basic arithmetic operations
"""Calculator utilities using NumPy.

Provides scalar/array-compatible wrappers for common math operations
and a small command-line interface for quick usage and demos.
"""

import numpy as np


def add(a, b):
    return np.add(a, b)


def subtract(a, b):
    return np.subtract(a, b)


def multiply(a, b):
    return np.multiply(a, b)


def divide(a, b):
    return np.divide(a, b)


def power(a, b):
    return np.power(a, b)


def sqrt(a):
    return np.sqrt(a)


def log(a):
    return np.log(a)


def exp(a):
    return np.exp(a)


def mean(a):
    return np.mean(a)


def median(a):
    return np.median(a)


def std_dev(a):
    return np.std(a)


def variance(a):
    return np.var(a)


def factorial(n):
    return np.math.factorial(n)


def gcd(a, b):
    return np.gcd(a, b)


def lcm(a, b):
    # handle scalar ints or numpy ints
    return abs(int(a) * int(b)) // int(np.gcd(a, b))


def sin(a):
    return np.sin(a)


def cos(a):
    return np.cos(a)


def tan(a):
    return np.tan(a)


def radians(deg):
    return np.radians(deg)


def degrees(rad):
    return np.degrees(rad)


def _parse_value(s):
    """Parse a string into a number or NumPy array.

    - Comma-separated values -> NumPy array of floats when possible.
    - Single numeric string -> int or float.
    - If input already numeric/array, returns numpy array or value.
    """
    if s is None:
        return None
    if isinstance(s, (int, float, np.ndarray, list, tuple)):
        return np.asarray(s)
    if isinstance(s, str):
        if "," in s:
            parts = [p.strip() for p in s.split(",") if p.strip()]
            try:
                return np.array([float(p) for p in parts])
            except ValueError:
                return np.array(parts)
        try:
            if "." in s:
                return float(s)
            return int(s)
        except ValueError:
            return s
    return s


def _format_out(x):
    try:
        if isinstance(x, np.ndarray):
            return x.tolist()
        # try converting to float if possible
        return float(x)
    except Exception:
        return x


def _demo():
    print("Calculator demo using NumPy — examples:")
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])
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

