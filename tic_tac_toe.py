def printBoard(board):
    for r in range(0, len(board)):
        for c in range(0, len(board[r])):
            print(board[r][c], end=' ')
        print()


def isWinnerHorizontally(player, board):
    cnt = 0
    for r in range(0, 3):
        for c in range(0, 3):
            if player == board[r][c]:
                cnt = cnt + 1

        if cnt >= 3:
            return True
        else:
            cnt = 0
    return False


def isWinnerVertically(player, board):
    cnt = 0
    for r in range(0, 3):
        for c in range(0, 3):
            if player == board[c][r]:
                cnt = cnt + 1
        if cnt >= 3:
            return True
        else:
            cnt = 0
    return False


def isWinnerOnDiagonal1(player, board):
    cnt = 0
    for r in range(0, 3):
        if player == board[r][r]:
            cnt = cnt + 1
    if cnt >= 3:
        return True
    else:
        return False


def isWinnerOnDiagonal2(player, board):
    cnt = 0
    if board[0][2] == player:
        cnt = cnt + 1
    if board[1][1] == player:
        cnt = cnt + 1
    if board[2][0] == player:
        cnt = cnt + 1
    if cnt == 3:
        return True
    return False


def isWinner(player, board):
    if isWinnerHorizontally(player, board):
        return True
    if isWinnerVertically(player, board):
        return True
    if isWinnerOnDiagonal1(player, board):
        return True
    if isWinnerOnDiagonal2(player, board):
        return True
    else:
        return False


print("Tic-Tac-Toe")
print()
print()

while True:
    board = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
    printBoard(board)
    while True:
        print("Player X'x turn")
        row = int(input("Enter your row to play on (1,2,3): "))
        col = int(input("Enter your col to play on (1,2,3): "))
        row = row - 1
        col = col - 1

        board[row][col] = "X"
        printBoard(board)

        if isWinner("X", board):
            print("X is the Winner!")
            break

        print()

        print("Player O's turn")
        row = int(input("Enter your row to play on (1,2,3): "))
        col = int(input("Enter your col to play on (1,2,3): "))
        row = row - 1
        col = col - 1

        board[row][col] = "O"
        printBoard(board)

        if isWinner("O", board):
            print("O is the Winner!")
            break

        print()
        print()

    print()
    print()
    playAgain = input("Would you like to play another game? (y or n)")
    if playAgain == "n":
        break
        print()
        print()
        print("Thank you for playing Tic-Tac-Toe.  I hope that you had fun!")