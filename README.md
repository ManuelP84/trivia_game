# trivia_game

## Table of Contents
1. [General Info](#general-info)
2. [Technologies](#technologies)

### General Info
***
This is a multiple choice trivia game. It consists of 5 levels of difficulty where questions are asked in the categories of:

* General Culture
* Arts
* Sports
* Science
* Geography.

There is a scale of prizes which are awarded as follows:
Level 1. 100 USD
Level 2. 300 USD
Level 3. 600 USD
Level 4. 1000 USD
Level 5. 2000 USD

The player can leave the game at any time. The money he will take is the amount of money corresponding to the completed levels. Similarly, if a question is answered incorrectly, the game is over.

At the start of each game the program will ask for an alias in order to register the game. This information will be stored in a sqlite3 database.

The user can delete the registered information of the games.

The program menu is as follows:

1. Start new game.
2. Show score positions
3. Delete score positions
4. Exit

The user can store more questions or replace them by means of the .txt files inside the folder "questions" following the same format. Questions must be separated by "-".

A sqlite3 database is used to store the games.

## Technologies
***
* [Python](https://www.python.org/): Version 3.8.10 