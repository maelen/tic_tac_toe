#!/usr/bin/env python3
# Tic Tac Toe game by Marie-Josee Blais

import random

# Import basic pygame modules
import pygame
from pygame.locals import *

# See if we can load more than standard BMP
if not pygame.font:
    print('Warning, fonts disabled')

if not pygame.image.get_extended():
    raise SystemExit("Sorry, extended image module required")


def is_winning(board, pos_x, pos_y, player):
    winning = False
    testing = False

    if board[pos_x][pos_y] == 0:
        testing = True
        board[pos_x][pos_y] = player

    for y in range(0, 3):
        if y == 2:
            winning = True
            print("Match H Line")
        else:
            if board[pos_x][y] != board[pos_x][y + 1]:
                # print("No Match H Line")
                break

    for x in range(0, 3):
        if x == 2:
            winning = True
            print("Match V Line")
        else:
            if board[x][pos_y] != board[x + 1][pos_y]:
                # print("No Match V Line")
                break

    if pos_x == pos_y:
        for x in range(0, 3):
            if x == 2:
                winning = True
                print("Match Diag 1")
            else:
                if board[x][x] != board[x + 1][x + 1]:
                    # print("No Match Diag 1")
                    break

    if pos_x + pos_y == 2:
        for x in range(0, 3):
            if x == 2:
                winning = True
                print("Match Diag 2")
            else:
                if board[x][2 - x] != board[x + 1][1 - x]:
                    # print("No Match Diag 2")
                    break

    if testing:
        board[pos_x][pos_y] = 0

    return winning


def get_next_position(board, last_position, player):
    other_player = 2 if player == 1 else 1

    for x in range(0, 3):
        for y in range(0, 3):
            if is_winning(board, x, y, player):
                print("Player winning position")
                return(x, y)
            elif is_winning(board, x, y, other_player):
                print("Other player winning position")
                return(x, y)

    # Check that this is not the first round
    if not last_position:
        # Did other player choose a corner ?
        if(last_position == (0, 0) or
           last_position == (0, 2) or
           last_position == (2, 0) or
           last_position == (2, 2) and
           board[1][1] == 0):
            print("Other player pulling a fast one 1")
            return(1, 1)

    # Check that this is not the first round
    if not last_position:
        # Did other player choose the center ?
        if last_position == (1, 1):
            print("Other player pulling a fast one 2")
            # Choose first available corner
            if board[0][0] == 0:
                return(0, 0)
            elif board[0][2] == 0:
                return(0, 2)
            elif board[2][0] == 0:
                return(2, 0)
            elif board[2][2] == 0:
                return(0, 0)

    # Choose a random position
    while True:
        x = random.randint(0, 2)
        y = random.randint(0, 2)
        if board[x][y] == 0:
            print("Random position")
            return (x, y)


def get_board_mouse_pos(w, h, mouse_x, mouse_y):
    if mouse_x > 0.65 * w:
        x = 2
    elif mouse_x > 0.35 * w:
        x = 1
    else:
        x = 0

    if mouse_y > 0.65 * h:
        y = 2
    elif mouse_y > 0.35 * h:
        y = 1
    else:
        y = 0
    print("MousePosition: {} {}".format(x, y))
    return (y, x)


