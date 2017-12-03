from src.basins import get_basins
from numpy import arange
from src.model import Model
from src.file_writer import write_to_files


def get_boundaries(points):
    points = list(sorted(points))
    boundaries = []
    last = points[0][1]
    for point, stable in points:
        if last != stable:
            boundaries.append(point)
            last = stable
    return boundaries


def main():
    xs = arange(0.0, 2.5, 0.01)
    ys = arange(0.0, 2.5, 0.01)

    offset = 1000

    alpha = 1.5
    mu = 0.7

    unstable, stable = get_basins(xs, ys, offset, Model(alpha, mu))
    all_points = list(map(lambda p: (p, False), unstable)) + list(map(lambda p: (p, True), stable))
    boundaries = get_boundaries(all_points)

    write_to_files('../files/boundaries_07', boundaries)


if __name__ == '__main__':
    main()
