
board = [
    [7 ,0 ,0 ,4 ,0 ,0 ,1 ,2 ,0],
    [6 ,0 ,0 ,0 ,7 ,5 ,0 ,0 ,9],
    [0 ,0 ,0 ,6 ,0 ,1 ,0 ,7 ,8],
    [0 ,0 ,7 ,0 ,4 ,0 ,2 ,6 ,0],
    [0 ,0 ,1 ,0 ,5 ,0 ,0 ,3 ,0],
    [9 ,0 ,4 ,0 ,6 ,0 ,0 ,0 ,5],
    [0 ,7 ,0 ,3 ,0 ,0 ,0 ,1 ,2],
    [1 ,2 ,0 ,0 ,0 ,7 ,4 ,0 ,0],
    [0 ,4 ,9 ,2 ,0 ,6 ,0 ,0 ,0]
]

# print the board
def print_board(bd):

    for i in range(len(bd)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - - -")

        for j in range(len(bd[0])):
            if j % 3 == 0:
                print(" | ", end="")

            if j == 8:
                print(bd[i][j], "| ")

            else:
                print(str(bd[i][j]), end=" ")

# return (y, x) coordinate for empty space in board
def find_space(bd):
    for i in range(len(bd)):
        for j in range(len(bd[0])):
            if bd[i][j] == 0:
                return (i, j)
    return False

# determine whether the number drawn is justified
def justified(bd, num, pos):

    # check row for reccurences
    for i in range(len(bd)):
        if bd[pos[0]][i] == num and pos[1 ]!= i:
            return False
    # check columm
    for i in range(len(bd)):
        if bd[i][pos[1]] == num and pos[0] != i:
            return False
    # check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y *3, box_y *3 + 3):
        for j in range(box_x *3, box_x *3 + 3):
            if bd[i][j] == num and (i ,j) != pos:
                return False

    return True

# solve the soduku
def solve(bd):
    empty = find_space(bd)
    if not empty:
        return True
    else:
        row, col = empty

    for i in range(1 ,10):
        if justified(bd, i, (row, col)):
            bd[row][col] = i

            if solve(bd):
                return True

            bd[row][col] = 0

print_board(board)

solve(board)

print(" \n")

print_board(board)