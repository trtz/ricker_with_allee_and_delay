from src.equilibrium_analyzer import get_jacoby_eigenvalues, root_is_stable
from src.file_writer import write_to_files
from src.helpers import get_rickers_trancendental_root
from numpy import arange


def equilibrium_stability_main():
    alpha = 1.5
    start = 0.4 + 0.001
    end = 2
    step = 0.2
    mu_range = arange(start, end, step)
    for mu in mu_range:
        root = get_rickers_trancendental_root(alpha, mu)
        values = get_jacoby_eigenvalues(alpha, mu, root)
        print(mu, root_is_stable(values))


def transcendental_equilibrium_main():
    alpha = 1.5
    start = 0.9
    end = 1.3
    step = 0.001
    mu_range = arange(start, end, step)
    if 0.5 in mu_range:
        mu_range.__delitem__(0.5)
    points = []
    for mu in mu_range:
        root = get_rickers_trancendental_root(alpha, mu)
        points.append((mu, root[0]))
    write_to_files('../files/m2', points, True)
