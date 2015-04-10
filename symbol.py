# coding=utf-8

from sympy import Function, Matrix, symbols, Symbol


class Vector(object):
    def __init__(self, items):
        self.vector = Matrix(items)


class SymbolVector(Vector):
    """ A vector representation for a list of symbol names. """
    def __init__(self, names):
        symbols = []
        for name in names:
            symbol = Symbol(name)
            symbols.append(symbol)

        super(SymbolVector, self).__init__(symbols)


class FunctionVector(Vector):
    """ A vector representation for a list of functions. """
    def __init__(self, names, independent_symbols):
        functions = []
        for name in names:
            function = Function(name)(*independent_symbols)
            functions.append(function)

        super(FunctionVector, self).__init__(functions)

#: Axial coordinate
x1 = Symbol('x1')

#: 1D initial twist & curvature
k = FunctionVector(['k1', 'k2', 'k3'], (x1, ))

if dynamic_flag:

    #: Time
    t = Symbol('t')

    #### Inner Variables #######################################################

    #: 1D strain
    gamma = FunctionVector(['γ11', '2γ12', '2γ13'], (x1, t))

    #: 1D curvature & twist
    kappa = FunctionVector(['κ1', 'κ2', 'κ3'], (x1, t))

    #: 1D velocity
    V = FunctionVector(['V1', 'V2', 'V3'], (x1, t))

    #: 1D angular velocity
    omega = FunctionVector(['Ω1', 'Ω2', 'Ω3'], (x1, t))

    #### Outer Variables #######################################################

    #: Outer variable for 1D strain
    outer_gamma = FunctionVector(['Oγ11', 'O2γ12', 'O2γ13'], (x1, t))

    #: Outer variable for 1D curvature & twist
    outer_kappa = FunctionVector(['Oκ1', 'Oκ2', 'Oκ3'], (x1, t))

    #: Outer 1D velocity
    outer_V = FunctionVector(['OV1', 'OV2', 'OV3'], (x1, t))

    #: Outer 1D angular velocity
    outer_omega = FunctionVector(['OΩ1', 'OΩ2', 'OΩ3'], (x1, t))

    #### Loading Variables #####################################################

    #: Applied forces
    f = FunctionVector(['f1', 'f2', 'f3'], (x1, t))

    #: Applied moments
    m = FunctionVector(['m1', 'm2', 'm3'], (x1, t))

else:

    #### Inner Variables #######################################################

    #: 1D strain
    gamma = FunctionVector(['γ11', '2γ12', '2γ13'], (x1, ))

    #: 1D curvature & twist
    kappa = FunctionVector(['κ1', 'κ2', 'κ3'], (x1, ))

    #: 1D velocity
    V = FunctionVector(['V1', 'V2', 'V3'], (x1, ))

    #: 1D angular velocity
    omega = FunctionVector(['Ω1', 'Ω2', 'Ω3'], (x1, ))

    #### Outer Variables #######################################################

    #: Outer variable for 1D strain
    outer_gamma = FunctionVector(['Oγ11', 'O2γ12', 'O2γ13'], (x1, ))

    #: Outer variable for 1D curvature & twist
    outer_kappa = FunctionVector(['Oκ1', 'Oκ2', 'Oκ3'], (x1, ))

    #: Outer 1D velocity
    outer_V = FunctionVector(['OV1', 'OV2', 'OV3'], (x1, ))

    #: Outer 1D angular velocity
    outer_omega = FunctionVector(['Oomega1', 'Oomega2', 'Oomega3'], (x1, ))

    #### Loading Variables #####################################################

    #: Applied forces
    f = FunctionVector(['f1', 'f2', 'f3'], (x1, ))

    #: Applied moments
    m = FunctionVector(['m1', 'm2', 'm3'], (x1, ))
