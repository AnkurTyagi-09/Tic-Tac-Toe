import math
import random

def print_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")

def check_win(board, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

def check_draw(board):
    return all(space != " " for space in board)

def minimax(board, depth, is_maximizing):
    if check_win(board, "O"):  # AI wins
        return 1
    if check_win(board, "X"):  # Player wins
        return -1
    if check_draw(board):  # Draw
        return 0
    
    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(board, depth + 1, False)
                board[i] = " "
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(board, depth + 1, True)
                board[i] = " "
                best_score = min(score, best_score)
        return best_score

def best_move(board, player):
    best_score = -math.inf if player == "O" else math.inf
    move = -1
    for i in range(9):
        if board[i] == " ":
            board[i] = player
            score = minimax(board, 0, player == "O")
            board[i] = " "
            if (player == "O" and score > best_score) or (player == "X" and score < best_score):
                best_score = score
                move = i
    return move

def tic_tac_toe():
    board = [" "] * 9
    mode = input("Choose mode: 1 for Single Player, 2 for Two Player: ")
    while mode not in ["1", "2"]:
        mode = input("Invalid choice. Choose 1 for Single Player or 2 for Two Player: ")
    
    print_board(board)
    current_player = "X"
    
    while True:
        if mode == "1" and current_player == "O":
            print("AI is making a move...")
            move = best_move(board, "O")
        else:
            try:
                move = int(input(f"Player {current_player}, enter your move (1-9): ")) - 1
                if board[move] != " ":
                    print("This space is already taken. Try again.")
                    continue
            except (ValueError, IndexError):
                print("Invalid move. Enter a number between 1 and 9.")
                continue
        
        board[move] = current_player
        print_board(board)
        
        if check_win(board, current_player):
            print(f"Player {current_player} wins!")
            break
        elif check_draw(board):
            print("It's a draw!")
            break
        
        current_player = "O" if current_player == "X" else "X"

tic_tac_toe()
2