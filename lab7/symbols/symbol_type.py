from enum import Enum


class SymbolType(Enum):
    TERMINAL = 1
    NON_TERMINAL = 2
    EPSILON = 3
    SIMPLE_PRODUCTION = 4
    SUPER_PRODUCTION = 5
