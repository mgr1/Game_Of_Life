# File:    proj1.py
# Author:  Matthew Grant
# Date:    11/17/15
# Section: 03
# Description:
#             This program allows a user to run Conway's Game of Life for a given number
#             of iterations. 


def initialBoard():

    # initialBoard generates the initial board as defined by the user.
    # Input: Board dimensions, and whether pixels are dead or alive
    # Output: Initial board

    
    boardRows = int(input("Please enter the number of rows as a positive integer: "))

    while boardRows <= 0:

        boardRows = int(input("Please enter a positive integer: "))

    boardColumns = int(input("Please enter the number of columns as a positive integer: "))

    while boardColumns <= 0:

        boardColumns = int(input("Please enter a positive integer: "))
    
    


    # Initialize board as a list

    board = []


    # Populate each row

    for i in range(boardRows):

        board.append([])

        for j in range(boardColumns):

            board[i].append(".")




    # Determine which cells are to be living

    # 'A' is used to represent a living cell and '.' is used to represent a dead cell

    cellRow = "filler"

    while cellRow != 'q':

        cellRow = input("Please enter the row of a cell you would like to make alive: ")

        if cellRow != 'q':

            cellRow = int(cellRow)

            if cellRow >= 0 and cellRow < boardRows:

                cellColumn = int(input("Please enter the column of the cell you would like to make alive: "))

                if cellColumn < 0 or cellColumn >= boardColumns:

                    print("Column input must be greater than or equal to zero or less than", boardRows)

                    while cellColumn < 0 or cellColumn >= boardColumns:

                        cellColumn = int(input("Please try again: "))

                board[cellRow][cellColumn] = 'A'

            else:

                print("Row input must be greater than or equal to zero and less than", boardRows)

                cellRow = input("Try again: ")
    

    print("Starting Board")

    for i in range(boardRows):

        for j in range(boardColumns):

            if (j + 1) % boardColumns == 0:

                print(board[i][j])

            else:

                print(board[i][j], end = '')

    print("\n\n")

    return board




def iteration(startingBoard, iterations):

    # iteration runs one iteration of Conway's Game of Life
    # Input: The board from the last iteration (the starting board for the first time)
    # Output: A new iteration of the board

    iterationCount = 0

    boardRows = len(startingBoard)

    boardColumns = len(startingBoard[0])

    board = list(startingBoard)

    displayBoard = []

    for n in range(boardRows):

        displayBoard.append([])

        for o in range(boardColumns):

            displayBoard[n].append('.')

    board = list(board)

    while iterationCount < iterations:


        # Run an iteration

        iterationCount += 1

        # Turn living cells dead if they have less than two or more than three live neighbors


        for i in range(boardRows):

            for j in range(boardColumns):

                # Cases: Corners, side columns, top and bottom columns, and middle/general problems

                # Corner Cases

                if (i == 0 or i == (boardRows - 1)) and (j == 0 or j == (boardColumns - 1)):

                    surrList = []


                    # Top Left

                    if i == 0 and j == 0:

                        surrList = []

                        surrList.append(board[0][1])

                        surrList.append(board[1][1])

                        surrList.append(board[1][0])

                        displayBoard[i][j] = valueCheck(surrList, board, i, j)
                        
                        surrList = []

                    # Top Right 

                    elif i == 0 and j == (boardColumns - 1):

                        surrList = []

                        surrList.append(board[1][j])

                        surrList.append(board[0][j - 1])

                        surrList.append(board[1][j - 1])

                        displayBoard[i][j] = valueCheck(surrList, board, i, j)

                        surrList = []
                        
                
                    # Bottom Left (boardRows - 1, 0)

                    elif i == (boardRows - 1) and j == 0:

                        surrList = []

                        surrList.append(board[i][1])

                        surrList.append(board[i-1][0])
                        
                        surrList.append(board[i-1][1])

                        displayBoard[i][j] = valueCheck(surrList, board, i, j)

                        surrList = []

                    # Bottom Right (boardRows - 1, boardColumns - 1)

                    else:

                        surrList = []

                        surrList.append(board[i][j - 1])

                        surrList.append(board[i-1][j])

                        surrList.append(board[i-1][j-1])

                        displayBoard[i][j] = valueCheck(surrList, board, i, j)

                        surrList = []

                # Special Case of Top and Bottom Rows (not inclusive of corners)

                elif (i == 0 or i == (boardRows - 1)) and (j != 0 and j != (boardColumns - 1)):

                    surrList = []

                    surrList.append(board[i][j+1])

                    surrList.append(board[i][j-1])

                    if i == 0 and j != 0 and j != (boardColumns - 1):

                        # Top Row

                        surrList.append(board[i+1][j+1])

                        surrList.append(board[i+1][j-1])

                        surrList.append(board[i+1][j])

                    else:
                        # Bottom Row

                        surrList.append(board[i-1][j+1])

                        surrList.append(board[i-1][j-1])

                        surrList.append(board[i-1][j])

                    displayBoard[i][j] = valueCheck(surrList, board, i, j)

                    surrList = []

                # Special Case of the left and right columns (not inclusive of corners)

                elif (j == 0 or j == (boardColumns - 1)) and (i != 0 and i != (boardRows - 1)):

                    surrList = []

                    surrList.append(board[i-1][j])

                    surrList.append(board[i+1][j])

                    # Exclusives to left side

                    if j == 0:

                        surrList.append(board[i-1][j+1])

                        surrList.append(board[i][j+1])

                        surrList.append(board[i+1][j+1])

                    else:

                        surrList.append(board[i-1][j-1])

                        surrList.append(board[i][j-1])

                        surrList.append(board[i+1][j-1])

                    displayBoard[i][j] = valueCheck(surrList, board, i, j)

                    surrList = []

                # General Case (space not in the corners or sides, with 8 surrounding spaces)

                else:

                    surrList = []

                    surrList.append(board[i-1][j-1])

                    surrList.append(board[i-1][j])

                    surrList.append(board[i-1][j+1])

                    surrList.append(board[i][j-1])

                    surrList.append(board[i][j+1])

                    surrList.append(board[i+1][j-1])

                    surrList.append(board[i+1][j])

                    surrList.append(board[i+1][j+1])

                    displayBoard[i][j] = valueCheck(surrList, board, i, j)

                    surrList = []


        print("Iteration No.", iterationCount)

        # Print the new board

        for i in range(boardRows):

            for j in range(boardColumns):

                if (j+1) % boardColumns == 0:

                    print(displayBoard[i][j])

                else:

                    print(displayBoard[i][j], end = '')

        print("\n\n")

        # The new board is now treated as the initial board

        board = list(displayBoard[ : ])
      
def valueCheck(surrList, board, i, j):

    # valueCheck() finds out how many living or dead elements surround a cell
    # Input: Board, indices, and the list of surrounding cells
    # Output: Living or dead cell

    board = list(board)

    surrList = list(surrList)

    row = i

    column = j

    count = 0

    for e in surrList:

        if e =='A':

            count += 1


    if count < 2:

        return '.'

    elif board[row][column] == 'A':

        if count == 3 or count == 2:

            return 'A'

        else:

            return '.'

    elif count == 3 and board[row][column] == '.':

        return 'A'

    else:
        
        return '.'


        




                    

def main():

    # main() contains all the functions which make up the program as a whole
    # Input: Functions
    # Output: Conway's Game of Life

    print("Welcome to Conway's Game of Life!")

    print("Coded by Mattthew Grant")

    startingBoard = initialBoard()

    iterations = int(input("How many iterations would you like to run? "))

    iteration(startingBoard, iterations)

    print("Thank you for using this simulator!")

main()
