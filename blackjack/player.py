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
        self.history["points"].append([])
        self.history["hands"].append([])
        self.history["statuses"].append([])
        # better list comprehension?
        for i in range(len(self.hands)):
            self.history["points"][-1].append(self.hands[i].points)
            self.history["hands"][-1].append(self.hands[i].cards)
            self.history["statuses"][-1].append(self.hands[i].status)

    def reset_hands(self):
        self.hands = [Hand()]

    def split(self, hand_number):
        original_hand = self.hands[hand_number].cards
        original_bet = self.hands[hand_number].bet
        self.hands.append(Hand([original_hand[1]], original_bet))
        self.hands[hand_number].cards = [original_hand[0]]


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
        return input("Would you like to hit (h), double down (d) "
                     "split (x) or stand (s) ")

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
