#display board
def printBoard(board):
    print(board[1] + '|' + board[2] + '|' + board[3])
    print(board[4] + '|' + board[5] + '|' + board[6])
    print(board[7] + '|' + board[8] + '|' + board[9])
    print("\n")

#is the input valid?
def validSpace(position):
    #is it an empty space?
    if board[position] == '-':
        return True
    #if not empty then not valid space
    else:
        return False

#play game
def insertLetter(letter, position):
    if validSpace(position):
        #if empty space then play the position
        board[position] = letter
        #print updated version of board
        printBoard(board)
        #should be an easier way to check this
        if checkDraw():
            print("Draw!")
            #can we loop game? perhaps a play again function?
            playGame()
            #can definitely shorten check for win function
        if checkForWin():
            if letter == 'X':
                print("Bot wins!")
                playGame()
            else:
                print("Player wins!")
                playGame()

        return

    else:
        #invalid space
        print("Can't insert there!")
        position = int(input("Please enter new position:  "))
        #loop back to check space is valid
        insertLetter(letter, position)
        return

def checkForWin():
    #first row win
    if (board[1] == board[2] == board[3] != '-'):
        return True
    #second row win
    elif (board[4] == board[5] == board[6] != '-'):
        return True
    #third row win
    elif (board[7] == board[8] == board[9] != '-'):
        return True
    #first column win
    elif (board[1] == board[4] == board[7] != '-'):
        return True
    #second column win
    elif (board[2] == board[5] == board[8] != '-'):
        return True
    #third column win
    elif (board[3] == board[6] == board[9] != '-'):
        return True
    #first diagonal win
    elif (board[1] == board[5] == board[9] != '-'):
        return True
    #second diagonal win
    elif (board[7] == board[5] == board[3] != '-'):
        return True
    #no win
    else:
        return False

#was it noughts or crosses that won?
def checkWhichMarkWon(mark):
    if board[1] == board[2] == board[3] and board[1] == mark:
        return True
    elif (board[4] == board[5] == board[6] and board[4] == mark):
        return True
    elif (board[7] == board[8] == board[9] and board[7] == mark):
        return True
    elif (board[1] == board[4] == board[7] and board[1] == mark):
        return True
    elif (board[2] == board[5] == board[8] and board[2] == mark):
        return True
    elif (board[3] == board[6] == board[9] and board[3] == mark):
        return True
    elif (board[1] == board[5] == board[9] and board[1] == mark):
        return True
    elif (board[7] == board[5] == board[3] and board[7] == mark):
        return True
    else:
        return False

#if no more empty spaces then it is a draw
def checkDraw():
    for key in board.keys():
        if (board[key] == '-'):
            return False
    return True

#the user's move
def playerMove():
    #position choice
    position = int(input("Enter the position for 'O':  "))
    #check if valid, winning move etc
    insertLetter(player, position)
    return

def compMove():
    #default low score as we want to aim for anything higher
    bestScore = -800
    #default position as we cannot actually access this on the board therefore we MUST find a better move (position)
    bestMove = 0
    for key in board.keys():
        #if the position is empty...
        if (board[key] == '-'):
            #we will play that position...
            board[key] = bot
            #and work out what this score would be...
            score = minimax(board, 0, False)
            #take our position back out (effectivel undoing our turn)
            board[key] = '-'
            #if the score we found is higher than the previous bestScore then this is the new bestScore
            if (score > bestScore):
                bestScore = score
                #and therefore this will also be the key (position) we want to play in
                bestMove = key

    #check if move is valid, winning move, draw etc
    insertLetter(bot, bestMove)
    return

def minimax(board, depth, isMaximizing):
    #return who the winner is
    #1 if bot
    if (checkWhichMarkWon(bot)):
        return 1
    #-1 if player
    elif (checkWhichMarkWon(player)):
        return -1
    #0 if draw
    elif (checkDraw()):
        return 0

    #maximising
    if (isMaximizing):
        bestScore = -800
        for key in board.keys():
            if (board[key] == '-'):
                board[key] = bot
                score = minimax(board, 0, False)
                board[key] = '-'
                if (score > bestScore):
                    bestScore = score
        return bestScore
    #minimizing
    else:
        bestScore = 800
        for key in board.keys():
            if (board[key] == '-'):
                board[key] = player
                score = minimax(board, 0, True)
                board[key] = '-'
                if (score < bestScore):
                    bestScore = score
        return bestScore

#empty board
board = {1: '-', 2: '-', 3: '-',
         4: '-', 5: '-', 6: '-',
         7: '-', 8: '-', 9: '-'}

#what player will see when they run the program
printBoard(board)
print("Computer goes first! Good luck.")
print("Positions are as follow:")
print("1, 2, 3 ")
print("4, 5, 6 ")
print("7, 8, 9 ")
print("\n")
player = 'O'
bot = 'X'

global firstComputerMove
firstComputerMove = True

def playGame():
  #while game is still running
  while not checkForWin():
    compMove()
    playerMove()
  #if game is over...
  if checkForWin():
    #if user wants to play again
    playAgain = input("Want to play again?:   ")
    if playAgain =='Yes':
      
      playGame()
    #if user wants to quit
    else:
      exit()

playGame()
