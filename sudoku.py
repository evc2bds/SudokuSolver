from pprint import pprint

def find_next_empty(puzzle):
    # finds the next row, col in the puzzle that is blank
    # return row, col tuple (or return (None, None) if there is not an empty row, col)
    
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r, c
    return None, None #if no spaces in the puzzle are left 

def is_valid(puzzle, guess, row, col):
    # figures out whether the guess at the row/col of the puzzle is a valid guess
    # returns True if is valid, False if not valid
    
    # check if guess is in the row:
    row_vals = puzzle[row]
    if guess in row_vals:
        return False
    
    # check if guess is in the column
    col_vals = []
    for i in range(9):
        col_vals.append(puzzle[i][col])
    if guess in col_vals:
        return False
    
    # check if guess is in the square we are in (start at beginning of square)
    # iterate over the 3 values in the row/column starting at the start row/column
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3
    
    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False
    return True 


def solve_sudoku(puzzle):
    # solve sudoku puzzle
    # puzzle is a list of lists, where each inner list is a row in the sudoku puzzle
    # return whether or not the solution exists to the puzzle 
    # if there is a solution, change the puzzle to be the solution
    
    # First choose a blank space in the puzzle to start and make a guess 
    row, col = find_next_empty(puzzle)
    
    # if there are no blank spaces left, then the puzzle is done 
    if row is None:
        return True # puzzle has been solved
    
    # If there's a place to put a number, then make a guess between 1 and 9
    # try all numbers 1-9 until we find a combination that works 
    for guess in range(1, 10):
        # Check if it is a valid guess
        if is_valid(puzzle, guess, row, col):
            # If the guess is valid then add it to the puzzle
            puzzle[row][col] = guess
            # Recursively call the solve_sudoku function 
            if solve_sudoku(puzzle): 
                return True
        # if the guess isn't valid OR it does not solve the puzzle, reset the value and try a new number
        puzzle[row][col] = -1 # reset value at this row/col
        
    # if none of the numbers work, the puzzle cannot be solved 
    return False

input_puzzle = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
]

print("Let's solve a 9x9 Sudoku Board!")
print("Enter the elements of the puzzle you want to solve one by one moving across each row.")
print("If the space is blank, enter '-1'")
for i in range(9):
    for j in range(9):
        print("Enter number at index", i, ", ", j)
        item = int(input())
        input_puzzle[i][j] = item

print(solve_sudoku(input_puzzle))        
pprint(input_puzzle)
    