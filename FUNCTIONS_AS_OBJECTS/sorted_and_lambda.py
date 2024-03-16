class FruitSorter:
    fruits  = ('strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana')
    def reverse(self, word):
        return word[::-1]
    def rhymes_words_with_reverse(self):
        """
        >>> fruits_sorter = FruitSorter()
        >>> fruits_sorter.rhymes_words_with_reverse()
        ['banana', 'apple', 'fig', 'raspberry', 'strawberry', 'cherry']
        """
        return sorted(self.fruits, key=self.reverse)
    def rhymes_words_with_lambda(self):
        """
        >>> fruits_sorter = FruitSorter()
        >>> fruits_sorter.rhymes_words_with_lambda()
        ['banana', 'apple', 'fig', 'raspberry', 'strawberry', 'cherry']
        """
        return sorted(self.fruits, key=lambda word: word[::-1]) # Nice

if __name__ == "__main__":
    import doctest
    doctest.testmod()