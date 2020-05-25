import numpy as np
def solution(map):
    board = np.array(distance_to_src(map)) + np.array(distance_to_dest(map)) - 1
    return np.amin(board)


def distance_to_dest(map):
    """
    Compute the cost of moving from any node in the map
    to the destination node

    :param Maze map
    """
    width = len(map[0])
    height = len(map)
    end = (height - 1, width - 1)
    return compute_cost(map, end)


def distance_to_src(map):
    """
    Compute the cost of moving to all the nodes in the map
    from the starting point
        :param Maze map
    """
    # node = (row, col)
    start = (0, 0)
    return compute_cost(map, start)

def compute_cost(map, start):
    width = len(map[0])
    height = len(map)

    # offsets for neighbours of any node
    # south, north, west, east
    neighbors = [(-1, 0), (1, 0), (0, -1), (0, 1)] #row, col

    max = 20*20

    # blank board to store g or h values
    board = [[max for i in range(0, width)] for j in range(0, height)]
    start_row = start[0]
    start_col = start[1]

    # starting point
    board[start_row][start_col] = 1

    # queue to store coordinates of nodes to evaluate
    queue = []

    # begin by evaluating from the start node
    queue.append(start)

    while queue:
        # get current node
        current = queue.pop(0)
        cur_col = current[1]
        cur_row = current[0]

        # get cost of moving to the neighbours of the current node
        for offset_col, offset_row in neighbors:
            new_col = cur_col + offset_col
            new_row = cur_row + offset_row

            # proceed only if coordinates of neighbours are within the map
            if 0 <= new_col < width and 0 <= new_row < height:
                # if the cost of the neighbor node is already evaluated, then skip
                # otherwise, evaluate its cost. This step also evaluates cost of
                # entering impassable nodes sitting right next to passable nodes
                if board[new_row][new_col] == max:
                    # Cost of reaching this neighbor node is the cost of reaching its parent + 1
                    board[new_row][new_col] = board[cur_row][cur_col] + 1

                    # if this neighbor node was an impassable wall,
                    # then don't add it to the evaluation queue.
                    if map[new_row][new_col] == 1:
                        continue
                    else:
                        queue.append((new_row, new_col))
    return board

if __name__ == "__main__":
    # map = [[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]
    # print_board(map)
    # print(solution(map))

    map = [[0, 1, 0, 0, 0, 0],
           [0, 1, 0, 1, 1, 0],
           [0, 1, 0, 0, 1, 0],
           [0, 1, 0, 1, 1, 0],
           [0, 1, 0, 1, 1, 0],
           [0, 0, 0, 1, 1, 0]]


    print(solution(map))

    map = [
        [0, 1, 1, 1, 1],
        [0, 1, 1, 1, 1],
        [0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0]
    ]

    print(solution(map))