import random

import ai
turnNumber = 0
board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]  # set up the board to be completely empty at the start
humanMoving: bool = random.choice([True, False])
winner = ""


def nextTurn():
    global humanMoving
    global winner
    showBoard()
    checkWinner()
    if winner != "":
        endGame()
    else:
        if humanMoving:
            humanMoving = False
            playerTurn()
        else:
            humanMoving = True
            aiTurn()


def introduction():
    print('''
    Welcome to Tic Tac Toe!

    Enter a number from 1 - 9 corresponding with the tile on the board as follows to move there!
        
                1 | 2 | 3
                ---------
                4 | 5 | 6
                ---------
                7 | 8 | 9
    
    Players take alternating turns placing symbols on the tiles of the grid to move there.

    Once one of the players scores three in a row, column or diagonal on the board, that player wins the game. 
    If the board becomes filled up and neither player has won, the game is ended in a draw.
                          
    The computer's tiles are denoted by a O, while the player's tiles are denoted by an X.
    ''')


def startGame():
    print()
    print("Let's begin!")
    if humanMoving:
        print("The player will go first!")
    else:
        print("The computer will go first!")
    nextTurn()


# noinspection PyBroadException
def playerTurn():
    grid_index = -1
    choosing = True
    while choosing:
        print()
        chosen_grid = input("Enter the square in which you would like to place your tile: ")
        try:
            grid_index = int(chosen_grid) - 1
            if grid_index in range(0, 9) and board[grid_index] == " ":
                choosing = False
            else:
                print("Not a valid tile")
        except:
            print("That was not a number silly goose X:(")

    board[grid_index] = "X"
    nextTurn()


def aiTurn():
    move = ai.optimalMove(board)
    print()
    print("The computer moved to tile " + str(move + 1))
    board[move] = "O"
    nextTurn()


def checkWinner():
    global winner
    global turnNumber
    if turnNumber == 9:

        winner = "No one is"
    turnNumber += 1
    for combination in ai.winningCombinations:
        if "X" == board[combination[0] - 1] == board[combination[1] - 1] == board[combination[2] - 1]:
            winner = "You are"
        elif "O" == board[combination[0] - 1] == board[combination[1] - 1] == board[combination[2] - 1]:
            winner = "The computer is"



def showBoard():
    print()
    print("             " + board[0] + " | " + board[1] + " | " + board[2])
    print("             ---------")
    print("             " + board[3] + " | " + board[4] + " | " + board[5])
    print("             ---------")
    print("             " + board[6] + " | " + board[7] + " | " + board[8])


def endGame():
    print()
    print(winner + " the winner!")


introduction()
startGame()
