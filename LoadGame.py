from game import game

load_game = True
while load_game:
    startgame = game()
    startgame.start_game()
    print()
    yesorno = input("Do you want to play again? (y/n) ")
    if yesorno == "n":
        load_game = False
        print("Thanks for playing!")