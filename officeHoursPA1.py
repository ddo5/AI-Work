import time # used for the timing features, see how long soln takes

#Global Vars (board and dictionary files) (POINT TO FILES)
WORD_DICT = "./twlo6.txt"
PREFIXES = "./twl06-prefixes.txt"

# Globals to store those contents
myDict = frozenset(word.strip() for word in open(WORD_DICT))
prefixDict = frozenset(word.strip() for word in open(PREFIXES))

N = 0 # size of the boggle board square, determine when we read the board in
totalMoves = 0 # moves, that we will increase with each
Answers = {} # place to store the found words, indexed by word length

#highly as recurisve as possible, check for hit, extended in all poissible directions
def explore( curWord, curPos, path ):
    global Answers, myBoard, totalMoves
    # if in explore, we are making a move, what is the first thing you want to do? (INCREMENT NUM MOVES)
    totalMoves += 1

    # this is adding the lattest char to the curWord
    newchar = myBoard[curPos[0]][curPos[1]].lower() # convert to lower (board data is in caps) (text data is all lowercase)
    newcurWord = curWord + newchar # add latest char to the newcurWord
    newpath = path+(curPos,) # add current pos to the path

    #comparsions and searches
    if(newcurWord in myDict): # if it's a good word, then success
        if not len(newcurWord) in Answers: Answers[len(newcurWord)] = set() #
        Answers[len(newcurWord)].add(newcurWord.upper())
    elif USE_Prefixes and (not newcurWord in prefixDict): return 1

    #legal positions
    exploreNext = genNextPos(curPos).difference(newpath)
    # now recurisvely explore all viable other positions
    for position in exploreNext:
        explore(newcurWord, position, newpath)

def genNextPos(curPos):
    x=curPos[0]
    y=curPos[1]
    myRange = range(0,N)
    newPlaces = set()
    deltas = (-1,0,1)

    for dx in deltas:
        for dy in deltas:
            nextP = (x+dx, y+dy)
            if(( nextP[0] in myRange ) and nextP[1] in myRange ) and (( nextP[0], nextP[1] ) !=curPos: newPlaces.add(nextP))
    return newPlaces

def loadBoard(fname):
    global N
    n = 0 # keep track of actual n board size
    newBoard = []
    with open (fname) as f:
        content=f.readlines()
        content=[x.strip() for x in content]
        for line in content:
            newBoard.append(line.split())
            n+=1

        N=n # set global to local
        return newBoard # generating into a 1D array

def printBoard(aBoard):
    print()
    for line in aBoard:
        print(" ".join(line))
    print()

def runBoard(boardfile, cleverness): #cleverness flag (using prefixes)
    global USE_Prefixes. myBoard, totalTime #identify dictionary
    USE_Prefixes = cleverness

    # load the board
    myBoard = loadBoard(boardfile)
    printBoard(myBoard)

    print("board loaded, time to run solver\n")

    # explore every board position
    start_time = time.time()
    for x in range(0,N):
        for y om range(0,N):
            explore('', (x,y) , ())
            #print("I found ", Answers, " starting with ", myBoard[x][y], " at ", x, y)
    totalTime = (time.time() - start_time)

    print("A;; done\n\n Searrched tota; of {:d} moves in {:6.3f} seconds".format(totalMoves, totalTime))

    print("\nWords Found:")
    Output = []
    for key in sorted(Answers.key()):
        print(key, "-letter words: ",",".join(answers[key]))
        Output += list(Answers[key])

    print("\nFound ", len(Output), " words in total. \n Alpha-sorted list words:")
    print(", ".join(sorted(Output)))

    print("\n\n")

BOARD = "./fourboard2.txt"
USE_Prefixes = False

#run iwthout PREFIXES
runBoard(BOARD, USE_Prefixes)

# run again, with PREFIXES
USE_Prefixes = True
runBoard(BOARD, USE_Prefixes)

# Question : how does explore have access to myBoard, shouldnt it take it as param
    #Answer : make myBoard global. Yes it needs to be global or Yes it needs to be passed in
'''
 Should you always declare your global variables the moment they are relevant? I.E., at the start of the main or in its pertinent local function

 delcare later on when it is needed, if you need it all the time the declare it before

'''
