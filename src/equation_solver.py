from sympy.solvers import solve
from src.model import Model
from sympy.abc import x, y


def get_roots(model: Model):
    f, g = model.f_symbolic, model.g_symbolic
    roots = solve([f - x, g - y])
    return list((root[x], root[y]) for root in roots)
