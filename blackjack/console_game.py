# import deck
# import player
### imports currently not working with my windows setup, so for now everything in one file

from random import shuffle

class Deck:
    single_deck = ["Ac", "Ac", "Ac", "4c", "5c", "6c", "7c", "8c", "9c", "Tc", "Jc", "Qc", "Kc",
            "Ad", "2d", "3d", "4d", "5d", "6d", "7d", "8d", "9d", "Td", "Jd", "Qd", "Kd",
            "Ah", "2h", "3h", "4h", "5h", "6h", "7h", "8h", "9h", "Th", "Jh", "Qh", "Kh",
            "As", "2s", "3s", "4s", "5s", "6s", "7s", "8s", "9s", "Ts", "Js", "Qs", "Ks"]
    
    def __init__(self, deck_count=4):
        self.game_deck = self.single_deck*deck_count
        shuffle(self.game_deck)

    def reshuffle(self, deck_count=4):
        self.game_deck = self.single_deck*deck_count
        shuffle(self.game_deck)

class Player:
    variable = "blah"
    def __init__(self):
        self.hand = []
        self.points = 0
        self.ace = False
        self.ten = False
        self.status = 'alive' # 'alive', 'bust', 'stand', 'blackjack' 

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

        if self.ace and self.points <= 141:
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
        print("The deck has been shuffled. You receive a " + '-'.join(self.hand))
        print("That's " + str(self.points))
        self.update_status()

class Dealer(Player):
    def __init__(self):
        super().__init__()
        self.upcard = ''
    
    def update_points(self):
        self.upcard = self.hand[0]
        return self.calculate_points()

deck = Deck()
player1 = Player()
dealer = Dealer()

deck_count = input("Welcome to Blackjack. How many decks should we use?")
game_deck = Deck(int(deck_count))
player1.draw(game_deck.game_deck)
dealer.draw(game_deck.game_deck)
while player1.points < 21:  
    action = input("Would you like to hit (h) or stand (s)")
    if action == 'h':
        player1.draw(game_deck.game_deck)
    elif action == 's':
        break
    else:
        print("Wrong key entered.")
if player1.points == 21:
    print("21 points!")
elif player1.points > 21:
    print("you busted with " + '-'.join(player1.hand) + " and " + str(player1.points) + " points")
else:
    print("You stand with " + '-'.join(player1.hand) + " and " + str(player1.points) + " points")

print("Dealer's Turn")
