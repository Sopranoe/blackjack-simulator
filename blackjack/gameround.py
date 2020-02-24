from deck import *
from player import *

class GameRound():
    def __init__(self, nr_players=1):
        self.game_deck = Deck()
        self.players = [Human('player' + str(i)) for i in range(nr_players)]
        self.dealer = Dealer()

    def deal_initial_card(self):
        for player in self.players:
            player.draw(self.game_deck.game_deck)
        self.dealer.draw(self.game_deck.game_deck) #open card
        self.dealer.draw(self.game_deck.game_deck) #hidden card

    def play(self, player):
        print(player.name + '\'s turn:')
        print("hand: " + '-'.join(player.hand) + ' - ' + str(player.points) + " points")
        while player.status == 'alive':
            action = player.get_action()
            if action == 'h': #hit
                player.draw(self.game_deck.game_deck)
            elif action == 's': #stand
                player.status = 'stand'
                print("Standing with " + str(player.points))
                #return player.status
        #return player.status

    def play_round(self):
        self.deal_initial_card()
        for player in self.players:
            self.play(player)
        if all(player.status == 'bust' for player in self.players):
           print("Dealer wins with " + '-'.join(self.dealer.hand) + ' - ' + str(self.dealer.points) + " points") 
        else:
            self.play(self.dealer)
        self.evaluate_winners()
    
    def evaluate_winners(self):
        for player in self.players:
            if player.status == 'stand':
                if self.dealer.status == 'stand':
                    if player.points > self.dealer.points:
                        player.status = 'win'
                    elif player.points == self.dealer.points:
                        player.status = 'draw'
                    else:
                        player.status = 'lose'
                elif self.dealer.status == 'bust':
                    player.status = 'win'
            #hprint(player.name + " - " + player.status)

#    def get_all_states(self):
#        return 
game_round = GameRound()

game_round.play_round()