from .hand import Hand


class Player:
    def __init__(self, name, balance, bet_size=100, bet_strat='fixed'):
        self.name = name
        self.hands = []
        self.balance = balance
        self.history = [balance]
        self.bet_strat = bet_strat
        self.bet_size = bet_size

    # def __str__():

    def get_action(self, hand_number):
        pass

    def fixed_bet(self):
        return self.bet_size

    def get_bet(self):
        # return 100
        bet_strategies = {'fixed': self.fixed_bet}
        return bet_strategies[self.bet_strat]()

    def save_result(self):
        self.history.append(self.balance)

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
    nr_humans = 0

    def __init__(self, name=None, balance=1000):
        Human.nr_humans += 1
        if name is None:
            name = f'human_{Human.nr_humans}'
        super().__init__(name, balance)

    def get_action(self, hand_number):
        return input("Would you like to hit (h), double down (d) "
                     "split (x) or stand (s) ")

    def get_bet(self):
        while True:
            bet = float(input("How much would you like to bet: "))
            if bet > 0 and bet <= self.balance:
                return bet


class BotStatic(Player):
    nr_bot_statics = 0

    def __init__(self, balance=1000, stand_with=17,
                 bet_size=100, bet_strat='fixed'):
        BotStatic.nr_bot_statics += 1
        name = f'BotStatic_{str(BotStatic.nr_bot_statics)} (sw{str(stand_with)})'
        super().__init__(name, balance, bet_size, bet_strat)
        self.stand_with = stand_with

    def get_action(self, hand_number):
        hand = self.hands[hand_number]
        if (hand.points in (9, 10, 11)
                and len(hand.cards) == 2
                and self.balance > 2*hand.bet):
            return "d"
        elif hand.points < self.stand_with:
            return "h"
        else:
            return "s"
