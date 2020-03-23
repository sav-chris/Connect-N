import connectN

# Constants
DEPTH = 4


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


class StudentPlayer_Example:
    """

        A (dumb) player example
    
    """

    def __init__(self, colour):
        self.colour = colour
        self.name = "BOB - n" # put your id here
        
    def getMove(self, board):
        # This example player always chooses the first move
        # from the set of possible moves.
        moves = board.legalMoves()
        n = len(moves)
        if n == 0:
            return []
        else:
            return moves[0]

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

class StudentPlayer_MinMax:
    """

    YOUR TASK:
    
    * Insert your name in  'self.name' in the '__init__' function.

    *Replace Insert the code of your player in the 'getMove' function.

    """

    def __init__(self, colour):
        self.colour = colour
        self.name = "The Killer Rabbit - n" # put your student id here
        
    def getMove(self, board):
        moves = getChildMoves(board)

        utilityMapFunction = lambda depth : (lambda b : maximiseUtility(b, depth))
        
        #get utilities of 'children'

        utilities = map(utilityMapFunction(DEPTH), moves)
        
        #utilities = maximiseUtility(board, DEPTH)
        return getMaxIndex(utilities) #get the best move
    
    def minimiseUtility(self, board, depth):        
        if (board.legalMoves() != []):  # if no legal moves
            # return evaluation of utility function
            return utility(board)
        elif (depth <= 0): # if reached depth
            # return evaluation of utility function
            return utility(board)
        else:
            # get child moves
            childMoves = getChildMoves(board)
            
            # reduce depth
            depth = depth - 1
            
            # get utilty using maximiseUtility(children, reduced Depth)
            maxFunc = lambda d : (lambda b : maximiseUtility(b, d)) #needs a bit of lambda calculus to do the map
            utilities = map(maxFunc(depth), childMoves)
            
            # choose child with minimum utility
            minIndex = getMinIndex(utilities)
            return utilities[minIndex]
            

    def maximiseUtility(self, board, depth):
        if (board.legalMoves() != []):  # if no legal moves
            # return evaluation of utility function
            return utility(board)
        elif (depth <= 0): # if reached depth
            # return evaluation of utility function
            return utility(board)            
        else:
            # get child moves
            childMoves = getChildMoves(board)
            
            # reduce depth
            depth = depth - 1
            
            # get utilty using minimiseUtility(children, reduced Depth)
            minFunc = lambda d : (lambda b : minimiseUtility(b, d)) #needs a bit of lambda calculus to do the map
            utilities = map(minFunc(depth), childMoves)
            
            # choose child with maximum utility
            maxIndex = getMaxIndex(utilities)
            return utilities[maxIndex]
            

    def utility(self, board):
        utility = 0
        for row in range(board.getHeight()):
            for collumn in range(board.getWidth()):
                horz = horizontalWindowUtility(board, row, collumn)
                vert = verticalWindowUtility(board, row, collumn)
                diag = diagWindowUtility(board, row, collumn)                
                utility = utility + horz + vert + diag  #sum total utility of all the windows
        return utility

        
                

    def horizontalWindowUtility(self, board, row, collumn):
        width = board.getWidth()

        if (collumn <= (width - (NWIN - 1))): #check that we haven't fallen off the board
            # check that window
            window = []
            for collumnIndexes in range(collumn, collumn + NWIN): #horizontal window
                window.append(board.cell[collumnIndexes, row]) # construct        
            return windowValue(window)            
            
        else:
            #we fell of the board, this window does not exist so return a zero utility
            return 0
        

    def verticalWindowUtility(self, board, row, collumn):
        height = board.getHeight()

        if (row <= (height - (NWIN - 1))): #check that we haven't fallen off the board
            # check that window
            window = []
            for rowIndexes in range(row, row + NWIN): #vertical window
                window.append(board.cell[collumn, rowIndexes]) # construct window
            return windowValue(window)    
            
        else:
            #we fell of the board, this window does not exist so return a zero utility
            return 0

    def diagWindowUtility(self, board, row, collumn):
        width = board.getWidth()
        height = board.getHeight()

        if ( (row <= (height - (NWIN - 1))) and (collumn <= (width - (NWIN - 1))) ): #check that we haven't fallen off the board
            # check that window
            window = []
            for indexes in range(NWIN): #diagnal up window
                window.append(board.cell[collumn + indexes, row + indexes]) # construct window
            return windowValue(window)
            
        else:
            #we fell of the board, this window does not exist so return a zero utility
            return 0

    def windowValue(self, window):
        #count the number of pices
        opponentsPieces = window.count(BLACK)
        thisPlayersPieces = window.count(WHITE)

        if (opponentsPieces == 0 and thisPlayersPieces != 0):
            return thisPlayersPieces #more pieces means higher utility
        elif (thisPlayersPieces == 0 and opponetsPieces != 0):
            return -1*opponentsPieces #more opponents pieces means negative utility
        else:
            return 0 # no one can claim this window, no utility



    def getChildMoves(self, board):
        childMoves = []
        for move in board.legalMoves():
            b = board.deepCopy()
            b.makeMove(player,move)
            childMoves.append(b)
        return childMoves

        
    def getMaxIndex(self, utilities):
        return utilities.index(max(utilities))

    def getMinIndex(self, utilities):
        return utilities.index(min(utilities))
        

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

