
# Author: Frederic Maire
# File last changed on 2008-08-02


import random

import your_player


# Constants for the cells
BLACK = +1  # First player colour
EMPTY = 0   # Empty cell indicator
WHITE = -1  # 2nd  player colour

NWIN = 4 # length of a winning segment

class Connect_N_Board:
    """
        A board is represented with a list of columns. Each column is itself a list of integer.
        This list of list is called 'cell'.
        The element cell[c][r] represents the content of the r'th element of the c'th column.
        It is either BLACK or WHITE or EMPTY.
    """
    
    def __init__(self, width = 7, height = 7):
        """
           Create an empty board
        """
        self.cell = [ [EMPTY for r in range(height)] for c in range(width) ]

    def reset(self):
        """
           Reset the board to an empty board of the same size as the current board
        """
        width = len(self.cell)
        height = len(self.cell[0])
        self.cell = [ [EMPTY for r in range(height)] for c in range(width) ]
        
    def __str__(self):       
        return  str(self.cell)
    
    def display(self):
        """
           Display the board on the screen
        """        
        print ' '        
        print 'Connect ', NWIN, ' Board '
        print ' '                
        for r in reversed(range(self.getHeight())):
            for c in range(self.getWidth()):
                if self.cell[c][r] == BLACK:
                    print '+',
                elif self.cell[c][r] == WHITE:
                    print '-',
                else:
                    print '.',
            print ' '
        for c in range(self.getWidth()):
            print c,
        print ' '
        print ' '

    # Height of the board (number of cells vertically)
    def getHeight(self):
        return len(self.cell[0])

    # Width of the board (number of cells horizontally)
    def getWidth(self):
        return len(self.cell)
        
    def deepCopy(self):
        """
            Return deep copy of this board.
            This clone of the board can be passed safely to any player without taking the risk
            of lunatic players damaging the original board.
        """
        clone = Connect_N_Board(self.getWidth(), self.getHeight())
        import copy
        clone.cell = copy.deepcopy(self.cell)
        return clone

    def legalMoves(self):
        """
            Return the list the column indices that can be played.
            This list is empty when the board is full.
        """
        return [c for c in range(self.getWidth()) if len([r for r in range(self.getHeight()) if self.cell[c][r]==EMPTY])>0 ]

    def checkwin(self):
        """
            Return winningColour, isGameFinished
            where
                'winningColour' is the colour of the winner ('winner' is set to EMPTY if the game is a draw or not finished yet)
                'isGameFinished' is a boolean            
        """
        w = self.getWidth()
        h = self.getHeight()
        numOccupiedCell = 0  # counter for the number of occupied cells (use to detect a terminal condition of the game)
        for r in range(h):
            for c in range(w):
                if self.cell[c][r] == EMPTY:
                    continue # this cell can't be part of winning segment
                # if we reach this point, the cell is occupied by a player stone
                numOccupiedCell = numOccupiedCell+1
                for dr,dc in [(1,0),(0,1),(1,1),(-1,1)]:  # direction of search
                    for i in range(NWIN):
                        # test if there exists a segment of NWIN uniformly coloured cells
                        if not(r+i*dr>=0) or not(r+i*dr<h) or not(c+i*dc<w) or not(self.cell[c+i*dc][r+i*dr] == self.cell[c][r]):
                            break # segment broken
                    else:
                        # Python remark: notice that the else is attached to the for loop "for i..."
                        # This block is executed if and only if 'i' arrives at the end of its range                        
                        return self.cell[c][r] , True # found a winning segment                    
        return EMPTY, numOccupiedCell==w*h
                                
        
    def makeMove(self, colour, move):
        """
            'move' is the column index of where the stone 'colour' should be dropped
            Warning: no error checking performed by this function.
        """
        emptyCellList = [r for r in range(self.getHeight()) if self.cell[move][r]==EMPTY]
        self.cell[move][emptyCellList[0]] = colour  # put the stone in the first empty cell of column 'move'
        
    def playOneGame(self, p1, p2, show):
        """
            Given two instances of players 'p1' and 'p2',  play out a game
            between them.  Returns the winning player. Returns 'None' in case of a draw.
            When 'show' is true, display each move in the game.
        """
        currentPlayer, otherPlayer = p1, p2
        winner = None
        gameFinished = False
        #
        while not(gameFinished):            
            if show:
                self.display()  # show the board
            #                
            move = currentPlayer.getMove(self.deepCopy())
            if show:
                print currentPlayer.name + ' is playing in column ' , move
            
            if (move == []) or (not move in self.legalMoves()): # for dysfunctional player
                gameFinished = True
                winner = otherPlayer
            else:                
                self.makeMove(currentPlayer.colour, move)
                winningColour, gameFinished = self.checkwin()
                if gameFinished:
                    winner = currentPlayer
                else:
                    currentPlayer, otherPlayer = otherPlayer, currentPlayer
        # if in verbose mode display the outcome of the game
        if show:
            self.display()
            if winner:
                print 'The winner is ', winner.name ,' ' ,
                if winner.colour == WHITE:
                    print 'White  -'
                else:
                    print 'Black  +'             
            else:
                print 'Game ended in a draw'
        #
        return winner

    def playHandicappedGameSeries(self, p1, p2, h, n, verbose):
        """
            Play n handicapped games between p1 and p2
            Player p1 starts with h extra moves
            Report the number of wins for each player
        """
        numWinP1 = 0
        numWinP2 = 0
        for i in range(n):
            self.reset()
            for i_h in range(h):
                move = p1.getMove(self.deepCopy())
                self.makeMove(p1.colour, move)            
            winner = self.playOneGame(p1, p2,verbose)
            if winner == p1:
                numWinP1 = numWinP1+1
            if winner == p2:
                numWinP2 = numWinP2+1
        print "Player ", p1.name, " won ", numWinP1, " games"
        print "Player ", p2.name, " won ", numWinP2, " games"
        print n-numWinP1-numWinP2, " games ended in a draw"
        
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

