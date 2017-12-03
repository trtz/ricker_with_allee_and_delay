from src.file_writer import write_to_files
from src.model import Model


def main():
    alpha = 1.5
    mu = 0.8

    model = Model(alpha, mu)
    curr = (1.5, 1.5)
    values = [curr[0]]
    count = 100
    while curr[0] > 0 and count > 0:
        curr = model.next(curr)
        values.append(curr[0])
        count -= 1
    points = list(enumerate(values))
    write_to_files('../files/time_series', points)


if __name__ == '__main__':
    main()
