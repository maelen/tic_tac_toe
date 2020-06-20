#!/usr/bin/env python
# Tic Tac Toe game by Marie-Josee Blais

import random, os.path

MAX_BOARD_DIM = 3

board = [[0,0,0],
         [0,0,0],
         [0,0,0]]

lastPosition = [-1,-1]
         
main_dir = os.path.split(os.path.abspath(__file__))[0]

def isWinning(posX,posY,player):
    global board
    winning=False
    testing=False
    
    if(board[posX][posY] == 0):
        testing = True
        board[posX][posY] = player
    
    for y in range(0,3):
        if (y == 2):
            winning=True
            print "Match H Line"
        else:
            if(board[posX][y] != board[posX][y+1]):
                # print "No Match H Line"
                break

    for x in range(0,3):
        if (x == 2):
            winning=True
            print "Match V Line"
        else:
            if(board[x][posY] != board[x+1][posY]):
                # print "No Match V Line"
                break

    if(posX==posY):
        for x in range(0,3):
            if (x == 2):
                winning=True
                print "Match Diag 1"
            else:                
                if(board[x][x] != board[x+1][x+1]):
                    #print "No Match Diag 1"
                    break

    if(posX+posY==2):
        for x in range(0,3):
            if (x == 2):
                winning=True
                print "Match Diag 2"
            else:                
                if(board[x][2-x] != board[x+1][1-x]):
                    #print "No Match Diag 2"
                    break
                    
    if(testing == True):
       board[posX][posY] = 0
       
    return winning

def getNextPosition(player):
    global lastPosition
    if player==1:
        otherPlayer=2
    else:
        otherPlayer=1
    for x in range(0,3):
        for y in range(0,3):
            if(isWinning(x,y,player)):
                print "Player winning position"
                return(x,y)
            elif(isWinning(x,y,otherPlayer)):
                print "Other player winning position"
                return(x,y)
    # Check that this is not the first round
    if( cmp(lastPosition,[-1,-1]) != 0):
        # Did other player choose a corner ?
        if((cmp(lastPosition,[0,0]) == 0  or
            cmp(lastPosition,[0,2]) == 0  or
            cmp(lastPosition,[2,0]) == 0  or
            cmp(lastPosition,[2,2]) == 0) and
            board[1][1] == 0):
            print "Other player pulling a fast one 1"
            return(1,1)
    
    # Check that this is not the first round    
    if( cmp(lastPosition,[-1,-1]) != 0):
        # Did other player choose the center ?
        if(cmp(lastPosition,[1,1]) == 0):
            print "Other player pulling a fast one 2"
            # Choose first available corner
            if(board[0][0] == 0):
                return(0,0)
            elif(board[0][2] == 0):
                return(0,2)
            elif(board[2][0] == 0):
                return(2,0)
            elif(board[2][2] == 0):
                return(0,0)
    
    # Choose a random position    
    while(True):
        x = random.randint(0,2)
        y = random.randint(0,2)
        if (board[x][y] == 0):
            print "Random position"
            return (x,y)

            
def main(winstyle = 0):
    global board
    global lastPosition
    winner = 0
    
    board[0]  = [0,0,0]
    player=1
    for i in xrange(9):
        #write to board
        (x,y)=getNextPosition(player)
        board[x][y] = player
        lastPosition = [x,y]           
        print board[0]
        print board[1]
        print board[2]
        print    
        
        #winning condition if yes finish game
        if (isWinning(x,y,player)):
            winner = player
            break
        else:
            if player==1:
                player=2
            else:
                player=1
    if(winner == 0):
        print "No winner !"
    else:
        print "Winner is player " + str(player)    
    
#call the "main" function if running this script
if __name__ == '__main__': main()
