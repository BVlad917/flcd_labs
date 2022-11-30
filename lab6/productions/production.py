from abc import ABC


class Production(ABC):
    def __init__(self, name):
        self.__name = name
        self.__production_type = None

    @property
    def name(self):
        return self.__name

    @property
    def production_type(self):
        return self.__production_type
