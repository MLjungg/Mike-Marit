def check_if_one_loop(board, previous_coordinate, current_coordinate): #In the first run previous_coordinate=None.
    start_coordinate = board.index(2)

        if row > 0:
            if board[row - 1][col] == 1 or board[row - 1][col] == 2:
                if board[row - 1][col] != previous_coordinate:
                    previous_coordinate = current_coordinate
                    current_coordinate = board[row - 1][col]
                    if current_coordinate == start_coordinate:
                        print ('loop is done')
                    else:
                        check_if_one_loop(previous_coordinate, current_coordinate)

        if row < size - 1 and board[row + 1][col] == 1:
            if board[row - 1][col] == 1 or board[row - 1][col] == 2:
                if board[row - 1][col] != previous_coordinate:
                    previous_coordinate = current_coordinate
                    current_coordinate = board[row - 1][col]
                    if current_coordinate == start_coordinate:
                        print ('loop is done')
                    else:
                        check_if_one_loop(previous_coordinate, current_coordinate)

        if board[row][col - 1] == 1 and col > 0:
            if board[row - 1][col] == 1 or board[row - 1][col] == 2:
                if board[row - 1][col] != previous_coordinate:
                    previous_coordinate = current_coordinate
                    current_coordinate = board[row - 1][col]
                    if current_coordinate == start_coordinate:
                        print ('loop is done')
                    else:
                        check_if_one_loop(previous_coordinate, current_coordinate)

        if col < size - 1 and board[row][col + 1] == 1:
            if board[row - 1][col] == 1 or board[row - 1][col] == 2:
                if board[row - 1][col] != previous_coordinate:
                    previous_coordinate = current_coordinate
                    current_coordinate = board[row - 1][col]
                    if current_coordinate == start_coordinate:
                        print ('loop is done')
                    else:
                        check_if_one_loop(previous_coordinate, current_coordinate)