class Player:
    """
    A base class for  players.  All players must override
    the initialize and getMove methods.
    """
    def __init__(self, colour):
        """
        Records the player's colour, either  black or
        for white.  Should also set the name of the player.
        """
        self.colour = colour
        self.name = "Player"

    def getMove(self, board):
        """
        Given the current board, should return a valid move.
        """
        pass


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

class RandomPlayer(Player):
    """
    Chooses a random move from the set of possible moves.
    """
    def __init__(self, colour):
        self.colour = colour
        self.name = "Random"
    def getMove(self, board):
        moves = board.legalMoves()
        n = len(moves)
        if n == 0:
            return []
        else:
            return moves[random.randrange(0, n)]

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

class HumanPlayer(Player):
    """
    Prompts a human player for a move.
    """
    def __init__(self, colour):    
        self.colour = colour
        self.name = "Human"
    def getMove(self, board):
        c = input("Enter column index (or -1's to concede): ")
        if not c in board.legalMoves() :
            return []
        return c

    
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def run_single_game():
     cb = Connect_N_Board(8,5)
##     p1 = RandomPlayer(BLACK)
     p1 =  your_player.StudentPlayer_Example(BLACK)
##     p1 = your_player.StudentPlayer_MinMax(BLACK)
##     p1 = your_player.StudentPlayer_AlphaBeta(BLACK)     
     p2 =  HumanPlayer(WHITE)
     cb.reset() # remove all stones from the board
     winner = cb.playOneGame(p1, p2, True)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
def run_HandicappedGameSeries():
     cb = Connect_N_Board(8,5)
     p1 = RandomPlayer(BLACK)
##     p1 =  your_player.StudentPlayer_Example(BLACK)
##     p1 = your_player.StudentPlayer_MinMax(BLACK)
##     p1 = your_player.StudentPlayer_AlphaBeta(BLACK)     
     p2 =  your_player.StudentPlayer_Example(WHITE)
     
     cb.playHandicappedGameSeries(p1, p2, 1, 100, False)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


if __name__ == '__main__':
     run_single_game()
##     run_HandicappedGameSeries()
     # raw_input()


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
     
##
##                CODE CEMETARY
##                
##     print cb.legalMoves()
##
##     cb.makeMove(1,2)
##     print cb.legalMoves()
##     
##     cb.makeMove(-1,2)
##     print cb.legalMoves()
##     cb.makeMove(1,1)
##     print cb.legalMoves()
##     cb.makeMove(1,0)
##     print cb.legalMoves()
##     
##     cb.display()
##     
##     cb2.display()
