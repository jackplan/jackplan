import numpy as np

class Shoe:
    cards = np.empty(0, dtype=np.int8)

    def __init__(self, deck_count):
        for deck_num in range(deck_count):
            self.cards = np.append(self.cards, range(8, 60))