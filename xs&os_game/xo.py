# hi

def checkRow(row):
	if grid[row][0] == grid[row][1] == grid[row][2]:
		return True
	else:
		return False

def checkCol(col):
	if grid[0][col] == grid[1][col] == grid[2][col]:
		return True
	else:
		return False

def checkMinDiag():
	if grid[0][2] == grid[1][1] == grid[2][0]:
		return True
	else:
		return False

def checkMajDiag():
	if grid[0][0] == grid[1][1] == grid[2][2]:
		return True
	else:
		return False

def checkGrid(row,col):
	if row == col == 1:
		if checkMajDiag() or checkMinDiag() or checkCol(col) or checkRow(row):
			return True
	elif (row+col)%2 == 1:
		if checkRow(row) or checkCol(col):
			return True
	else: 
		if checkRow(row) or checkCol(col):
			return True
		else:
			if row+col == 2:
				if checkMinDiag():
					return True
			else:
				if checkMajDiag():
					return True


def printGrid():
	for row in grid:
		print(row)


def play(row, col, sym):
	if grid[row][col] != 0:
		print('try somewhere else, plz.')
	else:
		grid[row][col] = sym
		if checkGrid(row, col):
			print(sym, 'won!\n')
		else:
			print('next turn>>')
	printGrid()



grid = [[0,0,0],[0,0,0],[0,0,0]]

os = 1
xs = 2

play(0,0,1)
play(0,1,1)
play(0,2,1)

