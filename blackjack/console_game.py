from deck import Deck
from player import Player, Dealer

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
