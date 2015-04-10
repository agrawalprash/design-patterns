""" Main entry point. """

# Standard library
import math

# 3rd party library
from numpy import array, linspace, zeros

# Local library
from expression_factory import FunctionExpressionFactory, DataExpressionFactory

def main():
    x_array = linspace(0, 2*math.pi, 100)
    t_array = array([0, 1, 2, 3])
    data = zeros((len(x_array), len(t_array)))

    def func(x, t):
        return math.sin(x*t)

    # expression_factory = FunctionExpressionFactory()
    # y = expression_factory.create(x_array=x_array, t_array=t_array, func=func)
    #
    # # expression_factory = DataExpressionFactory()
    # # y = expression_factory.create(x_array=x_array, t_array=t_array, data=data)
    #
    # y = Expression(x_array, t_array, data)
    # y.plot()

    from expression import Expression

    y = Expression(x_array=x_array, t_array=t_array, data=data)

    y = Expression.from_func(x_array=x_array, t_array=t_array, func=func)

    y.plot(t=1)
    y.plot(x=0)

if __name__ == "__main__":
    main()
