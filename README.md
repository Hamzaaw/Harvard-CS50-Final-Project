   Tic Tac Toe Game
    #### Description:A simple Tic Tac Toe game made with python.Can be enjoyed by two players, where one player is "X" and the other is "O" and both take turns marking either "X" or "O" on a 3x3 grid, and the first player to get 3 in a horizontal,vertical or diagonal row is the winner.If the there is no empty unit left on the grid and there is not any winner declared, then that means it i a tie.

The code for this project consists of 5 functions.

1.display_board:is used to display the 3x3 grid with 9 cells to represent the tic tac toe board,the board includes the position of the "X" and "O" which would be placed by the players.This function is used to show the current state of the game, it makes it easy for player to visualize the game.
2.check_winner: this function is resonsible for checking if there is a wiiner after every turn.So whenever either of the players make a move this function then checks if the game is over and there is a winner.This function uses array for it's implementation, and check for 3 "X" or "O" in a vertical/horizonatal/diagonal row.If found then the fuction returns the winner of the game.
3.make_move: this function is responsible for taking the input of the players and converting and inputting it into the correct position on the 3x3 grid.
4.check_tie: This function is similar to the check_winner function but instead of checking for wiiner after every move this instead checks for a tie after every turn.
5.main: This function is where all other function are called, this is also where the inputs are being taken.The function first instialises a exe matrix to represent the tic tac toe board. Intially all cells are empty.Setting the current player to "X".A while loops that runs until the game ends with either a winner or a tie.Inside the loop it calls the display_board function to print the current state of the board showing the position of "X" or "O". The function ask the player to move by inputing a position from 1 to 9.Then it checks if the position is valid and if the move can be made by calling make_move function.If the position is invalid and continues to the next iteration of the loop.Now after every move the check_winner function is called to see if the game has ended and if there is a winner.If there is a wiiner , the displau_board function is called to display the final baord state, and announces the winnerand then exits the loop.

The test_project consists of three functions.
1.test_make_move
2.test_check_winner
3.test_check_tie
