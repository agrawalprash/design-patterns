#: Interface
class FullSolver(object):
    def __init__(self):
        self.mesh_generator = MeshGenerator()
        self.cross_sectional_solver = CrossSectionalSolver()
        self.eqn_generator = EqnGenerator()
        self.eqn_solver = EqnSolver()

    def generate_mesh(self):
        self.mesh_generator.generate_mesh()

    def generate_equations(self):
        constitutive_relationship=self.cross_sectional_solver.solve()
        self.eqn_generator.generate_equations(constitutive_relationship)

    def solve(self):
        mesh = self.generate_mesh()
        eqns = self.generate_equations()
        self.eqn_solver.solve(eqns, mesh)


class DynamicFullSolver(FullSolver):

    def __init__(self, classical=True, linear=True, mode='transient'):
        self.mesh_generator = DynamicMeshGenerator()
        self.cross_sectional_solver = DynamicCrossSectionalSolver()

        if classical:
            self.eqn_generator = DynamicClassicalEqnGenerator()
        else:
            self.eqn_generator = DynamicTimoshenkoEqnGenerator()

        if mode == 'transient':
            self.eqn_solver = DynamicTransientEqnSolver(linear=linear)
        elif mode == 'eigenvalue':
            self.eqn_solver = DynamicEigenValueEqnSolver(linear=linear)
        else:
            self.eqn_solver = StaticEqnSolver(linear=linear)


class StaticFullSolver(FullSolver):
    def __init__(self):
        self.mesh_generator = StaticMeshGenerator()
        self.cross_sectional_solver = StaticCrossSectionalSolver()
        self.eqn_generator = StaticEqnGenerator()
        self.eqn_solver = StaticEqnSolver()


class SolverFactory(object):
    """ Factory to create FullSolver objects
    """

    def create_solver(self, dynamic):
        """ Create a solver of class FullSolver
        """
        if dynamic:
            return DynamicFullSolver()
        else:
            return StaticFullSolver()

if __name__ == "__main__":
    solver = SolverFactory().create_solver(dynamic=True)
    solver.solve()