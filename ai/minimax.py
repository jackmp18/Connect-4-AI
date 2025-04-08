# ai/minimax.py
import numpy as np
from game.board import is_valid_move, drop_piece, create_board, check_win

def get_best_move(board, piece):
    valid_moves = [c for c in range(board.shape[1]) if is_valid_move(board, c)]
    best_score = -float("inf")
    best_col = np.random.choice(valid_moves)

    for col in valid_moves:
        temp_board = board.copy()
        drop_piece(temp_board, col, piece)
        score = score_position(temp_board, piece)
        if score > best_score:
            best_score = score
            best_col = col
    return best_col

def score_position(board, piece):
    # Very simple scoring: prefer center
    center_array = [int(i) for i in list(board[:, board.shape[1]//2])]
    center_score = center_array.count(piece) * 3
    return center_score
