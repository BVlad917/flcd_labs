from productions.simple_production import SimpleProduction
from productions.production import Production
from productions.production_type import ProductionType


class SuperProduction(Production):
    def __init__(self, lhs, all_rhs):
        super().__init__('_'.join(elem.string for elem in lhs))
        self._ProductionBase__production_type = ProductionType.SUPER_PRODUCTION
        self.__lhs = lhs
        self.__create_super_production(all_rhs)

    @property
    def lhs(self):
        return self.__lhs

    @property
    def rhs_head(self):
        return self.__head

    @property
    def rhs_length(self):
        return self.__length

    @property
    def all_simple_productions(self):
        productions = []
        head = self.__head
        while head is not None:
            productions.append(head)
            head = head.next_simple_production
        return productions

    def __create_super_production(self, all_rhs):
        self.__length = len(all_rhs)
        prev_production = None
        for idx, rhs in enumerate(reversed(all_rhs)):
            p = SimpleProduction(f"{self.name}{self.__length - idx}", rhs, self, prev_production)
            if idx == len(all_rhs) - 1:
                self.__head = p
            prev_production = p

    def __str__(self):
        string = f"{self.name} --> "
        for p in self.all_simple_productions:
            string += '&'.join(str(e) for e in p.rhs) + ' | '
        return string[:-3]

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        if self.name != other.name or len(self.lhs) != len(other.lhs):
            return False
        if not all(e1 == e2 for e1, e2 in zip(self.lhs, other.lhs)):
            return False
        return all(e1 == e2 for e1, e2 in zip(self.all_simple_productions, other.all_simple_productions))
