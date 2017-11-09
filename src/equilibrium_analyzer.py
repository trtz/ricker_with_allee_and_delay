from sympy.abc import x, y
from sympy import diff, Matrix, Abs
from src.model import Model
from src.helpers import substitute


def get_jacoby_matrix(alpha, mu):
    model = Model(alpha, mu)
    f, g = model.f_symbolic, model.g_symbolic
    df_dx = diff(f, x)
    df_dy = diff(f, y)
    dg_dx = diff(g, x)
    dg_dy = diff(g, y)
    return Matrix([[df_dx, df_dy], [dg_dx, dg_dy]])


def get_calculated_jacoby_matrix(alpha, mu, point):
    x_, y_ = point
    matrix = get_jacoby_matrix(alpha, mu)
    return substitute(matrix, x_, y_)


def get_jacoby_eigenvalues(alpha, mu, point):
    matrix = get_calculated_jacoby_matrix(alpha, mu, point)
    eigen_vals = matrix.eigenvals()
    if len(eigen_vals) != 2:
        raise NotImplementedError()
    return list(value.evalf() for value in eigen_vals.keys())


def root_is_stable(lambdas):
    l1, l2 = lambdas
    return Abs(l1) < 1 and Abs(l2) < 1