class StudentPlayer_AlphaBeta:
    """

    YOUR TASK:
    
    * Insert your name in  'self.name' in the '__init__' function.

    *Replace Insert the code of your player in the 'getMove' function.

    """

    def __init__(self, colour):
        self.colour = colour
        self.name = "The Holy Hand Grenaide of Antioch - n" # put your student id here
        
    def getMove(self, board):
        moves = board.legalMoves()
        return moves[0]

        

    
 
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

class StudentPlayer_Champ:
    """

    YOUR TASK:
    
    * Insert your name in  'self.name' in the '__init__' function.

    *Replace Insert the code of your player in the 'getMove' function.

    """

    def __init__(self, colour):
        self.colour = colour
        self.name = "Sir Lancelot - n5741467" # put your student id here
        
    def getMove(self, board):
        return []


#code grave yard

    """
    def minimax(board, depth):

        if (depth > 0):
            moves = legalMoves(board)
            currentColour = (-1)^depth #alternate the colour, this could require attention

            #get list of possible boards
            for m in cb.legalMoves():
        	board = cb.deepCopy()
	        board.makeMove(currentColour,m)
	        boards.append(board)

        
        
            depth = depth - 1
        
        
        
        return []


    def bestMove(board, depth, turn):
        if ([] != board.legalMoves()): #any legal moves? 
            if (depth > 0): 
                #not reached end of depth --> keep searching
                nextTurn = turn * -1 #change turn
                nextDepth = depth - 1 #reduce depth
                
            else:
                #reached end of search --> evaluate utility
                
        else:
            #no more legal moves  --> evaluate utility up to here

            
    def untility(board, move, depth, player):
        boards = []
        for m in board.legalMoves():
        	b = board.deepCopy()
	        b.makeMove(player,m)
	        boards.append(b)

	return bestMove(boards,


	    def getUtilities(board, depth):
        
        


    def evaluateUtility(board):



    def getMaxIndex(utilities):
        return utilities.index(max(utilities))

    def getMinIndex(utilities):
        return utilities.index(min(utilities))




            # swap player
            # player = player * -1







        
        #for all windows
        for x = 1 : width:
            if (piece found):
                evaluate Windows around cell
                
            # traverse along collumns
                #if piece found, check windows
                #iterate up ^
                  #check windows

                
            evaluate utility of window for us
            find (wiegted ?) sum of utilities
        return utility














        
    for all cells on board
        #evaluation of our position
        if (nearEdge()):
            #start at edge
            evaluate window
        else:
            #start at poistion - N
            evaluate window

        #evaluation of opponent'sposition

        #find compromise

       function evaluate window
                #if window contains opponent, window is useless
                #count number of team's pieces




        
        if collumn <= 4
            cell = 1
        else
            cell = collumn - 3

        for line = start:collumn
            for i = 1:4
                if board[row, cell] < 0
                    i=4
                    value(line) = -1
                else
                    if board[row,cell] > 0
                        frame_tot += 1
        




        
"""

