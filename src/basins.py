from src.file_writer import write_to_files
from src.model import Model
from src.helpers import almost_zero
from scipy import arange


def get_basins(xs, ys, offset, model):
    stable = []
    unstable = []
    for x in xs:
        for y in ys:
            found = False
            start = (x, y)
            curr = (x, y)
            if almost_zero(curr):
                unstable.append(start)
                continue
            for i in range(offset):
                curr = model.next(curr)
                if almost_zero(curr):
                    unstable.append(start)
                    found = True
                    break
            if not found:
                stable.append(start)
    return unstable, stable


def main():
    alpha = 1.5
    mu = 1.04891
    model = Model(alpha, mu)
    xs = arange(0.0, 2.5, 0.001)
    ys = arange(0.0, 2.5, 0.001)

    offset = 2000

    unstable, stable = get_basins(xs, ys, offset, model)

    write_to_files('../files/stable', stable, True)
    write_to_files('../files/unstable', unstable, True)
