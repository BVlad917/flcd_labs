from symbols.symbol import Symbol
from symbols.symbol_type import SymbolType


class Epsilon(Symbol):
    """
    Symbol representing the Epsilon(ε) symbol
    """
    def __init__(self):
        super().__init__("ε")
        self._Symbol__symbol_type = SymbolType.EPSILON

    def __str__(self):
        return f'EPSILON("{self.name}")'
