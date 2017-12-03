from src.file_writer import write_to_files
from src.helpers import get_points
from src.model import Model


def main():
    offset = 1000
    count = 10

    start_point = (0.5, 0.5)

    alpha = 1.5
    mu = 1.04891
    epsilon = 0.0

    model = Model(alpha, mu)

    points = list(get_points(model, start_point, offset, count, epsilon))

    write_to_files('../files/main', points, True)
