class Hand:
    def __init__(self, cards=None, bet=0):
        self.status = 'alive'  # 'alive', 'bust', 'stand', 'blackjack', 'win', 'push', 'lose'
        self.bet = bet
        self.points = 0
        self.ace = False
        self.ten = False
        if cards is None:
            self.cards = []
        else:
            self.cards = cards
            self.update_points()
            self.update_status()

    def update_points(self):
        values = {"A": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7,
                  "8": 8, "9": 9, "T": 10, "J": 10, "Q": 10, "K": 10}
        hand_values = []
        card_ranks = [rank[0] for rank in self.cards]

        for rank in card_ranks:
            val = values.get(rank)
            if val == 1:
                self.ace = True
            elif val == 10:
                self.ten = True
            hand_values.append(val)

        self.points = sum(hand_values)
        if self.points <= 11 and self.ace:
            self.points = self.points + 10

    def update_status(self):
        if self.points == 21:
            if len(self.cards) == 2:
                self.status = 'blackjack'
            else:
                self.status = 'stand'
        elif self.points > 21:
            self.status = 'bust'

    def draw(self, deck, nr_cards=1):
        for i in range(nr_cards):
            self.cards.append(deck.pop())
        self.update_points()
        self.update_status()
