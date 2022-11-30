from productions.production import Production
from productions.production_type import ProductionType


class SimpleProduction(Production):
    def __init__(self, name, rhs, parent, next_production):
        super().__init__(name)
        self.__rhs = rhs
        self.__parent = parent
        self.__next_simple_production = next_production
        self._ProductionBase__production_type = ProductionType.SIMPLE_PRODUCTION

    @property
    def next_simple_production(self):
        return self.__next_simple_production

    @property
    def rhs(self):
        return self.__rhs

    @property
    def parent(self):
        return self.__parent

    def __str__(self):
        return f"{self.name} --> {' & '.join([str(e) for e in self.__rhs])}"

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        if len(self.rhs) != len(other.rhs) or self.name != other.name:
            return False
        return all(e1 == e2 for e1, e2 in zip(self.rhs, other.rhs))
