#!/usr/bin/env python3
# Tic Tac Toe game by Marie-Josee Blais

import random


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
        if (last_position == (0, 0) or
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


def main():
    board = [[0, 0, 0],
             [0, 0, 0],
             [0, 0, 0]]

    last_position = None
    winner = None
    player = 1

    for _ in range(9):
        # write to board
        (x, y) = get_next_position(board, last_position, player)
        board[x][y] = player
        last_position = [x, y]
        print("{}\n{}\n{}\n".format(board[0], board[1], board[2]))

        # winning condition if yes finish game
        if is_winning(board, x, y, player):
            winner = player
            break
        else:
            player = 2 if player == 1 else 1

    if winner is None:
        print("No winner !")
    else:
        print("Winner is player {}".format(player))


# call the "main" function if running this script
if __name__ == '__main__':
    main()
