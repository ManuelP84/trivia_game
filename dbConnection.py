import sqlite3

ROOT_DATABASE = "./database/scoreDb.db"

def createDb():
    """Create a data base for the player history."""

    try:
        score_connection = sqlite3.connect(ROOT_DATABASE) 
        score_connection.commit()
        score_connection.close()

    except Exception as ex:
        print(ex)


def createTable():
    """Create the table player."""

    try:
        score_connection = sqlite3.connect(ROOT_DATABASE) 
        cursor = score_connection.cursor()
        cursor.execute(
            """CREATE TABLE players(
                alias VARCHAR(10),
                price SMALLINT(10)
            )            
            """
        )
        score_connection.commit()
        score_connection.close()

    except Exception as ex:
        print(ex)

def insertScore(alias, price):
    """Insert a new score"""

    score_connection = sqlite3.connect(ROOT_DATABASE)
    cursor = score_connection.cursor()
    instruction = f"INSERT INTO players VALUES('{alias}', {price})"
    cursor.execute(instruction)
    score_connection.commit()
    score_connection.close()

def readScores():
    """Read all the historic scores"""

    score_connection = sqlite3.connect(ROOT_DATABASE)
    cursor = score_connection.cursor()
    instruction = "SELECT * from players ORDER BY price DESC"
    cursor.execute(instruction)
    data = cursor.fetchall()
    score_connection.commit()
    score_connection.close()    
    return data

def deleteScores():
    """Delete all the historic scores"""

    score_connection = sqlite3.connect(ROOT_DATABASE)
    cursor = score_connection.cursor()
    instruction = "DELETE FROM players"
    cursor.execute(instruction)
    score_connection.commit()
    score_connection.close()  