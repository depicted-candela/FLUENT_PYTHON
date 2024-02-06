import math

class Vector:
    """
    This class autotested by running the python file shows how the magic methods uses native Python's idioms
    """
    def __init__(self, x, y):
        self._x = x
        self._y = y
    def __repr__(self):
        """
        __repr__ method applies the repr() method directly to a user-defined object with custom representation
        >>> repr(Vector(2, 1))
        'Vector(2, 1)'
        """
        return f"Vector({self._x}, {self._y})"
    def __abs__(self):
        """
        __abs__ method applies the abs() method directly to a user-defined object with custom absolute value, here hypotenuse
        >>> abs(Vector(2, 1))
        2.23606797749979
        """
        return math.hypot(self._x, self._y)
    def __bool__(self):
        """
        __bool__ method applies the bool() method directly to a user-defined object with custom boolean value, here if absolute value (hypotenuse of the vector) is different to 0, the boolean value is True
        >>> bool(Vector(2, 1))
        True
        >>> bool(Vector(0, 0))
        False
        """
        return bool(abs(self))
    def __add__(self, other):
        """
        __abs__ method applies the + operand directly to a user-defined object with custom operand +, here addition between Vector's dimension
        >>> repr(Vector(2, 1) + Vector(4, 2))
        'Vector(6, 3)'
        """
        return Vector(self._x + other._x, self._y + other._y)
    def __sub__(self, other):
        """
        __sub__ method applies the - operand directly to a user-defined object with custom operand -, here substraction between Vector's dimension
        >>> repr(Vector(2, 1) - Vector(4, 2))
        'Vector(-2, -1)'
        """
        return Vector(self._x - other._x, self._y - other._y)
    def __mul__(self, other):
        """
        __mul__ method applies the * operand directly to a user-defined object with custom operand *, here multiplication between Vector's dimension
        >>> repr(Vector(2, 1) * Vector(4, 2))
        'Vector(8, 2)'
        """
        return Vector(self._x * other._x, self._y * other._y)

if __name__ == "__main__":
    import doctest
    doctest.testmod()