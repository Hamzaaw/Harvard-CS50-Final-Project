import pytest
from project import make_move, check_winner, check_tie

def test_make_move():
    board = [" " for _ in range(9)]

    # Test a valid move
    assert make_move(board, 4, "X") == True
    assert board[4] == "X"

    # Test an invalid move (position already taken)
    assert make_move(board, 4, "O") == False
    assert board[4] == "X"  # Should still be X

def test_check_winner():
    # Winning scenario for X
    board_x_wins = ["X", "X", "X", " ", " ", " ", " ", " ", " "]
    assert check_winner(board_x_wins) == "X"

    # Winning scenario for O
    board_o_wins = ["O", " ", " ", "O", " ", " ", "O", " ", " "]
    assert check_winner(board_o_wins) == "O"

    # No winner
    board_no_winner = ["X", "O", "X", "X", "O", "O", "O", "X", "X"]
    assert check_winner(board_no_winner) is None

def test_check_tie():
    # Scenario with a tie
    board_tie = ["X", "O", "X", "X", "O", "O", "O", "X", "X"]
    assert check_tie(board_tie) == True

    # Scenario without a tie (empty spaces)
    board_no_tie = ["X", "O", " ", " ", "O", " ", " ", " ", " "]
    assert check_tie(board_no_tie) == False

    # Scenario without a tie (winning condition)
    board_winner = ["X", "X", "X", " ", " ", " ", " ", " ", " "]
    assert check_tie(board_winner) == False
