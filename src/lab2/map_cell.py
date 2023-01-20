'''
Extra Credit Task-

Tic tac toe input
Here's the backstory for this challenge: imagine you're writing a tic-tac-toe game, where the board looks like this:

1:  X | O | X
   -----------
2:    |   |  
   -----------
3:  O |   |
    A   B   C
The board is represented as a 2D list:

board = [
    ["X", "O", "X"],
    [" ", " ", " "],
    ["O", " ", " "],
]
Imagine if your user enters "C1" and you need to see if there's an X or O in that cell on the board. To do so, you need to translate from the string "C1" to row 0 and column 2 so that you can check board[row][column].

Your task is to write a function that can translate from strings of length 2 to a tuple (row, column). Name your function get_row_col; it should take a single parameter which is a string of length 2 consisting of an uppercase letter and a digit.

For example, calling get_row_col("A3") should return the tuple (2, 0) because A3 corresponds to the row at index 2 and column at index 0 in the board.

'''

''' The following function takes in a String of length 2, being an upper case letter and a digit
# the function uses "ord()" to convert the first letter to an ascii character
'''
cell = "C3"                          # user enters the cell 
def get_row_col(cell):
    row = ord(cell[0]) - ord('A')    # subtracting the ascii value of the first letter by 'A's value (65) to get the index of the row
    column = int(cell[1]) - 1        # subtracting one to get the correct column 
    print (row, column)              # prints the tuple corresponding to the cell

if __name__ == '__main__':
    get_row_col(cell)


