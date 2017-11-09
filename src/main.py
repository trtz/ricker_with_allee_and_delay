from src.bifurcation import get_bif
from scipy import arange
from src.equilibrium_analyzer import get_jacoby_eigenvalues, root_is_stable
from src.file_writer import write_to_files
from src.helpers import get_rickers_trancendental_root
from src.model import Model


def bifurcation_main():
    alpha = 1.5

    start = 0.9
    end = 1.3
    step = 0.001
    count = 500
    offset = 1000
    start_point_fn = lambda mu: (1.1, 1.1)
    epsilon = 0.1
    transition_period = 5000

    bif = list(get_bif(alpha, start, end, step, count, offset, start_point_fn, epsilon, transition_period))
    write_to_files('../files/bif_noise', bif, True)


def phase_portrait_main():
    offset = 000
    count = 600

    start_point = (1.8, 1.8)

    alpha = 1.5
    mu = 1.15

    model = Model(alpha, mu)

    curr = start_point
    points = []
    for _ in range(offset):
        curr = model.next(curr)
    for _ in range(count):
        curr = model.next(curr)
        points.append(curr)
    write_to_files('../files/main', points, True)


def equilibrium_stability_main():
    alpha = 1.5
    start = 0.4 + 0.001
    end = 2
    step = 0.1
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


def main():
    bifurcation_main()


if __name__ == '__main__':
    main()
