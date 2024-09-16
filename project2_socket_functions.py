import socket
import connectfour
import project2_overlap_functions

def connect(host: str, port: int) -> 'connection':
    'Connects to the host and port specified by user'
    connectfour_socket = socket.socket()
    connectfour_socket.connect((host, port))

    connectfour_in = connectfour_socket.makefile('r')
    connectfour_out = connectfour_socket.makefile('w')

    return connectfour_socket, connectfour_in, connectfour_out

def close(connection: 'connection') -> None:
    'Closes the given connection'
    connectfour_socket, connectfour_in, connectfour_out = connection

    connectfour_in.close()
    connectfour_out.close()
    connectfour_socket.close()

def send_message(connection: 'connection', message: str) -> None:
    'Sends a line of text on the given connection, including a newline sequence'
    connectfour_socket, connectfour_in, connectfour_out = connection

    connectfour_out.write(message + '\r\n')
    connectfour_out.flush()

def receive_message(connection: 'connection') -> None:
    '''
    Receives a line of text from the given connection, which is returned
    without any kind of newline character/sequence in it
    '''
    connectfour_socket, connectfour_in, connectfour_out = connection

    return connectfour_in.readline()[:-1]

def valid_connect() -> 'connection':
    '''Repeatedly asks for input of host and port. If connection to the connect
    four server is successful, returns a connection.'''
    while True:
        try:
            host = input("What server would you like to connect to?")
            port = int(input("What is the port number?"))

            connection = connect(host, port)

            message = input("Username:")
            send_message(connection, "I32CFSP_HELLO {}".format(message))

            message_received = receive_message(connection)
            expected = f"WELCOME {message}"

            if message_received == expected:
                print(message_received)
                return(connection)
                break
            else:
                print("Incorrect username and/or server and/or port")
        except:
            print("Not the valid connect four server and/or port.")

def start_game(columns: int, rows: int, connection: 'connection') -> None:
    '''Starts the game. Sends server the colums and rows specified by user
    and prints that the server is ready.'''
    message = f"AI_GAME {columns} {rows}"
    send_message(connection, message)

    message_received = receive_message(connection)
    expected = "READY"
    
    if message_received == expected:
        pass
    else:
        close(connection)
        print("Received unexpected response from server. Connection closed.")

def game_code(connection: 'connection', columns: int, rows: int) -> None:
    '''The game code.'''

    game_state = connectfour.new_game(columns, rows)
    winner = connectfour.winner(game_state)
    project2_overlap_functions.print_board(game_state)

    while winner == 0:
        
        game_state, move, column_num = project2_overlap_functions.check_valid_input(game_state)
        game_state = project2_overlap_functions.check_valid_move(game_state, move, column_num)

        message = f"{move} {column_num}"
        send_message(connection, message)

        message_received = receive_message(connection)
        expected = "OKAY"

        winner = connectfour.winner(game_state)
        
        if message_received == expected:
            project2_overlap_functions.print_board(game_state)
        
            next_move = receive_message(connection)
            print("RED MOVE: " + next_move)

            try:
                move = next_move.split()[0]
                column_num = int(next_move.split()[1])
            except:
                close(connection)
                print("Received unexpected response from server. Connection closed.")
                winner = 3
                
            game_state = project2_overlap_functions.check_valid_move(game_state, move, column_num)
            project2_overlap_functions.print_board(game_state)

            message_received = receive_message(connection)
            expected = "READY"
            red = "WINNER_RED"
            yellow = "WINNER_YELLOW"

            if message_received == expected:
                print(message_received)
            else:
                winner = connectfour.winner(game_state)
                if winner == 1 and message_received == red:
                    close(connection)
                    print("YELLOW WON!")
                    winner
                elif winner == 2 and message_received == yellow:
                    close(connection)
                    print("RED WON!")
                else:
                    close(connection)
                    print("Received unexpected response from server. Connection closed.")
        else:
            close(connection)
            print("Received unexpected response from server. Connection closed.")
            winner = 3
            
