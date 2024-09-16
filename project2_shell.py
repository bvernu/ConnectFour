import project2_overlap_functions
import connectfour

def run() -> None:
    '''Runs the game of connect four.'''
    valid_input = project2_overlap_functions.column_row_input()
    columns = int(valid_input[0])
    rows = int(valid_input[1])

    game_state = connectfour.new_game(columns, rows)

    project2_overlap_functions.print_board(game_state)

    winner = connectfour.winner(game_state)

    while winner == 0:

        game_state, move, column_num = project2_overlap_functions.check_valid_input(game_state)
        game_state = project2_overlap_functions.check_valid_move(game_state, move, column_num)

        project2_overlap_functions.print_board(game_state)

        winner = connectfour.winner(game_state)

    if winner == 1:
        print("Y IS THE WINNER!")
    elif winner == 2:
        print("R IS THE WINNER!")

if __name__ == "__main__":
    run()



