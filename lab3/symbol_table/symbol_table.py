from collections import defaultdict

DEFAULT_CAPACITY = 17


class SymbolTable:
    def __init__(self, table_size=DEFAULT_CAPACITY):
        self.__hash_table = defaultdict(list)
        self.__capacity = table_size
        self.__size = 0

    def __str__(self):
        output_string = ""
        for hash_idx, values_list in sorted(self.__hash_table.items()):
            for idx, value in enumerate(values_list):
                output_string += f"({hash_idx}, {idx}) ---> {value}\n"
        return output_string

    def add_elem(self, symbol):
        """
        Add a new symbol to the symbol table. If the element already exists, throw ValueError
        :param symbol: the new symbol to insert in the symbol table; number or string
        """
        key, elem_index = self.find_symbol_position(symbol)
        if elem_index != -1:
            raise ValueError("Element already in the symbol table")
        else:
            self.__hash_table[key].append(symbol)
            self.__size += 1

    def get_size(self):
        """
        :return: the current size (number of symbols) of the symbol table
        """
        return self.__size

    def find_symbol_position(self, symbol):
        """
        Find the position of the symbol in the symbol table
        :param symbol: the symbol which should be searched; number or string
        :return: a pair with the position in the hash table at first position, and position in the collision list
        (if the symbol exists) or -1 (if the symbol doesn't exist) at the second position
        """
        key = self.__h(symbol)
        if symbol in self.__hash_table[key]:
            return key, self.__hash_table[key].index(symbol)
        else:
            return key, -1

    def __h(self, symbol):
        """
        Hash function. Adds the ASCII values of the characters in the given symbol, finds the ASCII sum, and
        computes the modulo with the argument <m> of the symbol table
        :param symbol: input to find the hash value for; number or string
        :return: hash value for the given input; int
        """
        str_value = str(symbol)
        ascii_sum = sum([ord(c) for c in str_value])
        return ascii_sum % self.__capacity
