from deck import *
from player import *

class GameRound():
    def __init__(self, players=[Human(), AiBasic()]):
        self.game_deck = Deck()
        self.players = players
        self.dealer = Dealer()

    def deal_initial_cards(self):
        for player in self.players:
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
        self.deal_initial_cards()
        for player in self.players:
            self.play(player)
        if all(player.status == 'bust' for player in self.players):
           print(f'Dealer wins with {"-".join(self.dealer.hand)}\'s hand - {self.dealer.points} points')
        else:
            self.play(self.dealer)
        self.evaluate_winners()
        for player in self.players:
            print(f'{player.name}: {player.status} with {str(player.points)} points')
    
    def evaluate_winners(self):
        for player in self.players:
            if player.status == 'stand':
                if self.dealer.status == 'stand':
                    if player.points > self.dealer.points:
                        player.status = 'wins'
                    elif player.points == self.dealer.points:
                        player.status = 'draws'
                    else:
                        player.status = 'loses'
                elif self.dealer.status == 'bust':
                    player.status = 'wins'
            elif player.status == 'bust':
                player.status = 'loses'

game_round = GameRound()

game_round.play_round()