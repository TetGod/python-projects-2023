import BlackJack_Classes
from cards_file import *
from player_file import *
from CommonGameFunction import *
import random





def main():
    print("\t\tWelcome to BlackJack!\n")
    names = []
    num = ask_number("how many player are playing (1 - 7)",low=1,high=8)
    for i in range(num):
        name = input("Player" + str(i+1) + "Enter your name(s)")
        names.append(name)

    game = BlackJack_Classes.BlackJack_Game(names)
    play = None
    while play != "n":
        game.play()
        play = ask_yes_no("\ndo you want to play again?:")

main()