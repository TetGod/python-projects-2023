from game import *
import settings as settings

def main():
    while True:
        choice = settings.display_menu(["Play Tic Tac Toe","Play Hang Man","Rock Paper Scissors","Quit"],"What would you like to do")

        print(choice)
        if choice == 1:
            game_TicTacToe()
        elif choice == 2:
            game_hangman()
            if settings.guesses < len(settings.HANGMAN):
                print("You won good job")
            else:
                print("you lose")
        elif choice == 3:
            rock_paper_scissors()
        else:
            settings.game_quit()


main()