
#Models
from models.player import Player
from models.array import Array

#Database connection
from dbConnection import createDb, createTable, insertScore, readScores, deleteScores

#Utilities
import random
import os

ROOT_LEVEL1 = "./questions/questions_level1.txt"
ROOT_LEVEL2 = "./questions/questions_level2.txt"
ROOT_LEVEL3 = "./questions/questions_level3.txt"
ROOT_LEVEL4 = "./questions/questions_level4.txt"
ROOT_LEVEL5 = "./questions/questions_level5.txt"
TOTAL_LEVELS = 5


class Game:
    """Game class. Include all the static methods for the game execution."""      
    
    @staticmethod
    def loadData(root):
        """Loads the data questions from the txt files to an array object."""
        
        questions_level1 = []
        question = {}
        obj = Array()

        with open(root, "r", encoding = "utf-8") as file:
            
            for line in file:
                if line.strip() != "-":
                    questions_level1.append(line.strip("\n"))
                else:
                    question = {
                        'category':questions_level1[0],
                        'level': questions_level1[1],
                        'question': questions_level1[2],
                        'a': questions_level1[3],
                        'b': questions_level1[4],
                        'c': questions_level1[5],
                        'd': questions_level1[6],
                        'answer': questions_level1[7]
                    }       
                                
                    obj.pushitem(question)
                    questions_level1.clear()
        return obj

    @staticmethod
    def requestAnswer():
        """Request an answer from the player."""    

        option_list = ['a', 'b', 'c', 'd', 'e']
        
        while True:
            option = input("Please enter the answer: ").strip().casefold()
            if option not in option_list:
                print("Please enter a valid option")
            else:
                return option

    @staticmethod
    def showQuestion(questions, index):
        """Present the question and the options to the user."""

        question = f"""
        {questions.__getitem__(index)['question']}
            a. {questions.__getitem__(index)['a']}
            b. {questions.__getitem__(index)['b']}
            c. {questions.__getitem__(index)['c']}
            d. {questions.__getitem__(index)['d']}

            e. Exit the game.
            Note: up to this point you will only earn the accumulated prize money from the previous levels.
        
        """
        print(question)

    @staticmethod
    def validateLevel(questions, level, price):
        """Validate a level. Returns True if the player passes all the questions."""

        nr_aserts = 0

        message = f"""
        Welcome to level  #{level}!!!
        If you pass the level you will get {price} USD.
        Good Luck!!
        """
        print(message)

        while(questions.__len__()>0):
            
            question_nr = random.randint(0, questions.__len__()-1)
            Game.showQuestion(questions, question_nr)        
            option = Game.requestAnswer()
            answer = questions.__getitem__(question_nr)['answer']
            questions.popitem(question_nr)
        
            if option == answer:
                print("Correct!!!")
                input()
                os.system("clear") 
                nr_aserts += 1
            elif option == 'e':
                print("Unfortunately you are leaving the game...")
                input()
                return False
            else:
                print("Inorrect!!!")
                input() 
                os.system("clear") 
                return False         
                
        if nr_aserts == 5:
            print("Congratulations!!!")
            return True
        else:
            return False
            
    @staticmethod
    def calculatePrice(new_player, passed_level, level):
        """Calculate the accumulated prize."""

        if passed_level is True:
            print("Passed to the next level!!")
            if level == 1:
                print("You got 100 USD")
                new_player.set_price(100)
            elif level == 2:
                print("You got 300 USD more")
                new_player.set_price(300)
            elif level == 3:
                print("You got 600 USD more")
                new_player.set_price(600)
            elif level == 4:
                print("You got 1000 USD more")
                new_player.set_price(1000)
            elif level == 5:
                print("You WON the game and got 2000 USD more.")
                new_player.set_price(2000)

        else:
            final_message = f"""
            Hi {new_player.get_alias()}
            It's the end of the game....
            You got {new_player.get_price()} USD
            You can do it better next time!
            See you soon...            
            """
            print(final_message)

    @staticmethod
    def startGame():
        """Start a new game."""

        passed_level = True

        new_player_alias = input("Please enter the alias to start the game: ")

        new_player = Player(new_player_alias)

        createDb()
        createTable()              

        for level in range(1, TOTAL_LEVELS +1):
            if level == 1:
                questions_level = Game.loadData(ROOT_LEVEL1)
                passed_level = Game.validateLevel(questions_level, str(level), '100') 
                Game.calculatePrice(new_player, passed_level, level)

            elif level == 2 and passed_level == True:
                questions_level = Game.loadData(ROOT_LEVEL2)
                passed_level = Game.validateLevel(questions_level, str(level), '300') 
                Game.calculatePrice(new_player, passed_level, level)
            
            elif level == 3 and passed_level == True:
                questions_level = Game.loadData(ROOT_LEVEL3)
                passed_level = Game.validateLevel(questions_level, str(level), '600') 
                Game.calculatePrice(new_player, passed_level, level)

            elif level == 4 and passed_level == True:
                questions_level = Game.loadData(ROOT_LEVEL4)
                passed_level = Game.validateLevel(questions_level, str(level), '1000') 
                Game.calculatePrice(new_player, passed_level, level)

            elif level == 5 and passed_level == True:
                questions_level = Game.loadData(ROOT_LEVEL4)
                passed_level = Game.validateLevel(questions_level, str(level), '2000') 
                Game.calculatePrice(new_player, passed_level, level)
        
        insertScore(new_player_alias, new_player.get_price())

    @staticmethod
    def showScore():
        """Show the score history."""
        
        data = readScores()
        for i in range(len(data)):
            print(f"{i+1}. {data[i][0]}  -  {data[i][1]} USD") 

    @staticmethod
    def clearScore():
        """Show the score history."""

        deleteScores()