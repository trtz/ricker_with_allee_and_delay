from src.equation_solver import get_roots
from src.model import Model
from sympy.abc import x, y


EPSILON = 0.00001


def almost_equals(this, other):
    return this - EPSILON < other < this + EPSILON


def get_rickers_trancendental_root(alpha, mu):
    model = Model(alpha, mu)
    roots = get_roots(model)
    return list(filter(lambda x_: not (almost_equals(0, x_[0]) or almost_equals(1, x_[0])), roots))[0]


def substitute(expr, x_value, y_value):
    return expr.subs(x, x_value).subs(y, y_value)
