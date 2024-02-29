def function_definition(*args : str) -> dict:
    """Multiple unpacking from multiple tuples
    Returns:
        dict: dictionary with multiple tuples unpacked
    >>> function_definition('define', ('name', 'par1', 'par2', 'par3'), 'body1', 'body2', 'body3')
    ('name', (['par1', 'par2', 'par3'], ['body1', 'body2', 'body3']))
    >>> ## An example with trailing comma to avoid write more cases
    >>> function_definition('define', ('name', ), 'body1', 'body2', 'body3')
    ('name', ([], ['body1', 'body2', 'body3']))
    >>> ## An example with two trailing commans making another case where body is empty
    >>> function_definition('define', ('name', ), )
    ('name', ([], []))
    """

    match args:
        ## for an not empty body
        case ['define', [name, *params], *body] if body:
            return (name, (params, body))
        ## for an empty body
        case ['define', [name, *params], *body]:
            return (name, (params, body))

if __name__ == "__main__":
    import doctest
    doctest.testmod()