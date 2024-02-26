## -> Comment
class FlatSequencesMatching:
    def __init__(self, value):
        match tuple(value):
            case ['1', *rest]: print("A: ", rest)
            case ['2', *rest]: print("B: ", rest)
            case ['3' | '4', *rest]: print("C: ", rest)