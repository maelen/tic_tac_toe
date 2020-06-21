#!/usr/bin/env python3
# Tic Tac Toe game by Marie-Josee Blais

import random

#import basic pygame modules
import pygame
from pygame.locals import *

#see if we can load more than standard BMP
if not pygame.font:
    print('Warning, fonts disabled')
if not pygame.image.get_extended():
    raise SystemExit("Sorry, extended image module required")

SCREENRECT     = Rect(0, 0, 640, 480)
COLOR_WHITE    = (250,250,250)
COLOR_BLACK    = (0,0,0)
COLOR_RED      = (250,0,0)
COLOR_GREEN    = (0,250,0)
COLOR_BLUE     = (0,0,250)

def is_winning(board, pos_x, pos_y, player):
    winning=False
    testing=False
    
    if(board[pos_x][pos_y] == 0):
        testing = True
        board[pos_x][pos_y] = player
    
    for y in range(0,3):
        if (y == 2):
            winning=True
            print("Match H Line")
        else:
            if(board[pos_x][y] != board[pos_x][y+1]):
                # print("No Match H Line")
                break

    for x in range(0,3):
        if (x == 2):
            winning=True
            print("Match V Line")
        else:
            if(board[x][pos_y] != board[x+1][pos_y]):
                # print("No Match V Line")
                break

    if(pos_x==pos_y):
        for x in range(0,3):
            if (x == 2):
                winning=True
                print("Match Diag 1")
            else:                
                if(board[x][x] != board[x+1][x+1]):
                    #print("No Match Diag 1")
                    break

    if(pos_x+pos_y==2):
        for x in range(0,3):
            if (x == 2):
                winning=True
                print("Match Diag 2")
            else:                
                if(board[x][2-x] != board[x+1][1-x]):
                    #print("No Match Diag 2")
                    break
                    
    if(testing == True):
       board[pos_x][pos_y] = 0
       
    return winning

def get_next_position(board, last_position, player):
    if player==1:
        other_player=2
    else:
        other_player=1
    for x in range(0,3):
        for y in range(0,3):
            if(is_winning(board, x, y, player)):
                print("Player winning position")
                return(x,y)
            elif(is_winning(board, x, y, other_player)):
                print("Other player winning position")
                return(x,y)
    # Check that this is not the first round
    if not last_position:
        # Did other player choose a corner ?
        if( last_position == (0,0) or
            last_position == (0,2) or
            last_position == (2,0) or
            last_position == (2,2) and
            board[1][1] == 0):
            print("Other player pulling a fast one 1")
            return(1,1)
    
    # Check that this is not the first round    
    if not last_position:
        # Did other player choose the center ?
        if(last_position == (1,1)):
            print("Other player pulling a fast one 2")
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
            print("Random position")
            return (x,y)
                    
def main(winstyle = 0):
    board = [[0,0,0],
             [0,0,0],
             [0,0,0]]

    last_position = None
    winner = None

    # Initialize game
    pygame.init()
    pygame.display.set_caption("MJB Tic-Tac-Toe")

    # Set the display mode
    winstyle = 0  # |FULLSCREEN
    bestdepth = pygame.display.mode_ok(SCREENRECT.size, winstyle, 32)
    screen = pygame.display.set_mode(SCREENRECT.size, winstyle, bestdepth)

    background = pygame.Surface(SCREENRECT.size)
    background = background.convert()
    background.fill(COLOR_WHITE)

    w = SCREENRECT.width * 0.90
    h = SCREENRECT.height * 0.90
    
    p1Image = pygame.Surface((Rect(0, 0, 0.20*w, 0.20*h)).size)
    p2Image = pygame.Surface((Rect(0, 0, 0.20*w, 0.20*h)).size)
    
    p1Image.fill(COLOR_BLUE)
    p2Image.fill(COLOR_RED)
    playerImages = [0,p1Image,p2Image]
    
    pygame.draw.line(background, COLOR_BLACK, (0.35 * w, 0.05 * h ), (0.35 * w, 0.95 * h), 5)
    pygame.draw.line(background, COLOR_BLACK, (0.65 * w, 0.05 * h ), (0.65 * w, 0.95 * h), 5)
    pygame.draw.line(background, COLOR_BLACK, (0.05 * w, 0.35 * h ), (0.95 * w, 0.35 * h), 5)
    pygame.draw.line(background, COLOR_BLACK, (0.05 * w, 0.65 * h ), (0.95 * w, 0.65 * h), 5)
    
    #Display The Background
    screen.blit(background, (0, 0))
    pygame.display.flip()
    
    BoardPosition = [[(0.10*w, 0.10*h),(0.40*w, 0.10*h),(0.70*w, 0.10*h)],
                    [ (0.10*w, 0.40*h),(0.40*w, 0.40*h),(0.70*w, 0.40*h)],
                    [ (0.10*w, 0.70*h),(0.40*w, 0.70*h),(0.70*w, 0.70*h)]]
    
    player=1
    clock = pygame.time.Clock()    
    for i in range(9):
        #write to board
        (x,y)=get_next_position(board, last_position, player)  
        board[x][y] = player
        screen.blit(playerImages[player], BoardPosition[x][y])
        pygame.display.flip()
        pygame.time.wait(1000)
        last_position = [x,y]       

        #winning condition if yes finish game
        if (is_winning(board, x,y,player)):
            winner = player
            break
        else:
            player=2 if player==1 else 1
        
    if(winner == None):
        print ("No winner !")
    else:
        print ("Winner is player " + str(player))

    running = True

    while running:        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
    clock.tick(240)
    pygame.quit()
    
#call the "main" function if running this script
if __name__ == '__main__': main()
