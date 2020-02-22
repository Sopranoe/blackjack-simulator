class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.points = 0
        self.ace = False
        self.ten = False
        self.status = 'alive' # 'alive', 'bust', 'stand', 'blackjack', 'win', 'draw', 'lose'

    def update_points(self):
        return self.calculate_points()

    def calculate_points(self):
        values = {"A": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, 
                    "9": 9, "T": 10, "J": 10, "Q": 10, "K": 10} # A = 1 or 11
        hand_values = []
        card_ranks = [rank[0] for rank in self.hand]

        for rank in card_ranks:
            val = values.get(rank)
            if val==1:
                self.ace = True
            elif val==10:
                self.ten = True
            hand_values.append(val)
        
        self.points = sum(hand_values)
        if self.points <= 11 and self.ace:
            self.points = self.points + 10

    def update_status(self):
        if self.points == 21:
            if len(self.hand) == 2:
                self.status = 'blackjack'
            else: 
                self.status = 'stand'
        elif self.points > 21:
            self.status = 'bust'
        else:
            self.status = 'alive'

    def draw(self, deck):
        self.hand.append(deck.pop())
        self.update_points()
        self.update_status()
        print("hand: " + '-'.join(self.hand) + ' : ' + str(self.points) + ' points')

    def get_action(self):
        return input("Would you like to hit (h) or stand (s)")

class Dealer(Player):
    def __init__(self):
        super().__init__('dealer')
    
    def get_action(self):
        if self.points < 17:
            return "h"
        else:
            return "s"

    def get_upcard(self):
        return self.hand[0]

class Human(Player):
    pass

class AiBasic(Player):
    pass