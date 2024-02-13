"""
>>> print(tests())
[True, True, False, True, True, False]

"""

from abc import abstractmethod

class TruthyAbs():
    @abstractmethod
    def __init__(self, t):
        self._a = t

class Truthy(TruthyAbs):
    """
    A class without len or bool will be always True as it is not intuitive
    >>> bool(Truthy())
    True
    """
    def __init__(self):
        super().__init__(None)

class NotTruthyB(TruthyAbs):
    """"
    A class with bool will be True or False depending in the method itself
    >>> bool(NotTruthyB(False))
    False
    >>> bool(NotTruthyB(True))
    True
    """
    def __init__(self, t):
        super().__init__(t)
    def __bool__(self):
        return self._a

class NotTruthyL(TruthyAbs):
    """
    A class with len will be True or False depending in the result of the method itself (0: False; not 0: True)
    >>> bool(NotTruthyL([1, 1]))
    True
    >>> bool(NotTruthyL([1, 1]))
    True
    """
    def __init__(self, t):
        super().__init__(t)
    def __len__(self):
        return len(self._a)

def tests():
    b_list = list()
    b_list.append(bool(Truthy()))
    b_list.append(bool(Truthy()))           # A class without len or bool will be always True as it is not intuitive
    b_list.append(bool(NotTruthyB(False)))
    b_list.append(bool(NotTruthyB(True)))
    b_list.append(bool(NotTruthyL([1, 1])))
    b_list.append(bool(NotTruthyL([])))
    return b_list

if __name__ == "__main__":
    import doctest
    doctest.testmod()