def main(winstyle=0):
    SCREENRECT = Rect(0, 0, 640, 480)
    w = SCREENRECT.width * 0.90
    h = SCREENRECT.height * 0.90

    COLOR_WHITE = (250, 250, 250)
    COLOR_BLACK = (0, 0, 0)
    COLOR_RED = (250, 0, 0)
    COLOR_GREEN = (0, 250, 0)
    COLOR_BLUE = (0, 0, 250)

    board = [[0, 0, 0],
             [0, 0, 0],
             [0, 0, 0]]

    last_position = None

    # Initialize game
    pygame.init()
    pygame.display.set_caption("MJB Tic-Tac-Toe")

    # Set the display mode
    winstyle = 0  # |FULLSCREEN
    bestdepth = pygame.display.mode_ok(SCREENRECT.size, winstyle, 32)
    screen = pygame.display.set_mode(SCREENRECT.size, winstyle, bestdepth)

    # Draw background
    background = pygame.Surface(SCREENRECT.size)
    background = background.convert()
    background.fill(COLOR_WHITE)
    pygame.draw.line(background, COLOR_BLACK,
                     (0.35 * w, 0.05 * h),
                     (0.35 * w, 0.95 * h),
                     5)
    pygame.draw.line(background, COLOR_BLACK,
                     (0.65 * w, 0.05 * h),
                     (0.65 * w, 0.95 * h),
                     5)
    pygame.draw.line(background, COLOR_BLACK,
                     (0.05 * w, 0.35 * h),
                     (0.95 * w, 0.35 * h),
                     5)
    pygame.draw.line(background, COLOR_BLACK,
                     (0.05 * w, 0.65 * h),
                     (0.95 * w, 0.65 * h),
                     5)

    # Draw player 1
    p1_image = pygame.Surface((Rect(0, 0, 0.20 * w, 0.20 * h)).size)
    p1_image.fill(COLOR_WHITE)
    pygame.draw.rect(p1_image, COLOR_BLUE, Rect(
        0, 0, int(0.18 * w), int(0.18 * h)), 0)
    pygame.draw.rect(p1_image, COLOR_WHITE, Rect(
        int(0.02 * w), int(0.02 * h), int(0.14 * w), int(0.14 * h)), 0)

    # Draw player 2
    p2_image = pygame.Surface((Rect(0, 0, 0.20 * w, 0.20 * h)).size)
    p2_image.fill(COLOR_WHITE)
    pygame.draw.circle(p2_image, COLOR_RED, (int(0.10 * w),
                                             int(0.10 * h)), int(0.10 * h), 0)
    pygame.draw.circle(p2_image, COLOR_WHITE, (int(
        0.10 * w), int(0.10 * h)), int(0.07 * h), 0)

    player_images = [None, p1_image, p2_image]

    board_position = (((0.10*w, 0.10*h), (0.40*w, 0.10*h), (0.70*w, 0.10*h)),
                      ((0.10*w, 0.40*h), (0.40*w, 0.40*h), (0.70*w, 0.40*h)),
                      ((0.10*w, 0.70*h), (0.40*w, 0.70*h), (0.70*w, 0.70*h)))

    clock = pygame.time.Clock()

    running = True
    while running:
        # Start a new game
        winner = None
        board = [[0, 0, 0],
                 [0, 0, 0],
                 [0, 0, 0]]

        # Display The Background
        screen.blit(background, (0, 0))
        pygame.display.flip()

        # Choose a random player
        player = random.randint(1, 2)

        for _ in range(9):
            # Write to board
            if player == 1:
                (x, y) = get_next_position(board, last_position, player)
            else:
                wait_for_button = True
                while wait_for_button:
                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            (button1, _, _) = pygame.mouse.get_pressed()
                            if button1:
                                (mouse_x, mouse_y) = pygame.mouse.get_pos()
                                (x, y) = get_board_mouse_pos(w, h,
                                                             mouse_x, mouse_y)
                                if board[x][y] == 0:
                                    wait_for_button = False
            board[x][y] = player
            screen.blit(player_images[player], board_position[x][y])
            pygame.display.flip()
            if player == 2:
                pygame.time.wait(1000)
            last_position = [x, y]

            # winning condition if yes finish game
            if is_winning(board, x, y, player):
                winner = player
                break
            else:
                player = 2 if player == 1 else 1

        if winner is None:
            message = "No winner"
        else:
            if winner == 1:
                message = "Computer wins ! "
            else:
                message = "You win ! "
        print(message)
        if pygame.font:
            font = pygame.font.Font(None, 36)
            text = font.render(message, 1, (10, 10, 10))
            textpos = text.get_rect(centerx=background.get_width() / 2)
            screen.blit(text, textpos)
            pygame.display.flip()

        wait_for_button = True
        while wait_for_button:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    wait_for_button = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    wait_for_button = False

    clock.tick(240)
    pygame.quit()


# Call the "main" function if running this script
if __name__ == '__main__':
    main()
