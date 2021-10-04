import time
class Boggle():
    '''
    Function : loadWords
    Param: some file from user
    Return: Each entry in the txt document as a separate entity
    Goal: The goal of this function is to take a large set of words and funnel it into a dictionary that can be
        accessed later. This will be the key to validation of a possible word combination
    '''
    def loadWords(filename):
        words_file = open(filename, "r")
        lines = words_file.readlines()
        myDict = {}
        for val in lines:
            myValues = str.split(",")
            myDict.add(myValues[0].strip("\n"))
        print(myDict)
        return lines
    '''
    Function : loadBoard
    Param: filename, this has the board to be used in the game
    Return: My board in the form of a list of lists. Each row is a list of random characters
    Goal: The goal of this function is to load the board for the game. This does NOT format it
    '''
    def loadBoard(self, filename):
        #open file
        with open(filename, "r") as file:
            #read lines of the file
            lines = file.readlines()
            # initializing an empty list to append to
            myOut = []
            #looping through the lines and spliting/striping characters
            for str in lines:
                myList = str.split(",")
                myOut.append(myList[0].strip("\n"))
            #setting the appended values of myOut list to the board itself
            myBoard = myOut
            print(myOut)
        print('\n')
        return myBoard
    '''
    Function : printBoard
    Param: board loaded and saved in loadBoard
    Return: Printed display of the game board
    Goal: The goal of this function is to format the board correctly so that it prints the correct number of rows/cols
        evenly. 
    '''
    def printBoard(self, myBoard):
        # looping through the generated board
        for row in myBoard:
            #split the rows
            values = row.split()
            # join the values that were split with a space in between them
            print(' '.join(values))
        print('\n')
        return myBoard
    '''
    Function : possibleMoves
    Param: myBoard and (x,y) position 
    Return: Set of possible coordinates to move to 
    Goal: The goal of this function is to examine each possible move from a current position on the board. With different
        coordinates, different results are produced. The method will check whether a possible move leaps off the board
        into a upper bound. 
    '''
    def possibleMoves(self, x,y , myBoard):
        # initializing an empty moves list to append to when a move is found
        moves = []
        # counter for the possibilities found
        count = 0

        # the following conditionals check each position relative to the length of the board and current position
        # passed in. Up, Down, Left, Right, Diagonal
        # future iterations SHOULD include recursion for simplicity
        if x + 1 < len(myBoard[0]):
            moves.append((x + 1, y))
            count += 1
            if y + 1 < len(myBoard):
                moves.append((x + 1, y + 1))
                count += 1
            if y - 1 >= 0:
                moves.append((x + 1, y - 1))
                count += 1

        if x - 1 >= 0:
            moves.append((x - 1, y))
            count += 1
            if y + 1 < len(myBoard):
                moves.append((x - 1, y + 1))
                count += 1
            if y - 1 >= 0:
                moves.append((x - 1, y - 1))
                count += 1

        if y + 1 < len(myBoard):
            moves.append((x, y+1))
            count += 1

        if y - 1 >= 0:
            moves.append((x, y - 1))
            count += 1
        # formatting for output of the possible moves generated
        print("Possible Moves:" + '\n')
        print(moves)
        print('\n')
        print("Total moves found:" + '\n')
        print(count)
        print('\n')
        return moves

    '''
    Function : legalMoves
    Param: possibleMoves list, path taken 
    Return: A set of possible moves minus the ones already taken
    Goal: The goal of this function is to verify what legal moves can made from any current location. It is almost
        a replica of the previous function possibleMoves, but it takes into account where the player has already visited 
    '''
    def legalMoves(self, *possibleMoves, path):
        # setting the path taken to the possible moves already found
        path = possibleMoves
        # subtracting the possible moves to find what the next move can legally be
        legalPath = possibleMoves - path
        return legalPath

    '''
    Function : examineState
    Param: Boggle board, current position, reference dictionary 
    Return: Whether the current state or path is a valid word, printing the word found and verification 
    Goal: The goal of this function is to act as a lookup for the current path generated. If it matched a word in the 
        word dictionary, then a point is awarded
    '''
    def examineState(self, myBoard, x, y,  myDict):
        pass

if __name__ == '__main__':
    b = Boggle()
    myBoard = b.loadBoard('threeboard.txt')
    b.printBoard(myBoard)
    b.possibleMoves(3, 3, myBoard)
    b.possibleMoves(2, 1, myBoard)

