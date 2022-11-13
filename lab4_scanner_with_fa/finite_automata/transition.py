class Transition:
    """
    Transition representation. Follows the following convention:
    δ(state, accepted) = result
    """
    def __init__(self, state: str, accepted: str, result: str) -> None:
        self.__state = state
        self.__accepted = accepted
        self.__result = result

    def get_state(self) -> str:
        return self.__state

    def get_accepted(self) -> str:
        return self.__accepted

    def get_result(self) -> str:
        return self.__result

    def __str__(self) -> str:
        return f"δ({self.__state}, {self.__accepted}) = {self.__result}"

    def __repr__(self) -> str:
        return f"δ({self.__state}, {self.__accepted}) = {self.__result}"
