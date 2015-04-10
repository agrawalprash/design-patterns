""" A class representing a dependent expression """


# 3rd party library
from matplotlib.pylab import plot, show, xlabel, ylabel


class Expression(object):

    @classmethod
    def from_func(cls, x_array, t_array, func):
        # Create an empty data array
        data = zeros((len(x_array), len(t_array)))

        # Populate the data array by evaluating the function at given input
        # points
        for i, x in enumerate(x_array):
            for j, t in enumerate(t_array):
                data[i][j] = func(x, t)

        return cls(x_array, t_array, data)

    @classmethod
    def from_file(cls, x_array, t_array, path):
        with open(path) as f:
            raw_data = f.read()

        row_strings = raw_data.split('\n')
        rows = []
        for row_string in row_strings:
            row = [float(s) for s in row_string.split()]
            rows.append(row)

        data = array(rows)

        return cls(x_array, t_array, data)

    def __init__(self, x_array, t_array, data):
        self.x_array = x_array
        self.t_array = t_array
        self.data = data

    def plot(self, x=None, t=None):
        if x is None and t is None:
            raise RuntimeError("Invalid input")

        if t is not None:
            y_array = self.data[:, t]
            title = 'At t=%s' % t
            plot(self.x_array, y_array)
            xlabel('x_array')
            ylabel(title)
            show()

        if x is not None:
            y_array = self.data[x, :]
            title = 'At x=%s' % x
            plot(self.t_array, y_array)
            xlabel('t_array')
            ylabel(title)
            show()
