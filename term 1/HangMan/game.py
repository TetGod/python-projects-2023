import settings
import settings as settings
import random

def game_hangman():
    word = random.choice(settings.WORDS)
    so_far = "?"*len(word)
    used_letters = []

    print("Welcome to Hangman. Good Luck!")
    while settings.guesses < settings.max_guess and so_far != word:
        print(word)
        print("You have used the following letter")
        print(used_letters)
        print()
        print()

        print(settings.HANGMAN[settings.guesses])

        print("\nSo far, the word is:\n", so_far)


        guess = input("\n\nPick a letter: ").lower()
        while guess in used_letters:
            print("you have already guessed that letter")
            guess = input("\n\nPick a letter: ")
            if guess.isalpha():
                guess = guess.lower()
            else:
                continue

        used_letters.append(guess)

        if guess in word.lower():
            print("\nYes!", guess, "that is in the word!")
            new = ""
            for i in range(len(word)):
                if guess == word[i]:
                    new += guess
                else:
                    new += so_far[i]
            so_far = new

        else:
            print("\nSorry,", guess, "is not in the word.")
            settings.guesses += 1


# TicTacToe methods
def display_instructions():
    print("""
    Welcome to the greatest intellectual challenge of all time: Tic-Tac-Toe.
    This will be a showdown between your human brain and my silicon processor.
    """)
    print("""
    You will make your move known by entering a number 1 - 9. The number
    will correspond to the board position as illustrated:
    """)
    display_board([1,2,3,4,5,6,7,8,9])
    print("Prepare yourself, human. The ultimate battle is about to commence.")
    input ("Press enter to Begin")


def display_board(curboard):
    print(str.format("""
    \t{0} | {1} | {2}
    \t---------
    \t{3} | {4} | {5}
    \t---------
    \t{6} | {7} | {8}
    """,curboard[0],curboard[1],curboard[2],curboard[3],curboard[4],curboard[5],curboard[6],curboard[7],curboard[8]))

def new_board():
    board=[]
    for i in range(settings.MAX_Spots):
        board.append(settings.empty)

    return board

def rock_paper_scissors():
    while True:
        options = ["Rock","Paper","Scissors"]
        choice = settings.display_menu(options,"Choose?")
        player = options[choice-1]
        comp = random.choice(options)
        print("You",player)
        print("comp",comp)
        if (comp == options[0] and player == options[2]) or (comp == options[1] and player == options[0]) or \
                (comp == options[2] and player == options[1]):
            print("player Lost")
            return "Lose"
        elif comp == player:
            print("Tie")
            continue
        else:
            print("player Wins")
            return "Win"


def setPieces():
    win = rock_paper_scissors()
    if win == "win":
        human = settings.x
        comp = settings.o
    else:
        human = settings.o
        comp = settings.x
    return human,comp

def human_turn(board):
    legal = legal_moves(board)
    choice = -1
    while choice not in legal:
        choice = settings.getNumberInRange("What square would you like?",1,settings.MAX_Spots)-1
        if choice not in legal:
            print("\nThat square is already occupied, foolish human. Choose another.\n")

    return choice

def legal_moves(board):
    moves = []
    for i in range(settings.MAX_Spots):
        if board[i] == settings.empty:
            moves.append(i)
    return moves

def comp_Move(board,comp,human,diff):
    copy_of_board = board[:]
    legal = legal_moves(board)
    diff = diff
    if diff == "Easy":
        # easy
        choice = random.choice(legal)
        return choice
    elif diff == "Normal":
        if(comp == settings.x):
            best_moves_list = [4,0,3,6,8,1,3,5,7]
        else:
            best_moves_list = [1,3,5,7,4,0,2,6,8]
    elif diff == "Hard":
        if (comp == settings.x):
            best_moves_list = [5,3,2,8,7,1,6,0,5]
        else:
            best_moves_list = [5,2,6,5,4,0,3,1,7]
        # checking if comp can win
        for move in legal:
            copy_of_board[move] = comp
            if winner(copy_of_board) == comp:
                print("I shall take square number"+ str(move +1))
                return move
            copy_of_board[move]=settings.empty

        # if human can win
        for move in legal:
            copy_of_board[move] = human
            if winner(copy_of_board) == human:
                print("I shall take square number"+ str(move +1))
                return move

            copy_of_board[move]=settings.empty

        for move in best_moves_list:
            if move in legal:
                print("I shall take square number" + str(move + 1))
                return move

def diff_select():
    while True:
        options = ["Easy", "Normal", "Hard"]
        easy = "Easy"
        normal = "Normal"
        hard = "Hard"
        choice = settings.display_menu(options, "Choose?")
        if choice == 1:
            return easy
        elif choice == 2:
            return normal
        else:
            return hard

    return choice

def winner(board):
    winner = ""
    ways_to_win = [[0,1,2],[3,4,5],[6,7,8],[0,4,8],[2,4,6],[0,3,6],[1,4,7],[2,5,8]]
    for row in ways_to_win:
        if board[row[0]] == board[row[1]] == board [row[2]] != settings.empty:
            winner = board[row[0]]
            return winner
    if settings.empty not in board:
        return "Tie"
    return None

def compmove(board):
    # easy
    choice = 0
    legal = legal_moves(board)
    random.choice(legal)
    return choice

def next_turn(turn):
    if turn == settings.x:
        return settings.o
    else:
        return settings.x
def congrats(win,comp,human):
    if win != "Tie":
        print(win, "has Won")
    if win == comp:
        print("As i predicted human I am triumphant as always. \n"
              "this is proof that computers are the superior race")
    elif win == human:
        print("No no it cannot be h how did you actually do it. \n"
              "this wont happen again!")
    elif win == "Tie":
        print("You human are very lucky today as you were able to tie with such as i.  \n"
              "feel free to try again if you dare")
def game_TicTacToe():

    display_instructions()
    board = new_board()
    human, comp = setPieces()
    turn = settings.x
    display_board(board)
    diff = diff_select()
    while not winner(board):
        if turn == human:
            move = human_turn(board)
            board[move] = human
        else:
            move = comp_Move(board,comp,human,diff)
            board[move] = comp
        display_board(board)
        turn = next_turn(turn)