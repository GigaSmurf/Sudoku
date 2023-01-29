board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]
#1. Find the empty position
#2. Try all numbers 1-9
#3. Find the first(or next) value that is valid
#4. Repeat for all values in that row
#5. "BackTrack" algorithm - if looped through all the values and none can be valid, then set the previous value to 0 trying a dif num -->
# backtrack again (if needed)
def solve (bo):
    find = find_empty(bo)
    if not find:
        #found the solution
        return True
    else:
        row, col = find
    #check through all values
    for i in range(1,10):
        #check if valid solution
        if valid(bo, i, (row,col)):
            bo[row][col] = i
            #recursion for the next values until something is false - if solve is false bo[row][col] of the previous is set
            #to zero to "backtrack" and try to get a different value...if that doesn't work "backtrack" again
            if solve(bo):
                return True
            #backtracks, setting the value to zero, continuing the loop to get a different number
            bo[row][col] = 0
    return False

#Check if value valid at that position
def valid(bo, num, pos):
    # Check row
    for i in range(len(bo[0])):
        #insert num and ignore the row we just inserted
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(bo)):
        #Check if the comlum value is valid
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
        #What box we are in
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False

    return True

def print_board(bo):

    for i in range(len(bo)):
        if i % 3 == 0 and i!=0:
            print("- - - - - - - - - - - - ")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j!=0:
                print(" | ", end="")
                
            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")
def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j) #row, column
    #No blank squares
    return None
print_board(board)
solve(board)
print("___________________________________")
print_board(board)



