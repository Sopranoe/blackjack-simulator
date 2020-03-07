import time
from blackjack.deck import Deck
from blackjack.player import Human, AiBasic
from blackjack.round import Round


def human_player_game():
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


def simulate_game():
    players = [AiBasic(500, 15), AiBasic(500, 16),
               AiBasic(500, 17), AiBasic(500, 18)]
    deck = Deck()
    run_game = True

    while run_game:
        round = Round(players, deck)
        round.play_round()
        if any(player.balance <= 0 for player in players):
            print("first player is out of money")
            print("____________________________")
            for player in players:
                print(player.name + ":")
                print(player.history)
                print("____________________________")
            run_game = False
        if len(deck.game_deck) < 0.5*deck.card_count:
            deck.reshuffle()


start_time = time.time()
simulate_game()
duration = time.time() - start_time
print(f'This game of blackjack took {duration} seconds.')

# human_player_game()
