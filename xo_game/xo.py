# Xs and Os game

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
	# moves += 1
	# if moves >= 9:
	# 	print('TIE!')
	# 	return True
	if grid[row][col] != 0:
		print('try somewhere else, plz.')
	else:
		grid[row][col] = sym
		if checkGrid(row, col):
			print(symtab[sym], 'WON!\n')
			return True
		else:
			pass
	printGrid()


grid = [[0,0,0],[0,0,0],[0,0,0]]
symtab = ['X', 'O']
# moves = 0


def main():
	print('Field numbers:\n  0 1 2\n0 _ _ _\n1 _ _ _\n2 _ _ _')
	
	while True:
		xrow = input("X's row: ")
		xcol = input("X's col: ")
		if play(int(xrow), int(xcol), 1):
			break
		orow = input("O's row: ")
		ocol = input("O's col: ")
		if play(int(orow), int(ocol), 2):
			break




# ------------------------------------------------
if (__name__ == '__main__'): 
    main()