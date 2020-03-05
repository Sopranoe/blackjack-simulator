from .player import Dealer


class Round():
    def __init__(self, players, deck):
        self.game_deck = deck
        self.players = players
        self.dealer = Dealer()
        self.players_alive = len(self.players)

    def initialize_round(self):
        self.players_alive = len(self.players)
        for player in self.players:
            player.reset_hands()
            player.hands[0].bet = player.get_bet()
            print(f'{player.name} bets {player.hands[0].bet}')
            player.hands[0].draw(self.game_deck.game_deck, 2)
        self.dealer.reset_hands()
        self.dealer.hands[0].draw(self.game_deck.game_deck, 2)  # open card

    def play_hand(self, player):
        print(f'_____{player.name}\'s turn_____')
        for hand_number, hand in enumerate(player.hands):
            print(f'hand({hand_number + 1}): {"-".join(hand.cards)} '
                  f'- {hand.points} points')
            while hand.status == 'alive':
                print(f'{player.name}, hand({hand_number + 1}): '
                      f'{"-".join(hand.cards)} - {str(hand.points)} points')
                action = player.get_action(hand_number)
                if action == 'h':  # hit
                    hand.draw(self.game_deck.game_deck)
                elif action == 's':  # stand
                    hand.status = 'stand'
                    print(f'{player.name} standing on hand {hand_number + 1} '
                          f'with {str(hand.points)} points')
                elif action == 'd':  # double down
                    if len(hand.cards) == 2 and player.balance >= 2*hand.bet:
                        hand.bet *= 2
                        hand.status = 'stand'
                        hand.draw(self.game_deck.game_deck)
                        print(f'{player.name} {hand.status} after double on hand'
                              f'({hand_number + 1}) with {"-".join(hand.cards)} - '
                              f'{str(hand.points)} points')
                    elif len(hand.cards) > 2:
                        print("Double down not possible with more than 2 cards")
                    elif player.balance < 2*hand.bet:
                        print("Not enough money to double down.")
                elif action == 'x':  # split
                    if (len(hand.cards) == 2 and player.balance >= 2*hand.bet and hand.cards[0][0] == hand.cards[1][0]):
                        player.split(hand_number)
                        hand.draw(self.game_deck.game_deck)
                        print(f'{player.name} {hand.status} after double on hand'
                              f'({hand_number + 1}) with {"-".join(hand.cards)} - '
                              f'{str(hand.points)} points')
                    elif player.balance < 2*hand.bet:
                        print("Not enough money to split.")
                    elif player.balance < 2*hand.bet:
                        print("Splitting not possible.")
                    
        if all(hand.status == 'bust' for hand in player.hands):
            self.players_alive -= 1

    def play_round(self):
        self.initialize_round()
        for player in self.players:
            self.play_hand(player)
        if self.players_alive <= 0:
            print(f'Dealer win with {"-".join(self.dealer.hands[0].cards)}\'s '
                  f'hand - {self.dealer.points} points')
        else:
            self.play_hand(self.dealer)
        self.evaluate_winners()
        print("_____results______")
        for player in self.players:
            for hand in player.hands:
                print(f'{player.name}(${player.balance}): {hand.status} '
                      f'${hand.bet} with {str(hand.points)} points'
                      f' ({"-".join(hand.cards)})')
                hand.bet = 0
            player.save_result()
        self.dealer.save_result()  # not really needed

    def evaluate_winners(self):
        for player in self.players:
            for hand in player.hands:
                if hand.status == 'stand':
                    if self.dealer.hands[0].status == 'stand':
                        if hand.points > self.dealer.hands[0].points:
                            hand.status = 'win'
                        elif hand.points == self.dealer.hands[0].points:
                            hand.status = 'push'
                        else:
                            hand.status = 'lose'
                    elif self.dealer.hands[0].status == 'bust':
                        hand.status = 'win'
                    elif self.dealer.hands[0].status == 'blackjack':
                        hand.status = 'lose'
                elif hand.status == 'bust':
                    hand.status = 'lose'
                if hand.status == 'blackjack':
                    if self.dealer.hands[0].status != 'blackjack':
                        player.balance += 1.5*hand.bet
                    else:
                        hand.status = 'push'
                if hand.status == 'win':
                    player.balance += hand.bet
                if hand.status == 'lose':
                    player.balance -= hand.bet
