class ParserOutput:
    def __init__(self, configuration):
        self.__representation = self.__build_string_of_productions(configuration)

    @property
    def representation(self):
        return self.__representation

    def save_to_file(self, file_path="outputs/representation.out"):
        with open(file_path, 'w') as f:
            f.write(self.__representation)

    @staticmethod
    def __build_string_of_productions(configuration):
        return ' '.join(symbol.name for symbol in configuration.working_stack)
