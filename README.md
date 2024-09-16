# ConnectFour
A Connect Four game that can be played two ways. First, using a python-shell-based implementation and the second, a networked version that uses a connection to a server.

First Version:
- a two-player game
- the user is able to specify the width and height of the board, and is asked to do so before playing
- the user then indicates whether they want to "DROP" or "POP" a disc and into which row
- if an input is invalid, the user is given specific instructions on how to fix it and examples of valid inputs
- after the first player gives a valid input, the second player does so. the players are differentiated using R and Y

Second Version:
- a one-player game against a server
- implemented using networks and sockets
- user gives inputs in the same way as the first version
