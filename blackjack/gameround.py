from deck import *
from player import *

class GameRound():
    def __init__(self, players=[Human(), AiBasic()]):
        self.game_deck = Deck()
        self.players = players
        self.dealer = Dealer()

    def initialize_round(self):
        for player in self.players:
            player.bet = player.get_bet()
            print(f'{player.name} bets {player.bet}')
            player.draw(self.game_deck.game_deck)
        self.dealer.draw(self.game_deck.game_deck) #open card
        for player in self.players:
            player.draw(self.game_deck.game_deck)
        self.dealer.draw(self.game_deck.game_deck) #hidden card

    def play(self, player):
        print(f'{player.name}\'s hand: {"-".join(player.hand)} - {player.points} points')
        while player.status == 'alive':
            action = player.get_action()
            if action == 'h': #hit
                player.draw(self.game_deck.game_deck)
            elif action == 's': #stand
                player.status = 'stand'
                print(player.name + " standing with " + str(player.points))

    def play_round(self):
        self.initialize_round()
        for player in self.players:
            self.play(player)
        if all(player.status == 'bust' for player in self.players):
           print(f'Dealer win with {"-".join(self.dealer.hand)}\'s hand - {self.dealer.points} points')
        else:
            self.play(self.dealer)
        self.evaluate_winners()
        for player in self.players:
            print(f'{player.name}(${player.balance}): {player.status} with {str(player.points)} points')
    
    def evaluate_winners(self):
        for player in self.players:
            if player.status == 'stand':
                if self.dealer.status == 'stand':
                    if player.points > self.dealer.points:
                        player.status = 'win'
                    elif player.points == self.dealer.points:
                        player.status = 'push'
                    else:
                        player.status = 'lose'
                elif self.dealer.status == 'bust':
                    player.status = 'win'
                elif self.dealer.status == 'blackjack':
                    player.status = 'lose'
            elif player.status == 'bust':
                player.status = 'lose'
            if player.status == 'blackjack':
                if self.dealer.status != 'blackjack':
                    player.balance += 1.5*player.bet
                else:
                    player.status = 'push'
            if player.status == 'win':
                player.balance += player.bet
            if player.status == 'lose':
                player.balance -= player.bet

            player.bet = 0
                
game_round = GameRound()

game_round.play_round()