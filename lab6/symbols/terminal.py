from symbols.symbol import Symbol
from symbols.symbol_type import SymbolType


class Terminal(Symbol):
    """
    Symbol representing a terminal.
    """
    def __init__(self, string: str):
        super().__init__(string)
        self._Symbol__symbol_type = SymbolType.TERMINAL

    def __str__(self):
        return f'TERMINAL("{self.string}")'
