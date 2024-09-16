import project2_socket_functions
import project2_overlap_functions
import connectfour

def run() -> None:
    '''Runs the game of connect four'''

    connection = project2_socket_functions.valid_connect()
    columns, rows = project2_overlap_functions.column_row_input()
    project2_socket_functions.start_game(columns, rows, connection)

    project2_socket_functions.game_code(connection, columns, rows)
        
if __name__ == "__main__":
    run()
