import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from blackjack.deck import Deck
from blackjack.player import Human, BotStatic
from blackjack.round import Round


def human_player_game():
    players = [Human(), BotStatic()]
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
    players = [BotStatic(100000, 15), BotStatic(100000, 16),
               BotStatic(100000, 17), BotStatic(100000, 18)]
    deck = Deck()
    run_game = True

    while run_game:
        round = Round(players, deck)
        round.play_round()
        game_history = {}
        if any(player.balance <= 0 for player in players):
            print("first player is out of money")
            print("____________________________")
            for player in players:
                game_history[player.name] = player.history
                print(player.name + ":")
                print(player.history)
                print("____________________________")
            visualize_results(game_history)
            run_game = False
        if len(deck.game_deck) < 0.5*deck.card_count:
            deck.reshuffle()


def visualize_results(results):
    sns.set(style="darkgrid")
    df = pd.DataFrame.from_dict(results)
    g = sns.relplot(kind="line", data=df)
    g.fig.autofmt_xdate()
    plt.show()


start_time = time.time()
simulate_game()
duration = time.time() - start_time
print(f'This game of blackjack took {duration} seconds.')

# human_player_game()
