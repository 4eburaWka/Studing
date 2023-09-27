class NAME_OF_CLASS:
    def __init__(self, A) -> None:
        self.__A = A

a = NAME_OF_CLASS(2)
# a.__init__.__code__.co_varnames[1] = 3

print(a.__init__.__code__.co_varnames)