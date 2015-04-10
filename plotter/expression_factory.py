""" A factory to create new Expression objects. """

# 3rd party library
from numpy import shape, zeros

# Local library
from expression import Expression


class BaseExpressionFactory(object):

    def create(self, **kwargs):
        """ Create an Expression object from the given keyword arguments.
        """
        raise NotImplementedError


class FunctionExpressionFactory(BaseExpressionFactory):
    """ Factory to create an expression from a function between x and t.
    """

    def create(self, x_array, t_array, func):
        # Create an empty data array
        data = zeros((len(x_array), len(t_array)))

        # Populate the data array by evaluating the function at given input
        # points
        for i, x in enumerate(x_array):
            for j, t in enumerate(t_array):
                data[i][j] = func(x, t)

        return Expression(x_array, t_array, data)


class DataExpressionFactory(BaseExpressionFactory):
    """ Factory to create an expression from a 2D data array.
    """

    def create(self, x_array, t_array, data):
        if shape(data) != (len(x_array), len(t_array)):
            raise ValueError("Invalid data type")

        return Expression(x_array, t_array, data)