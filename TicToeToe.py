import random

SYSTEM, PLAYER = 'X', 'O'

def isMovesLeft(Board):
	for i in range(3):
		for j in range(3):
			if (Board[i][j] == '_'):
				return True
	return False

def evaluate(Board):
	for row in range(3) :	
		if (Board[row][0] == Board[row][1] and Board[row][1] == Board[row][2]):	
			if (Board[row][0] == SYSTEM):
				return 10
			elif (Board[row][0] == PLAYER):
				return -10

	for col in range(3):
		if (Board[0][col] == Board[1][col] and Board[1][col] == Board[2][col]):
			if (Board[0][col] == SYSTEM):
				return 10
			elif (Board[0][col] == PLAYER):
				return -10

	if (Board[0][0] == Board[1][1] and Board[1][1] == Board[2][2]):
		if (Board[0][0] == SYSTEM):
			return 10
		elif (Board[0][0] == PLAYER):
			return -10

	if (Board[0][2] == Board[1][1] and Board[1][1] == Board[2][0]):
		if (Board[0][2] == SYSTEM):
			return 10
		elif (Board[0][2] == PLAYER):
			return -10

	return 0

def minimax(Board, depth, isSystem):
    score = evaluate(Board)
    if (score == 10):
        return score
    if (score == -10):
        return score
    if (isMovesLeft(Board) == False):
        return 0
    
    if (isSystem):
        best = -1000
        for i in range(3):
            for j in range(3):
                if (Board[i][j]=='_'):
                    Board[i][j] = SYSTEM
                    best = max(best, minimax(Board, depth + 1, not isSystem))
                    Board[i][j] = '_'
        return best
    else :
        best = 1000
        for i in range(3):
            for j in range(3):
                if (Board[i][j] == '_'):
                    Board[i][j] = PLAYER
                    best = min(best, minimax(Board, depth + 1, not isSystem))
                    Board[i][j] = '_'
        return best

def findBestMove(Board):
	bestVal = -1000
	bestMove = (-1, -1)
	for i in range(3):
		for j in range(3):
			if (Board[i][j] == '_'):
				Board[i][j] = SYSTEM
				moveVal = minimax(Board, 0, False)
				Board[i][j] = '_'
				if (moveVal > bestVal):
					bestMove = (i, j)
					bestVal = moveVal
	return bestMove

Board = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]

isSystem = random.choice([False,True])

while True:
    if isSystem:
        (x,y) = findBestMove(Board)
        print("Systems's move : ",x,y)
        Board[x][y] = SYSTEM
    else:
        x,y = map(int, input("Player's move : ").split())
        if Board[x][y]!='_':
            print("Enter a valid move.")
            isSystem = not isSystem
        else:
            Board[x][y] = PLAYER
    
    for row in Board:
        print(row)
    
    score = evaluate(Board)
    if score==10:
        print("It's System win!")
        break
    elif score==-10:
        print("It's Player win!")
        break
    elif not isMovesLeft(Board):
        print("It's a Draw!")
        break
    else:
        isSystem = not isSystem