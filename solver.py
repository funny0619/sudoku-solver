import math
def isvalid(arr, row, col, value):
    length = int(math.sqrt(len(arr)))
    # check row
    for i in range(len(arr[0])):
        if arr[row][i] == value:
            return False
    # check column
    for i in range(len(arr)):
        if arr[i][col] == value:
            return False
    # check square
    x = row // length
    y = col // length
    for i in range(x * length, x * length + length):
        for j in range(y * length, y * length + length):
            if arr[i][j] == value:
                return False

    return True

def findEmpty(arr):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == 0:
                return (i, j)

def sudokuSolver(arr):
    found = findEmpty(arr)
    if not found:
        return True
    else:
        row = found[0]
        col = found[1]
    for value in range(1, len(arr) + 1):
        if isvalid(arr, row, col, value):
            arr[row][col] = value
            if sudokuSolver(arr):
                return True
            arr[row][col] = 0
