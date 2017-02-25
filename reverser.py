class Reverser:
    def __init__(self):
        self.str = ""

    def reverse(self, str_val):
        self.str = str_val
        return self.str[::-1]
