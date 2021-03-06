from random import shuffle


class Deck:
    single_deck = [
        "Ac", "2c", "3c", "4c", "5c", "6c", "7c", "8c", "9c", "Tc", "Jc", "Qc", "Kc",
        "Ad", "2d", "3d", "4d", "5d", "6d", "7d", "8d", "9d", "Td", "Jd", "Qd", "Kd",
        "Ah", "2h", "3h", "4h", "5h", "6h", "7h", "8h", "9h", "Th", "Jh", "Qh", "Kh",
        "As", "2s", "3s", "4s", "5s", "6s", "7s", "8s", "9s", "Ts", "Js", "Qs", "Ks"
        ]

    def __init__(self, deck_count=4):
        self.game_deck = self.single_deck*deck_count
        self.card_count = deck_count*52
        shuffle(self.game_deck)

    def reshuffle(self, deck_count=4):
        self.game_deck = self.single_deck*deck_count
        shuffle(self.game_deck)
