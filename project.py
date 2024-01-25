def display_board(board):
    for i in range(3):
        print(f" {board[i*3]} | {board[i*3+1]} | {board[i*3+2]} ")
        if i < 2:
            print("---+---+---")

def make_move(board, position, player):
    if board[position] == " ":
        board[position] = player
        return True
    return False

def check_winner(board):
    winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                            (0, 3, 6), (1, 4, 7), (2, 5, 8),
                            (0, 4, 8), (2, 4, 6)]
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != " ":
            return board[combo[0]]
    return None

def check_tie(board):
    return all([spot != " " for spot in board])

def main():
    board = [" " for _ in range(9)]
    current_player = "X"

    while True:
        display_board(board)
        try:
            position = int(input(f"Player {current_player}, enter your move (1-9): ")) - 1
            if position not in range(9) or not make_move(board, position, current_player):
                print("Invalid move, try again.")
                continue
        except ValueError:
            print("Please enter a number between 1 and 9.")
            continue

        if winner := check_winner(board):
            display_board(board)
            print(f"Player {winner} wins!")
            break
        if check_tie(board):
            display_board(board)
            print("It's a tie!")
            break

        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    main()
