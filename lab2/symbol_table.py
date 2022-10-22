from collections import defaultdict

DEFAULT_SIZE = 17


class SymbolTable:
    def __init__(self):
        self.__hashtable = defaultdict(list)
        self.__m = DEFAULT_SIZE

    def add_elem(self, elem):
        key, elem_index = self.find_element_position(elem)
        if elem_index != -1:
            raise ValueError("Element already in the symbol table")
        else:
            self.__hashtable[key].append(elem)

    def find_element_position(self, elem):
        key = self.h(elem)
        if elem in self.__hashtable[key]:
            return key, self.__hashtable[key].index(elem)
        else:
            return key, -1

    def h(self, value):
        str_value = str(value)
        ascii_sum = sum([ord(c) for c in str_value])
        return ascii_sum % self.__m
