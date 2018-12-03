# Xs and Os game

def checkRow(row):
    if 0 != grid[row][0] == grid[row][1] == grid[row][2]:
        return True
    else:
        return False

def checkCol(col):
    if 0 != grid[0][col] == grid[1][col] == grid[2][col]:
        return True
    else:
        return False

def checkMinDiag():
    if 0 != grid[0][2] == grid[1][1] == grid[2][0]:
        return True
    else:
        return False

def checkMajDiag():
    if 0 != grid[0][0] == grid[1][1] == grid[2][2]:
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
        print(symtab[row[0]], symtab[row[1]], symtab[row[2]])


def play(row, col, sym):
    grid[row][col] = sym
    printGrid()
    if checkGrid(row, col):
        print(symtab[sym], 'WON!\n')
        return True
    else:
        return False
    

grid = [[0,0,0],[0,0,0],[0,0,0]]
symtab = ['_', 'X', 'O']


def main():
    moves = 0;
    print('Field numbers:\n  1 2 3\n1 _ _ _\n2 _ _ _\n3 _ _ _')
    
    while True:
        if moves == 9:
            print("TIE!")
            break
        sign = 1 if moves%2==0 else 2
        while True:
            row = int(input(str(symtab[sign]) + "'s row: ")) - 1
            col = int(input(str(symtab[sign]) + "'s col: ")) - 1
            if row in range(0,3) and col in range(0,3) and grid[row][col] == 0 : break
        moves += 1
        if play(int(row), int(col), sign):
            break

    # --------------test
    # tietab = [[0,0],[1,1],[0,1],[0,2],[2,0],[1,0],[1,2],[2,1],[2,2]]
    # xwntab = [[1,1],[0,0],[0,1],[1,0],[2,0],[0,2],[2,1],[2,2],[1,2]]
    # tab = tietab
    # for n in range(0,9):
    #   print(n)
    #   sign = 1 if n%2==0 else 2
    #   if play(tab[n][0], tab[n][1], sign):
    #       break
    #   if n == 8: print('TIE!')
    # ------------------

    
# ------------------------------------------------
if (__name__ == '__main__'): 
    main()
