from deck import Deck
from player import Player, Dealer

class GameRound():
    def __init__(self, nr_players=1):
        self.game_deck = Deck()
        self.players = [Player('player' + str(i)) for i in range(nr_players)]
        self.dealer = Dealer()

    def deal_initial_card(self):
        for player in self.players:
            player.draw(self.game_deck.game_deck)
        self.dealer.draw(self.game_deck.game_deck) #open card
        self.dealer.draw(self.game_deck.game_deck) #hidden card

    def play(self, player):
        print(player.name + '\'s turn:')
        print('hand: ' + player.hand[0])
        while player.status == 'alive':
            action = input("Would you like to hit (h) or stand (s)")
            if action == 'h': #hit
                player.draw(self.game_deck.game_deck)
                print("hand: " + '-'.join(player.hand) + ' : ' + str(player.points) + ' points')
            elif action == 's': #stand
                player.status == 'stand'
                print("You decided to stand")
                return player.status
        return player.status

    def play_round(self):
        self.deal_initial_card()
        for player in self.players:
            self.play(player)
        self.play(self.dealer)
            

game_round = GameRound(4)

game_round.play_round()
