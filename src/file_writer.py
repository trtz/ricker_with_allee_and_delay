
def write_to_file(filename, float_list, rewrite=True):
    if rewrite:
        open(filename, 'w').close()
    result_str = ''
    for value in float_list:
        result_str += str(value) + '\n'
    with open(filename, 'a') as file:
        file.write(result_str)


def write_to_files(files_prefix, float_collection, rewrite=True):
    float_collection = list(float_collection)
    x_file = files_prefix + '_x.txt'
    y_file = files_prefix + '_y.txt'
    xs = (point[0] for point in float_collection)
    ys = (point[1] for point in float_collection)
    write_to_file(x_file, xs, rewrite)
    write_to_file(y_file, ys, rewrite)
