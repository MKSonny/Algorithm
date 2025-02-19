import sys

input = sys.stdin.readline

def game_validation(board):
    def check_piece():
        piece = {'X': 0, 'O': 0}
        for i in range(3):
            for j in range(3):
                if board[i][j] == '.': continue
                piece[board[i][j]] += 1

        return piece['X'], piece['O']

    board = [list(board[:3]), list(board[3:6]), list(board[6:])]

    def check_bingo():
        bingo = {'X': 0, 'O': 0}

        # 가로 빙고 체크
        for row in board:
            if len(line := list(set(row))) == 1 and line[0] != '.':
                bingo[line[0]] += 1

        # 세로 빙고 체크
        for col in zip(*board):
            if len(line := list(set(list(col)))) == 1 and line[0] != '.':
                bingo[line[0]] += 1

        # 대각선 빙고 체크
        if len(line := list(set([board[0][0], board[1][1], board[2][2]]))) == 1 and line[0] != '.':
            bingo[line[0]] += 1
        if len(line := list(set([board[0][2], board[1][1], board[2][0]]))) == 1 and line[0] != '.':
            bingo[line[0]] += 1

        return bingo['X'], bingo['O']

    piece_x, piece_o = check_piece()
    bingo_x, bingo_o = check_bingo()

    if bingo_x == 0 and bingo_o == 0:
        if piece_x == 5 and piece_o == 4:
            return "valid"
    elif bingo_x <= 2 and bingo_o == 0:
        if piece_x - 1 == piece_o:
            return "valid"
    elif bingo_x == 0 and bingo_o == 1:
        if piece_x == piece_o:
            return "valid"
    return "invalid"


while (board := input().strip()) != "end":
    print(game_validation(board))