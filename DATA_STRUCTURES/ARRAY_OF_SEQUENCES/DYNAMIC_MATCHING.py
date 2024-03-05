class DynamicMatching:
    """Example for tuple matching
    """
    def __init__(self, a : int, b : int, c : int, *values : int) -> None:
        """Initializes the class to unpackage values

        Args:
            a int: The first argument
            b int: The second argument
            c int: The third argument
            *args int: The remaining arguments to be dynamically unpackaged
        """
        self.packaged_values    = (a, b, c, *values)
    # The number for unpackaging with the exact pattern
    def exact_arguments_unpackager(self):
        """Unpackages arguments in the exact pattern they were provided
        >>> dm = DynamicMatching(1, 2, 3, 4, 5, 6, 7)
        >>> dm.exact_arguments_unpackager()
        1 2 3 [4, 5, 6, 7]
        """
        a, b, c, *values = self.packaged_values
        print(a, b, c, values)
    def less_arguments_unpackager(self):
        """Unpackages less arguments than the number of the not optional ones
        >>> dm = DynamicMatching(1, 2, 3, 4, 5, 6, 7)
        >>> dm.less_arguments_unpackager()
        1 2 [3, 4, 5, 6, 7]
        """
        a, b, *values = self.packaged_values
        print(a, b, values)
    def more_arguments_unpackager(self):
        """Unpackages less arguments than the number of the not optional ones
        >>> dm = DynamicMatching(1, 2, 3, 4, 5, 6, 7)
        >>> dm.more_arguments_unpackager()
        1 2 3 4 [5, 6, 7]
        """
        a, b, c, d, *values = self.packaged_values
        print(a, b, c, d, values)

def main():
    dm = DynamicMatching(1, 2, 3, 4, 5, 6, 7)
    print("\nPair Matching")
    dm.exact_arguments_unpackager()
    print("\nLess Matching")
    dm.less_arguments_unpackager()
    print("\nMore Matching")
    dm.more_arguments_unpackager()

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()