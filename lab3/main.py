import re


class Scanner:
    def __init__(self, symbol_table):
        self.__symbol_table = symbol_table

    @staticmethod
    def read_file_lines(file_path):
        with open(file_path, 'r') as f:
            lines = f.readlines()
        lines = [(line_number, line.rstrip()) for line_number, line in enumerate(lines)]
        return lines

    def split_line(self, line):
        # line = re.split("(=)|(<)|(>)|(;)|( )|(\()|(\))", line)
        # line = [t for t in line if t is not None and t != ' ' and t != '']
        string_constants = []
        char_constants = []
        non_string_or_char = []
        string_delim_indexes = self.find_indexes_of_char(line, '"')
        char_delim_indexes = self.find_indexes_of_char(line, "'")
        all_delimiters = sorted(string_delim_indexes + char_delim_indexes)
        if len(string_delim_indexes):
            string_constants = self.get_strings_between_indexes(line, string_delim_indexes)
        if len(char_delim_indexes):
            char_constants = self.get_strings_between_indexes(line, char_delim_indexes)
        if len(all_delimiters):
            non_string_or_char = self.get_strings_outside_indexes(line, non_string_or_char)
        return string_constants, char_constants, non_string_or_char

    @staticmethod
    def find_indexes_of_char(line, char):
        return [idx for idx, ltr in enumerate(line) if ltr == char]

    @staticmethod
    def get_strings_between_indexes(line, indexes):
        return [line[idx1: idx2 + 1] for idx1, idx2 in zip(indexes[:-1], indexes[1:])]

    @staticmethod
    def get_strings_outside_indexes(line, indexes):
        strings = []
        current_start = 0
        for idx1, idx2 in zip(indexes[:-1], indexes[1:]):
            current_end = idx1
            strings.append(line[current_start: current_end])
            current_start = idx2
        return strings

    def scan_file(self, file_path):
        lines = self.read_file_lines(file_path)
        for line_number, line in lines:
            line = line.strip()
            string_constants, non_strings = self.split_line(line)
            print(line + ": " + str(string_constants) + ", " + str(non_strings))


scanner = Scanner(0)
scanner.scan_file("./lab3/programs/p1.txt")
