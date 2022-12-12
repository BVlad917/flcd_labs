class ParserOutput:
    def __init__(self, output_msg, configuration):
        self.__output_msg = output_msg
        self.__representation = self.__build_string_of_productions(configuration)

    @property
    def output_msg(self):
        return self.__output_msg

    @property
    def representation(self):
        return self.__representation

    def save_to_file(self, file_path="outputs/representation.out"):
        with open(file_path, 'w') as f:
            f.write(self.__output_msg + "\n")
            f.write("PRODUCTIONS STRING: " + self.__representation + "\n")

    @staticmethod
    def __build_string_of_productions(configuration):
        return 'NaN' if configuration is None else ' '.join(symbol.name for symbol in configuration.working_stack)
