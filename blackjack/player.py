from .hand import Hand


class Player:
    def __init__(self, name, balance):
        self.name = name
        self.hands = []
        self.balance = balance
        self.history = {'balance': [balance], 'points': [[0]],
                        'hands': [['']], 'statuses': [['start']]}

    # def __str__():

    def get_action(self, hand_number):
        pass

    def get_bet(self):
        return 100

    def save_result(self):
        self.history["balance"].append(self.balance)
        # better list comprehension?
        for i in range(len(self.hands)):
            self.history["points"][i].append(self.hands[i].points)
            self.history["hands"][i].append(self.hands[i].cards)
            self.history["statuses"][i].append(self.hands[i].status)

    def reset_hands(self):
        self.hands = [Hand()]


class Dealer(Player):
    def __init__(self):
        super().__init__('dealer', 0)

    def get_action(self, hand_number=0):
        if self.hands[hand_number].points < 17:
            return "h"
        else:
            return "s"

    def get_upcard(self):
        return self.hands[0][0]


class Human(Player):
    def __init__(self, name='human', balance=1000):
        super().__init__(name, balance)

    def get_action(self, hand_number):
        return input("Would you like to hit (h),"
                     "stand (s) or double down (d): ")

    def get_bet(self):
        while True:
            bet = int(input("How much would you like to bet: "))
            if bet > 0 and bet <= self.balance:
                return bet


class AiBasic(Player):
    def __init__(self, balance=1000):
        super().__init__('AiBasic', balance)

    def get_action(self, hand_number):
        hand = self.hands[hand_number]        
        if hand.points in (9, 10, 11) and len(hand.cards) == 2:
            return "d"
        elif hand.points < 17:
            return "h"
        else:
            return "s"
