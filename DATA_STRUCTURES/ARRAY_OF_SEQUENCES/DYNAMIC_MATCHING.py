## -> Comment
class DynamicMatching:
    def __init__(self, a, b, c, *values):
        self.PAIRED_MATCHING = 1
        self.LEFT_MATCHING   = 2
        self.RIGHT_MATCHING   = 3
        self.packaged_values = (a, b, c, *values)
    def pair_matching(self, type):
        if type == self.PAIRED_MATCHING:
            a, b, c, *values = self.packaged_values
            print(a, b, c, values)
        elif type == self.LEFT_MATCHING:
            a, b, *values = self.packaged_values
            print(a, b, values)
        elif type == self.RIGHT_MATCHING:
            a, b, c, d, values = self.packaged_values
            print(a, b, c, d, values)