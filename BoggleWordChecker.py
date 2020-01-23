def find_word(board, word):
    max_x = len(board[0]) - 1
    max_y = len(board) - 1 
    index = 1
    len_word = len(word)
    word_arr = list(word)
#     print(word)
    # Loop through all letters on the board.
    for y, row  in enumerate(board):
        for x, letter in enumerate(row):
            # If we found the first letter on the board, check it to see if it connects.
            if letter == word_arr[0]:
                used = set()
                used.add((x, y))
#                 print(f'start letter: {board[y][x]}, ({x+1}, {y+1})')
                if check_word(x, y, board, word_arr, index, max_x, max_y, used):
                    return True
    return False
            
def check_word(x, y, board, word_arr, index, max_x, max_y, used):
    # Make local copy of used to manipulate.
    local_used = used.copy()
    # If we've found the last letter, return True.
    if index >= len(word_arr):
#         print('Found last letter')
        return True
    next_letter = word_arr[index]
    # Loop through all valid connecting letters to see if it is the next letter.
    for new_x in range(x-1, x+2):
        for new_y in range(y-1, y+2):
            if ((new_x >= 0) and (new_y >= 0)) and ((new_x <= max_x) and (new_y <= max_y)):
                if (new_x, new_y) not in local_used:
                    curr_letter = board[new_y][new_x]
                    # If we found the next letter, call the function to check the next letter with new params.
                    if curr_letter == next_letter:
                        local_used.add((new_x, new_y))
#                         print(f'Current letter: {curr_letter} == {next_letter} at ({new_x}, {new_y})')
                        if check_word(new_x, new_y, board, word_arr, index+1, max_x, max_y, local_used):
                            return True
                        else:
                            continue
    # Did not find any valid connecting letters.
#     print('Found no connector')
    return False
    
    
