from scipy import arange
from src.model import Model


def get_bif(alpha, start, end, step, count, offset, start_point_fn, epsilon, transition_period):
    parameters = arange(start, end, step)

    for parameter in parameters:
        start_point = start_point_fn(parameter)
        curr_point = start_point
        model = Model(alpha, parameter)
        for _ in range(offset):
            curr_point = model.next(curr_point)
        for _ in range(transition_period):
            curr_point = model.next(curr_point, epsilon)
            if type(curr_point[0]) == complex or curr_point[0] <= 0:
                break
        for _ in range(count):
            curr_point = model.next(curr_point, epsilon)
            if type(curr_point[0]) == complex or curr_point[0] <= 0:
                break
            yield parameter, curr_point[0]
