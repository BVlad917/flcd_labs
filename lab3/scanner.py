import re
from collections import defaultdict

from symbol_table.symbol_table import SymbolTable


class Scanner:
    def __init__(self, tokens_file_path='./utils/tokens.in'):
        self.__tokens_file_path = tokens_file_path
        self.__symbol_table = SymbolTable()
        self.__pif = list()
        self.__read_tokens_file()

    def scan_program(self, file_path):
        """
        Scan a program from the given path and look for lexical error
        :param file_path: the path of the program; string
        :return: program internal form (list), symbol table (SymbolTable), and output_message
        """
        lines = self.__read_file_lines(file_path)
        output_message = "LEXICALLY CORRECT"
        for line_number, line in lines:
            line = line.strip()  # remove spaces at the beginning and end
            try:
                self.scan_line(line)
            except (KeyError, ValueError) as err:
                # if we get here => lexical error
                # create a more readable error message and print it
                err_str = str(err).strip("'")
                col_position = err_str.index(':')
                err_str = err_str[:col_position + 1] + "\n" + err_str[col_position + 2:]
                output_message = f"LEXICAL ERROR AT LINE {line_number + 1}: {err_str}"
        return self.__pif, self.__symbol_table, output_message

    def scan_line(self, line):
        """
        Scan a given line for lexical errors using the algorithm:
            1. Tokenize
            2. Classify
            3. Codify
        The class variables self.__pif and self.__symbol table will be modified at the end of the function
        :param line: a line from the program; string
        """
        tokens = self.tokenize(line)
        tokens_category = self.classify(tokens)
        self.codify(tokens, tokens_category)

    def tokenize(self, line):
        """
        Tokenize a program line and return the tokens
        :param line: the line to be tokenized; string
        :return: the tokens in the line
        """
        strings, chars, non_strings_or_chars = self.__extract_strings_and_chars(line)
        tokens = strings + chars
        tokens += self.__split_non_strings_or_chars(non_strings_or_chars)
        return tokens

    def classify(self, tokens):
        """
        Classify tokens from a list into one of the 5 categories:
            reserved keyword, constant, operator, separator, identifier
        :param tokens: list of tokens
        :return: dictionary mapping category_type->list_of_tokens_matching_category_type
        """
        tokens_category = defaultdict(list)
        for token in tokens:
            if self.__is_reserved_word(token):
                tokens_category["reserved_words"].append(token)
            elif self.__is_char_constant(token) or self.__is_str_constant(token) or self.__is_int_constant(token):
                tokens_category["constants"].append(token)
            elif self.__is_operator(token):
                tokens_category["operators"].append(token)
            elif self.__is_separator(token):
                tokens_category["separators"].append(token)
            elif self.__is_identifier(token):
                tokens_category["identifiers"].append(token)
            else:
                raise ValueError(f"Incorrect token: {token}")
        return tokens_category

    def codify(self, tokens, tokens_category):
        """
        Add a list of tokens to the Symbol Table and the Program Internal Form
        :param tokens: list of tokens to be added
        :param tokens_category: dictionary which has all tokens classified by type; output of the method <classify>
        """
        # add the identifiers to the symbol table
        for identifier in tokens_category["identifiers"]:
            try:
                self.__symbol_table.add_elem(identifier)
            except ValueError:
                pass  # identifier already in the symbol table
        # add the constants to the symbol table
        for constant in tokens_category["constants"]:
            try:
                self.__symbol_table.add_elem(constant)
            except ValueError:
                pass  # constant already in the symbol table
        # add all (possible) tokens to the program internal form (PIF)
        for token in tokens:
            position_pair = self.__symbol_table.find_symbol_position(token)
            if position_pair[1] == -1:
                self.__pif.append((token, (-1, -1)))
            else:
                self.__pif.append((token, position_pair))

    @staticmethod
    def __is_identifier(word):
        """
        Check if the input is an identifier (using the defined rules of the program)
        """
        return re.match('^(_|[a-zA-Z])([a-zA-Z]|[0-9])*$', word)

    @staticmethod
    def __is_int_constant(word):
        """
        Check if the input is an integer constant (using the defined rules of the program)
        """
        return re.match('^(-)?([1-9]+[0-9]*)$|^0$', word)

    def __is_char_constant(self, word):
        """
        Check if the input is a char constant (using the defined rules of the program)
        """
        if len(word) != 3 or word[0] != "'" or word[-1] != "'":
            return False
        regex_pattern = r'^[a-zA-Z]$|^[0-9]$|^' + self.__get_regex_splitter() + r'$'
        return re.match(regex_pattern, word[1])

    def __is_str_constant(self, word):
        """
        Check if the input is a string constant (using the defined rules of the program)
        """
        if len(word) < 3 or word[0] != '"' or word[-1] != '"':
            return False
        regex_pattern = r'^(([a-zA-Z])|([0-9])|' + self.__get_regex_splitter() + ')+$'
        return re.match(regex_pattern, word[1:-1])

    def __is_operator(self, word):
        """
        Check if the input is an operator
        """
        return word in self.__operators

    def __is_separator(self, word):
        """
        Check if the input is a separator
        """
        return word in self.__separators

    def __is_reserved_word(self, word):
        """
        Check if the input is a reserved word
        """
        return word in self.__reserved_words

    @staticmethod
    def __read_file_lines(file_path):
        """
        Read a file and return the lines in a list, along with the line number (starting from 0)
        :param file_path: path of the file; string
        :return: list of tuples containing (line_number, line)
        """
        with open(file_path, 'r') as f:
            lines = f.readlines()
        lines = [(line_number, line.rstrip()) for line_number, line in enumerate(lines)]
        return lines

    def __read_tokens_file(self):
        """
        Read the program operators, separators, and reserved keywords from the tokens.in file
        """
        lines = self.__read_file_lines(self.__tokens_file_path)
        for line_num, line in lines:
            split_line = line.split(':', 1)
            if not len(split_line):
                continue
            symbols_type = split_line[0]
            symbols = split_line[1].split(',')
            if symbols_type == 'operators':
                self.__operators = symbols
            elif symbols_type == 'separators':
                self.__separators = symbols
            elif symbols_type == 'reserved_words':
                self.__reserved_words = symbols

    def __extract_strings_and_chars(self, line):
        """
        Takes a string (the program line) as input and extracts from this line all parts which are between
        single or double quotes.
        :param line: line in the program; string
        :return: string constants, char constants, and everything else that is left
        example:
            input: write("Hi, how are you doing?")
            output: string_constants = ["Hi, how are you doing?"]
                    char_constants = []
                    non_string_or_char = ["write(", ")"]
        """
        grouped_string_delim = self.__group_quotes(line, '"')
        grouped_char_delim = self.__group_quotes(line, "'")
        all_delimiters = sorted(grouped_string_delim + grouped_char_delim, key=lambda x: x[0])
        string_constants = self.__get_strings_between_indexes(line, grouped_string_delim)
        char_constants = self.__get_strings_between_indexes(line, grouped_char_delim)
        non_string_or_char = self.__get_strings_outside_indexes(line, all_delimiters) if len(all_delimiters) else [line]
        return string_constants, char_constants, non_string_or_char

    def __split_non_strings_or_chars(self, non_strings_or_chars_list):
        """
        Takes a list of split line portions which do NOT contain string/char constants and splits it
        :param non_strings_or_chars_list: list of split line portions; does not contain any string/char constants
        :return: the input list of split line portions is further subdivided by separators, operators, etc
        example1: input: ["if (c<min) {"]
                  output: ["if", "(", "c", "<", "min", ")", "{"]
        example2: input: ["write(", ")"]
                  output: ["write", "(", ")"]
        """
        numbers_and_non_constants = []
        for line_portion in non_strings_or_chars_list:
            line_portion = re.split(self.__get_regex_splitter(), line_portion)
            line_portion = [t for t in line_portion if t is not None and t != ' ' and t != '']
            numbers_and_non_constants.extend(line_portion)
        return numbers_and_non_constants

    def __group_quotes(self, line, quote_type):
        """
        Group all appearances of quotes by opening/closing quotes
        :param line: the line to be searched; string
        :param quote_type: the type of quote to find groups for; " or '
        :return: list of pairs of indices of the grouped quotes
        example: input: line = this" is a string" and it "contains" quotes
                        quote_type = "
                 output: [(4, 17), (26, 35)]
        """
        quote_indexes = self.__find_indexes_of_char(line, quote_type)
        num_quotes = len(quote_indexes)
        if num_quotes % 2 == 1:
            quote_description = "double" if quote_type == '"' else "single"
            raise KeyError(f"Missing {quote_description} quote in the following line: {line}")
        return [(quote_indexes[i], quote_indexes[j])
                for i, j in zip(range(0, num_quotes, 2), range(1, num_quotes, 2))]

    def __get_regex_splitter(self):
        """
        Construct the regex pattern used to split a line to maximum granularity. Uses all operators and separators
        :return: a regex pattern, string
        """
        splitter_string = r""
        escape_chars = ['*', '+', '(', ')', '[', ']']  # have meaning in regex, should be escaped with '\'
        for splitter_char in self.__operators + self.__separators:  # the operators and separators are used to split
            if splitter_char in escape_chars:
                splitter_string += '(' + f"\\{splitter_char}" + ')' + '|'
            else:
                splitter_string += '(' + splitter_char + ')' + '|'
        return splitter_string[:-1]  # ignore the last '|' which was added at the end of the loop

    @staticmethod
    def __find_indexes_of_char(string, char):
        """
        Find all the indexes of <char> in <string> and returns them in a list
        """
        return [idx for idx, ltr in enumerate(string) if ltr == char]

    @staticmethod
    def __get_strings_between_indexes(string, index_pairs):
        """
        Return the substrings from <line> delimited by the indices from <index_pairs>
        NB: The indexes are INCLUSIVE on both ends
        :param string: a string
        :param index_pairs: list of pairs of indices
        :return: list of substrings
        example: input:  string = This is some string to be split
                         index_pairs = [(0, 3), (5, 7), (13, 17)]
                 output: ["This", "is ", "strin"]
        """
        return [string[start: end + 1] for start, end in index_pairs]

    @staticmethod
    def __get_strings_outside_indexes(string, indexes):
        """
        Opposite operation of <__get_strings_between_indexes>
        Return the substring from <line> which are NOT delimited by the indices from <index_pairs>
        :param string: a string
        :param indexes: list of pairs of indices
        :return: list of substrings
        example: input:  string = This is some string to be split
                         index_pairs = [(0, 3), (5, 7), (13, 17)]
                 output: [" ", "some ", "g to be split"]
        """
        if not len(indexes): return []
        strings = [string[:indexes[0][0]]]
        start = indexes[0][1]
        for index_pair in indexes[1:]:
            end = index_pair[0]
            strings.append(string[start + 1: end])
            start = index_pair[1]
        strings.append(string[indexes[-1][1] + 1:])
        return [s for s in strings if len(s) > 0]
