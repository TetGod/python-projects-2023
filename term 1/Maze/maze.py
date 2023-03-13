# Landon Bowcutt
# 10/6/2022
# Oregon Trail

import requests
import random

#gloal variables
option1 = 1


#functions
def gameloop(story, question,options1,options2,insults):
    while True:
        print("Welcome to the Dorgon")
        print("It appears you have been trapped inside some small dark space")
        print("what direction would you like to go in")
        while True:
            choice = input(question)
            if (choice in options1):
                story = "options1"
                break
            elif choice in options2:
                story = "option 2"
                break

            else:
                print(random.choice(insults))

        if (option1 = True):
            print Living Room



gameloop("starting","give me an input",[1,"one","yes"],[2,"two","no"],["you suck at this game","go touch some grass","Really ???"])