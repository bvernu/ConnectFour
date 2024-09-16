import connectfour

def column_row_input() -> 'dimensions':
    '''Repeatedly asks user for column and row inputs until valid.'''
    while True:
        try:
            rows = int(input("Enter number of rows. Must be an integer more than or equal to 4 and less than or equal to 20"))
            columns = int(input("Enter number of columns. Must be an integer more than or equal to 4 and less than or equal to 20"))

            if (rows < 4 or columns < 4 or rows > 20 or columns > 20):
                print("Number of rows and columns must be more than or equal to 4 and less than or equal to 20")
            else:
                return columns, rows
                break
        except ValueError:
            print("Number of rows and columns must be integers more than or equal to 4 and less than or equal to 20")
            continue

def check_valid_input(game_state: 'GameState') -> 'GameState':
    '''Repeatedly asks for input that satisfies the given gameboard size.'''
    columns = connectfour.columns(game_state)
    while True:
        try:
            input1 = input("Enter your move. First specify DROP or POP and then the column number:")

            input1 = input1.split()

            move = input1[0]
            column_num = int(input1[1])

            if move != "DROP" and move != "POP":
                print("Must specify move first as DROP or POP")
            elif column_num > columns:
                print("Must be within the valid gameboard. Your gameboard has {} columns".format(columns))
            else:
                return game_state, move, column_num
                break
        except ValueError:
            print("First specify drop or remove and then the column number. Example: 'DROP 4' or 'POP 6'.")
            continue
        except IndexError:
            print("First specify drop or remove and then the column number. Example: 'DROP 4' or 'POP 6'.")
            continue

def check_valid_move(game_state: 'GameState', move: str, column_num: int) -> 'GameState':
    '''Repeatedly asks for input until it is a valid game move given
    the current state of the gameboard.'''
    while True:
        if move == "DROP":
            try:
                game_state_new = connectfour.drop(game_state, column_num-1)
                return game_state_new
                break
            except:
                print("Piece can not be dropped in the given column because the specified column is already filled")
                game_state, move, column_num = check_valid_input(game_state)
                return check_valid_move(game_state, move, column_num)
        if move == "POP":
            try:
                game_state_new = connectfour.pop(game_state, column_num-1)
                return game_state_new
                break
            except:
                print("Piece can not be popped in the given column because the specified column does not have any pieces or it was not placed by you")
                game_state, move, column_num = check_valid_input(game_state)
                return check_valid_move(game_state, move, column_num)

def print_board(game_state: 'GameState') -> None:
    '''Prints the current gameboard given the current game state.'''
    columns = connectfour.columns(game_state)
    rows = connectfour.rows(game_state)
    for i in range(1, columns):
        if i < 9:
            i = str(i)
            print(i.ljust(3), end = "")
        elif i == 9:
            i = str(i)
            print(i, end = "")
        else:
            i = str(i)
            print(i.rjust(3), end = "")
    if columns < 10:
        print(str(columns).ljust(3), end = "")
    else:
        print(str(columns).rjust(3), end = "")
    for i in range(rows):
        print()
        for element in game_state[0]:
            if element[i] == 0:
                print("*  ", end = "")
            elif element[i] == 1:
                print("Y  ", end = "")
            elif element[i] == 2:
                print("R  ", end = "")
    print()

