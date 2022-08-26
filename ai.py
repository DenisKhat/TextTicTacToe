winningCombinations = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 5, 9], [3, 5, 7], [1, 4, 7], [2, 5, 8], [3, 6, 9]]


def optimalMove(board):  # A function to try and have the AI find the optimal move to move on the tic-tac-toe grid.
    points_of_board = list(calculatePointScore(index+1, board) for index, element in enumerate(board))
    # print(points_of_board)
    return points_of_board.index(max(points_of_board))


def calculatePointScore(tile, board):
    # print(tile)
    point_score = 0

    if board[tile-1] == " ":
        point_score += 1

        if tile == 5:
            point_score += 1

        for combination in winningCombinations:
            if tile in combination:
                # print(combination)
                keys_to_check = combination.copy()
                keys_to_check.remove(tile)
                # print(keys_to_check)
                # print(keys_to_check[0]-1)
                # print(board[keys_to_check[0]-1])
                if board[keys_to_check[0]-1] == board[keys_to_check[1]-1]:
                    match board[keys_to_check[0]-1]:
                        case "O":
                            # print("we gonna win tonight!")
                            point_score += 100  # arbitrarily big number that would beat any other scenario. wins game.
                        case "X":
                            # print("two x's")
                            point_score += 20  # small enough does not beat above case. stops opponent from winning.
                        case " ":
                            # print("empty column")
                            point_score += 1  # empty row is nice, but not nicer than any of the above.
    return point_score
