
#Models
from models.game import Game

#Utilities
import os

def run():
    """Main function"""

    title = """
    ********************************
    ***Welcome to the Trivia Game***
    ********************************   
    """

    menu = """
    Plese enter one of the following options...

    1. Start new game.
    2. Show score positions
    3. Delete score positions
    4. Exit
    
    """
    
    
    while True:
        print(title)
        print(menu)

        option = input("option: ")

        if option == '1':
            os.system("clear")
            Game.startGame()

        elif option == '2':
            os.system("clear")
            Game.showScore()

        elif option == '3':
            os.system("clear")
            Game.clearScore()

        elif option == '4':
            exit()

        else:
            print("Please enter a valid option.")


if __name__ == "__main__":
    run()


     