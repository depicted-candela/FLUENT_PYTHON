# from ..PYTHON_DATA_MODEL.FRENCH_DECK import FrenchDeck

def slices_the_iterable_french_deck(iterable, slicer: slice):
    """Slice in a french deck with given slicers
    >>> slices_the_iterable_french_deck('bicycle', slice(0, len('bicycle'), 3))
    'bye'
    >>> slices_the_iterable_french_deck('Nicolas ALberto', slice(-3, 0, -2)) 
    'rbAslc'
    >>> # Does not include the N character because slices does not use the last item.
    >>> # In this case, as we are moving ourselves from end to start, the first item is not used
    """
    # french_deck = FrenchDeck()
    return iterable[slicer]

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print("Conclusion")
    print("The direction always have relevance with the properties of slicers")
    print("An slicer can be created with the slice() builf-in method")
    print("Slicer objects can be used in extensive algoritms")