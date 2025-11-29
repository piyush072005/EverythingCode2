#using NumPy to perform basic arithmetic operations
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
    return abs(a * b) // np.gcd(a, b)
def sin(a):
    return np.sin(a)
def cos(a):
    return np.cos(a)
def tan(a):
    return np.tan(a)
def radians(degrees):
    return np.radians(degrees)
def degrees(radians):
    return np.degrees(radians)

