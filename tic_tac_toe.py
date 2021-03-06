"""
Implement tic-tac-toe
The program is in not played optimally by both sides because the moves are chosen randomly
"""

import random

#O(1)
def win(player, row, col, n):
    if (row  in occupied_row[player] and len(occupied_row[player][row]) == n) or (col in occupied_col[player] and len(occupied_col[player][col]) == n) or len(occupied_diag_up[player]) == n or len(occupied_diag_down[player]) == n:
        return True
    else:
        return False
#O(1)
def fill(player, row, col, n):
    if row not in occupied_row[player]:
        occupied_row[player][row] = set()
    occupied_row[player][row].add(col)
    
    if col not in occupied_col[player]:
        occupied_col[player][col] = set()
    occupied_col[player][col].add(row)
    
    if row == col:
        if player not in occupied_diag_down:
            occupied_diag_down[player] = set()
        occupied_diag_down[player].add((row, col))
    
    if col == n-1-row:
        if player not in occupied_diag_up:
            occupied_diag_up[player] = set()
        occupied_diag_up[player].add((row, col))

#O(1)    
def move(player, row, col, n):
    board[row][col] = 'O' if player == 1 else 'X'
    fill(player, row, col, n)
    
    if win(player, row, col, n):
        return player

#O(n+n)
def game(board, n):
    player = random.randint(1, 2)
    while len(s):
        position = random.choice(s)
        row = (position-1) // n
        col = (position-1) % n
        s.remove(position)
        win = move(player, row, col, n)
        if win:
            return win
        player = 2 if player == 1 else 1
    return -1
    
n = int(input())
board = [['.' for i in range(n)] for j in range(n)]

s = []

for i in range(n*n):
    s.append(i+1)

occupied_row = {1: {}, 2: {}}
occupied_col = {1: {}, 2: {}}
occupied_diag_up = {1: set(), 2: set()}
occupied_diag_down = {1: set(), 2: set()}

win_player = game(board, n)

print('Final board: ', board)
if win_player == -1:
    print('Draw')
else:
    print('Player win: ', win_player)
