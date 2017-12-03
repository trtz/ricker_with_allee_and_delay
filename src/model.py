from math import exp as math_exp
from sympy import exp as sympy_exp
from sympy.abc import x, y
from random import normalvariate


class Model:
    def __init__(self, alpha, mu):
        self.f = lambda x_, y_: x_ ** alpha * math_exp(mu * (1 - y_))
        self.g = lambda x_, y_: x_
        self.f_symbolic = x ** alpha * sympy_exp(mu * (1 - y))
        self.g_symbolic = x
        self.alpha = alpha
        self.mu = mu

    def next(self, point, epsilon=0):
        noise = epsilon * normalvariate(0, 1) * point[0]
        new_point = self.f(*point) + noise, self.g(*point)
        return (0, 0) if new_point[0] <= 0 or new_point[1] <= 0 else new_point
