from src.equation_solver import get_roots
from src.model import Model
from sympy.abc import x, y
from math import sqrt


EPSILON = 0.00001


def get_dist(value1, value2):
    x1, y1 = value1
    x2, y2 = value2
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def almost_zero(point, delta=0.01):
    return is_close(point, (0, 0), delta)


def is_close(point1, point2, delta=0.01):
    return almost_equals(get_dist(point1, point2), 0.0, delta)


def almost_equals(value1, value2, epsilon=EPSILON):
    if type(value1) != type(value2):
        raise ValueError('Type1 must be type2')
    if type(value1) == tuple:
        return almost_equals(get_dist(value1, value2), 0.0, epsilon)
    return value1 - epsilon < value2 < value1 + epsilon


def get_rickers_trancendental_root(alpha, mu):
    model = Model(alpha, mu)
    roots = get_roots(model)
    return list(filter(lambda x_: not (almost_equals(0, x_[0]) or almost_equals(1, x_[0])), roots))[0]


def substitute(expr, x_value, y_value):
    return expr.subs(x, x_value).subs(y, y_value)


def get_points(model, start_point, offset, count, epsilon=0):
    curr = start_point
    for _ in range(offset):
        curr = model.next(curr, epsilon)
    if count > 0 and offset == 0:
        yield start_point
    for _ in range(count):
        curr = model.next(curr, epsilon)
        yield curr
