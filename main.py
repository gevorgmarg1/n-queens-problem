def diagonalCheck(board, row, col):         #Check the availability of the cell diagonally
    if row != len(board)-1:                 #If the given cell is not the last row
        for i in range(row+1, len(board)):  #Go down for until reached the last one
            if col-(i-row) >= 0:
                if (board[i][col-(i-row)] == 1):    #Check the south-east diagonals
                    return False
            if col+(i-row) < len(board[row]):       #Check the south-west diagonals
                if board[i][col+(i-row)] == 1:
                    return False
    if row != 0:                            #If the given cell is not the first row
        for j in range(row-1,-1, -1):       #Go up until reached the first row
            if col-(row-j) >= 0:                #Check the north-east diagonals
                if (board[j][col-(row-j)] == 1):
                    return False
            if col+(row-j) < len(board[row]):   #Check the north-west diagonals
                if (board[j][col+(row-j)] == 1):
                    return False
    return True                             #If everything was good, return True

def isValid(board, row, col):               #Checking if the cell is valid to set a new Queen
    if not 1 in board[row]:                 #Checking if any Queens in the same row
        for i in range(len(board[row])):    #---Checking if any Queens in the same column
            if board[i][col] == 1:
                return False                #---
        return diagonalCheck(board, row, col)       #If rows and columns are free, check diagonally
    else:
        return False

def solver(n):
    board = [[0 for i in range(n)] for j in range(n)]       #Build NxN matrix with 0s in it
    row = 0                                 #Variable for the number of rows
    col = 0                                 #Variable for the number of columns
    moveForward = True                      #A boolean to check if it allowed to go forward or not
    while row < len(board):                 #Run by each row
        while col < len(board[row]):        #Run by each column of the given row
            if board[row][col] == 1:
                board[row][col] = 0
                col += 1
            if isValid(board, row, col):    #Check the availability of the given cell
                board[row][col] = 1
                col = 0
                row += 1
                moveForward = True
                break                       #If everythin is ok, assign value of 1 to the given cell, go to the next row, Allow to move forward
            else:
                if col < len(board[row])-1 and moveForward:     #If not available and this is not the last cell of the row, go to the next cell in the row
                    col+=1
                else:                                           #If not available and reached to the last cell, go back to the previous row
                    moveForward = False                         #Do not allow to move forward
                    row -= 1                                    #Going to the previous row
                    col = board[row].index(1)+1                 #Go to the cell after the previously assigned value of 1
                    board[row][board[row].index(1)] = 0         #Change the beforehand assigned value to 0
                    while col >= len(board[row]) and row > 0:   #As the column number may exceed the possible number of columns, run through
                        if (1 in board[row]):                       #if there is 1 in the row change it to 0 and go back 1 row and assign the column number to the next
                            board[row][board[row].index(1)] = 0
                            row -= 1
                            col = board[row].index(1) + 1
                        else:
                            col = 0


    return board                                                #Once the problem is solved return the solved board

def main():
    solved = solver(int(input("Please type a number")))

    print("The solution for your input is: ")
    for i in solved:
        print(i, "\n")

if __name__ == "__main__":
    main()