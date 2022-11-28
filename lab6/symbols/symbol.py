from abc import ABC


class Symbol(ABC):
    """
    Symbol abstract parent class. Holds the following:
    - string: the string of the symbol; str
    - symbol_type: the type of the symbol (terminal, non terminal, epsilon); member of SymbolType enum
    """
    def __init__(self, string: str):
        self.__string = string
        self.__symbol_type = None

    @property
    def symbol_type(self):
        return self.__symbol_type

    @property
    def string(self):
        return self.__string

    def __eq__(self, other):
        return self.symbol_type == other.symbol_type and self.string == other.string

    def __str__(self):
        return f'SYMBOL("{self.string}")'

    def __repr__(self):
        return str(self)
