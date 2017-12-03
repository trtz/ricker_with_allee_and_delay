import matplotlib.pyplot as plt


def plot(point_list):
    xs = [point[0] for point in point_list]
    ys = [point[1] for point in point_list]
    plt.scatter(xs, ys, c='k', s=0.01)
    plt.show()
