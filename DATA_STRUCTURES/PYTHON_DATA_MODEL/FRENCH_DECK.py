import collections

# Created a new Card class wrapped by 'namedtuple' with two named new variables (rank and suit)
# and no methods because the simplicity of the class
Card = collections.namedtuple('Card', 'rank suit')

# The shuffler class to obtain all the possible cards in a French Deck
class FrenchDeck:
    # Creates as a variable a list of strings for all possible values in a single suit
    # using list comprehension: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, and K
    ranks = [str(i) for i in range(2, 11)] + list('AJQK')
    # Creates as a variable a list of strings for all possible suits: diamonds, spades
    # hearts, and clubs
    suits = 'diamonds spades hearts clubs'.split()
    
    # Initialize the class
    def __init__(self):
        # Saves all the possible Cards in this French set using the standardized
        # class for a single object within the set
        self._cards = [Card(r, s) for r in self.suits for s in self.ranks]
    
    # Returns the number of single objects within the French set
    def __len__(self):
        return len(self._cards)
    
    # Returns a desired item searched by position in the list of cards (ordered
    # by suit first and then by rank)
    def __getitem__(self, item):
        return self._cards[item]

def random_choices(fd):
    from random import choice
    print("\n")
    print("More Python's native tools")
    print("\n")
    print(">>> choice(fd)")
    print(choice(fd))
    print(">>> choice(fd)")
    print(choice(fd))
    print(">>> choice(fd)")
    print(choice(fd))
    print("\n")

    print("As you can see, our created __len__() method is not needed for our class since len() is a fundamental Python's construct, but what\ncan accept the fundamental Python's len()?")
    print("As you can see, our created __getitem__(item) method is not needed for our class since [] is a fundamental Python's construct, but\nwhat can accept the fundamental Python's []?")
    print("That's the reason for delving in the fundamental collections of Python, like the Java native Collections Framework, but here funda-")
    print("mentals are used explicitly in the sense that is expectedto work directly with Python's native collections")
    print("As you can see, again the native Python's fundamentals can iterate over other native Python's fundaments, saving a lot of code lines.")

if __name__ == "__main__":
    import doctest
    fd = FrenchDeck() # Instance creation of the French Deck
    doctest.testfile("FRENCH_DECK.txt", globs={'fd': fd})
    random_choices(fd)
    print("Up to now is clear how native Python's fundamentals help us saving code lines and own brain effort not memorizing all methods with the same\npurpose for each type of data structure that we could create.")
