from collections import defaultdict

DEFAULT_PRIME = 53


class SymbolTable:
    def __init__(self):
        self.__hashtable = defaultdict(list)
        self.__m = DEFAULT_PRIME

    def add_elem(self, elem):
        key = self.h(elem)
        if elem in self.__hashtable[key]:
            raise ValueError("Element already in the symbol table")
        else:
            self.__hashtable[key].append(elem)

    def find_element_position(self, elem):
        key = self.h(elem)
        if elem in self.__hashtable[key]:
            return key
        else:
            return -1

    def h(self, value):
        if isinstance(value, (int, float, complex)):
            value = str(value)
        return len(value) % self.__m
