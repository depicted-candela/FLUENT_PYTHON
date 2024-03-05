def get_creators(record: dict) -> list:
    """Get the creator(s) of a book

    Args:
        record (dict): values coming in JSON schema trasformed to a dictionary for Python 

    Raises:
        ValueError: when the dict has just the name of a book
        ValueError: when the dict does not have neither name of a book nor its api

    Returns:
        list: a list with the creators of the book

    >>> b1 = dict(api=1, author='Douglas Hofstadter', type='book', title='Gödel, Escher, Bach')
    >>> get_creators()
    ['Douglas Hofstadter']
    >>> from collections import OrderedDict
    >>> b2 = OrderedDict(api=2, type='book',
    ... title='Python in a Nutshell',
    ... authors='Martelli Ravenscroft Holden'.split())
    >>> get_creators()
    ['Martelli', 'Ravenscroft', 'Holden']
    >>> 
    """
    match record:
        case {'type': 'book', 'api': 2, 'authors': [*names]}:
            return names
        case {'type': 'book', 'api': 1, 'author': name}:
            return [name]
        case {'type': 'book'}:
            raise ValueError(f"Invalid 'book' record: {record!r}")
        case {'type': 'movie', 'director': name}:
            return [name]
        case _:
            raise ValueError(f'Invalid record: {record!r}')

if __name__ == "__main__":
    import doctest
    doctest.testmod()