from game import *
import settings as settings

def main():
    print(type(settings.HANGMAN))
    while True:
        game()
        if settings.guesses < len(settings.HANGMAN):
            print("You won good job")
        else:
            print("you lose")

        answer = input("Do you want to play again y/n")
        if answer.upper() == "y":
            pass
        else:
            break

main()