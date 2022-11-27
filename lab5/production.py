class Production:
    def __init__(self, lhs, rhs):
        self.__lhs = lhs
        self.__rhs = rhs

    @property
    def lhs(self):
        return self.__lhs

    @property
    def rhs(self):
        return self.__rhs

    def __str__(self):
        return f"{' & '.join([str(e) for e in self.__lhs])} --> {' & '.join([str(e) for e in self.__rhs])}"

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        if len(self.lhs) != len(other.lhs) or len(self.rhs) != len(other.rhs):
            return False
        lhs_eq = all(e1 == e2 for e1, e2 in zip(self.lhs, other.lhs))
        rhs_eq = all(e1 == e2 for e1, e2 in zip(self.rhs, other.rhs))
        return lhs_eq and rhs_eq
