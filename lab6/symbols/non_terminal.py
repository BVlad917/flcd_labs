from symbols.symbol import Symbol
from symbols.symbol_type import SymbolType


class NonTerminal(Symbol):
    """
    Symbol representing a non-terminal
    """
    def __init__(self, string: str):
        super().__init__(string)
        self._Symbol__symbol_type = SymbolType.NON_TERMINAL

    def __str__(self):
        return f'NON-TERMINAL("{self.name}")'
