# Landon Bowcutt
# 10/6/2022
# Oregon Trail

import requests
import random

#gloal variables
option1 = 1

def insult():
    insults = ["you suck at this game","go touch some grass","Really ???"]
    print(random.choice(insults))
#functions
def room1():
    while True:
        print("art")
        print("Welcome to the Dungeon")
        print("It appears you have been trapped inside a dimly lit space")
        print("what would you like to do")
        choice = input("Give me an input")
        if (choice == "open door"):
            room2()
            break
        elif choice =="look around":
            print("there is a door in front of you a carpet under you and lots of dust and bones")
            notextroom1()
            break
        elif choice =="check under carpet":
            print("nothing here except more dust of course")
            notextroom1()
            break
        elif choice == "3":
            pass
        else:
            insult()

def notextroom1():
    while True:
        print("what would you like to do")
        choice = input("Give me an input")
        if (choice == "open door"):
            room2()
            break
        elif choice == "look around":
            print("there is a door in front of you a carpet under you and lots of dust and bones")
            notextroom1()
            break
        elif choice == "check under carpet":
            print("nothing here except more dust of course")
            break
        elif choice == "3":
            pass
        else:
            insult()

def room2():
    while True:
        print("art")
        print("You are now in a dark hallway")
        print("would you like to go left or right")
        print("what would you like to do")
        choice = input("Give me an input")
        if (choice == "left"):
            room3()
            break
        elif choice =="right":
            room4()
            break
        elif choice == "go back":
            room1()
            break
        elif choice == "up":
            pass
        else:
            insult()

def room3():
    while True:
        print("art")
        print("")
        print("You see i tiny sliver of light and a doorway")
        print("what would you like to do")
        choice = input("Give me an input")
        if (choice == "1"):
            room2()
            break
        elif choice =="2":
            room3()
            break
        elif choice == "3":
            pass
        else:
            insult()

def room4():
    while True:
        print("art")
        print("you are still in the hallway however it is darker")
        print("would you like to go left or right")
        print("what would you like to do")
        choice = input("Give me an input")
        if (choice == "1"):
            room2()
            break
        elif choice =="2":
            room3()
            break
        elif choice == "3":
            pass
        else:
            insult()
def room5():
    while True:
        print("art")
        print("you are still in the hallway however it is darker")
        print("would you like to go left or right")
        print("what would you like to do")
        choice = input("Give me an input")
        if (choice == "1"):
            room2()
            break
        elif choice =="2":
            room3()
            break
        elif choice == "3":
            pass
        else:
            insult()
def room6():
    while True:
        print("art")
        print("you are still in the hallway however it is darker")
        print("would you like to go left or right")
        print("what would you like to do")
        choice = input("Give me an input")
        if (choice == "1"):
            room2()
            break
        elif choice =="2":
            room3()
            break
        elif choice == "3":
            pass
        else:
            insult()
def room7():
    while True:
        print("art")
        print("you are still in the hallway however it is darker")
        print("would you like to go left or right")
        print("what would you like to do")
        choice = input("Give me an input")
        if (choice == "1"):
            room2()
            break
        elif choice =="2":
            room3()
            break
        elif choice == "3":
            pass
        else:
            insult()
def room8():
    while True:
        print("art")
        print("you are still in the hallway however it is darker")
        print("would you like to go left or right")
        print("what would you like to do")
        choice = input("Give me an input")
        if (choice == "1"):
            room2()
            break
        elif choice =="2":
            room3()
            break
        elif choice == "3":
            pass
        else:
            insult()
def room9():
    while True:
        print("art")
        print("you are still in the hallway however it is darker")
        print("would you like to go left or right")
        print("what would you like to do")
        choice = input("Give me an input")
        if (choice == "1"):
            room2()
            break
        elif choice =="2":
            room3()
            break
        elif choice == "3":
            pass
        else:
            insult()
def room10():
    while True:
        print("art")
        print("you are still in the hallway however it is darker")
        print("would you like to go left or right")
        print("what would you like to do")
        choice = input("Give me an input")
        if (choice == "1"):
            room2()
            break
        elif choice =="2":
            room3()
            break
        elif choice == "3":
            pass
        else:
            insult()
room1()