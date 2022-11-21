class Production:
    def __init__(self, production_string):
        self.__parse_string(production_string)

    def __parse_string(self, production_string):
        elems = production_string.split('->')
        self.__left_hand_side = elems[0]
        self.__right_hand_side = elems[1].split('|')

    @property
    def left_hand_side(self):
        return self.__left_hand_side

    @property
    def right_hand_side(self):
        return self.__right_hand_side

