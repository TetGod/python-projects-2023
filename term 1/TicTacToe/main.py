def getNumberInRange(question,min,max):
    while True:
        x = input(question)
        try:
            x = int(x)
        except:
            print("not a number")
            continue
        if x >= min and x <= max:
            return x
        else:
            print("not in Range")

def display_menu(options,question):
    print(RIBBON)
    print(question)
    for i in range(len(options)):
        print(str.format("\t({0}.) ------------- {1:<30}",i+1,options[i]))
    print(RIBBON)
    while True:
        choice = input("What would you like to do? ")
        if choice.isnumeric():
            choice = int(choice)
            if choice <= len(options) and choice > 0:
                return choice
            else:
                print("not in the correct Range")
        else:

            def game_quit():
                clear_screen()
                choice = display_menu(["Yes", "No"], "Are you sure you want to quit?")
                if choice == 1:
                    print("Good by")
                    input("Press Enter to Continue")
                    quit()
                else:
                    return