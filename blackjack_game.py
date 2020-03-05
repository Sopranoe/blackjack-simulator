from blackjack.deck import Deck
from blackjack.player import Human, AiBasic
from blackjack.round import Round


players = [Human(), AiBasic()]
deck = Deck()
run_game = True

while run_game:
    round = Round(players, deck)
    round.play_round()
    quit = input('Do you want to quit? (y/n): ')
    if quit == 'y':
        print("Thanks for playing!")
        print(players[0].history)
        run_game = False
    if players[0].balance <= 0:
        print("first player is out of money")
        run_game = False
    if len(deck.game_deck) < 0.5*deck.card_count:
        deck.reshuffle()
