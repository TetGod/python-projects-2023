guesses = 0


HANGMAN = ("""
 ------
 |    |
 |
 |
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |   -+-
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |    |
 |   |
 |   |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |    |
 |   | |
 |   | |
 |
----------
"""
)
max_guess = len(HANGMAN)-1
WORDS = ["variable","Monty Python","Snake","function","Hello World","Print","Input","computer language","script","bool","def","if elif","error","pycharm","value","loops","randint"
    ,"len","tuple","attribute"]

# Tic Tac Toe Settings
MAX_Spots = 9
x = "X"
o = "O"
empty = " "

def display_menu(options,question):
    for i in range(len(options)):
        print(str.format("\t({0}.) ------------- {1:<30}",i+1,options[i]))
    while True:
        choice = getNumberInRange(question,1,len(options))
        return choice

def getNumberInRange(question, min, max):

    while True:
        x = input(question)
        try:
            x = int(x)
        except:
            print("not a number")
            continue
        if x >= min or x <= max:
            return x
        else:
            print("not in Range")

def game_quit():
    choice = display_menu(["Yes", "No"], "Are you sure you want to quit?")
    if choice == 1:
        print("Good by")
        input("Press Enter to Continue")
        quit()
    else:
        return