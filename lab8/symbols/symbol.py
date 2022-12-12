from abc import ABC


class Symbol(ABC):
    """
    Symbol abstract parent class. Holds the following:
    - name: the name of the symbol; str
    - symbol_type: the type of the symbol (terminal, non terminal, epsilon); member of SymbolType enum
    """
    def __init__(self, name: str):
        self.__name = name
        self.__symbol_type = None

    @property
    def symbol_type(self):
        return self.__symbol_type

    @property
    def name(self):
        return self.__name

    def __eq__(self, other):
        return self.symbol_type == other.symbol_type and self.name == other.name

    def __repr__(self):
        return str(self)
