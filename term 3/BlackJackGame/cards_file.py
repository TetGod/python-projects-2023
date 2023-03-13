

class Base_Card():
    RANKS = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    SUITS = ["♠","♣","♥","♦"]

    def __init__(self,rank,suit):
        """Constructor this is called to Build an object from this class"""

        self.isFacedUp = False
        self.rank = rank
        self.suit = suit

    def __str__(self):
        """returns a string rep of the object when printed """
        ret = ""
        if self.isFacedUp:
            ret = str.format("""
                    _____________
                   | {0:2}{1}        |
                   |             |
                   |             |
                   |             |
                   |        {1}{0:2} |
                    _____________
            """,self.rank, self.suit)
        else:
            ret = """
                    _____________
                   |*************|
                   |*************|
                   |*************|
                   |*************|
                   |*************|
                    _____________
                                """

        return ret


    def flip(self):
        """toggles the isFacedUp bool"""
        self.isFacedUp = not self.isFacedUp

    @property
    def value(self):
        if self.isFacedUp:
            return Base_Card.RANKS.index(self.rank)+1
        else:
            return 0

class BlackJack_Card(Base_Card):
    ACE_VALUE = 1

    @property
    def value(self):
        if self.isFacedUp:
            val = BlackJack_Card.RANKS.index(self.rank)+1
            if val > 10:
                val = 10
        else:
            val = None

        return val



if __name__ == "__main__":
    print("this is not a program try importing and using the classes")
    input("\n\nPress the enter key to exit.")
