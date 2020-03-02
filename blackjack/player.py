class Player:
    def __init__(self, name, balance):
        self.name = name
        self.hand = []
        self.points = 0
        self.ace = False
        self.ten = False
        self.status = 'alive'  # 'alive', 'bust', 'stand', 'blackjack', 'win', 'push', 'lose'
        self.balance = balance
        self.bet = 0
        self.history = {'balance': [balance], 'points': [0],  # depending on use case, it
                        'hand': [''], 'status': ['']}  # might be better to initialize all as empty lists
        #self.history = pd.DataFrame(columns=['balance', 'points', 'hand', 'status'])

    # def __str__():

    def update_points(self):
        return self.calculate_points()

    def calculate_points(self):
        values = {"A": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7,
                  "8": 8, "9": 9, "T": 10, "J": 10, "Q": 10, "K": 10}
        hand_values = []
        card_ranks = [rank[0] for rank in self.hand]

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
        print(f'{self.name} received {self.hand[-1]}')

    def get_action(self):
        pass

    def get_bet(self):
        return 100

    def save_result(self):
        self.history["balance"].append(self.balance)
        self.history["points"].append(self.points)
        self.history["hand"].append(self.hand)
        self.history["status"].append(self.status)


class Dealer(Player):
    def __init__(self):
        super().__init__('dealer', 0)

    def get_action(self):
        if self.points < 17:
            return "h"
        else:
            return "s"

    def get_upcard(self):
        return self.hand[0]


class Human(Player):
    def __init__(self, name='human', balance=1000):
        super().__init__(name, balance)

    def get_action(self):
        return input("Would you like to hit (h) or stand (s): ")

    def get_bet(self):
        while True:
            bet = int(input("How much would you like to bet: "))
            if bet > 0 and bet <= self.balance:
                return bet


class AiBasic(Player):
    def __init__(self, balance=1000):
        super().__init__('AiBasic', balance)

    def get_action(self):
        if self.points < 17:
            return "h"
        else:
            return "s"
