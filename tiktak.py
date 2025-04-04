import random

def drawBoard(board):
    print('*---' * 3, end='*\n')
    print(f'* {board[0] or "0"}', f'* {board[1] or "1"}', f'* {board[2] or "2"} *', end='\n')
    print('*---' * 3, end='*\n')
    print(f'* {board[3] or "3"}', f'* {board[4] or "4"}', f'* {board[5] or "5"} *', end='\n')
    print('*---' * 3, end='*\n')
    print(f'* {board[6] or "6"}', f'* {board[7] or "7"}', f'* {board[8] or "8"} *', end='\n')
    print('*---' * 3, end='*\n')

def isAvailable(place, board):
    return board[place] not in ['X', 'O']

def isFinished(board):
    # Check rows
    for i in range(0, 7, 3):
        if board[i] == board[i+1] == board[i+2] and board[i] in ['X', 'O']:
            return True
    # Check columns
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] and board[i] in ['X', 'O']:
            return True
    # Check diagonals
    if (board[0] == board[4] == board[8] or board[2] == board[4] == board[6]) and board[4] in ['X', 'O']:
        return True
    # Check for draw
    if all(space in ['X', 'O'] for space in board):
        print("It's a draw!")
        return True
    return False

def makeMove(place, board):
    while True:
        try:
            if 0 <= place <= 8 and isAvailable(place, board):
                board[place] = 'O'
                drawBoard(board)
                break
            else:
                place = int(input("Invalid move. Try again: "))
        except ValueError:
            place = int(input("Please enter a valid number between 0 and 8: "))

def ranMove(board):
    while True:
        tryMove = random.randint(0, 8)
        if isAvailable(tryMove, board):
            board[tryMove] = 'X'
            drawBoard(board)
            break

def playGame():
    while True:
        board = [None] * 9  # Initialize empty board
        gameOver = False
        print("Okay, I'll go first!")
        board[4] = 'X'  # Computer takes center if available
        drawBoard(board)

        while not gameOver:
            userMove = int(input("Where do you want to play? "))
            makeMove(userMove, board)
            if isFinished(board):
                print("Game over. You win!")
                gameOver = True
                break
            print("My turn!")
            ranMove(board)
            if isFinished(board):
                print("Game over. I win!")
                gameOver = True
                break

        playAgain = input("Do you want to play again? Type Y or N: ").strip().lower()
        if playAgain != 'y':
            print("Thanks for playing! Bye!")
            break

# Run the game
while True:
    start = input("Do you want to play tic-tac-toe? Type Y or N: ").strip().lower()
    if start == 'y':
        playGame()
        break
    elif start == 'n':
        print("Ok, bye!")
        break
    else:
        print("Sorry, I didn't understand that.")