def print_board(board):
    """
    Print the sudoku board with grid lines for each mini box
    :param board: Sudoku board to print
    """
    rowlength = None

    for row in range(len(board)):
        output_str = ""

        if row !=0 and rowlength is not None:
            print('-' * rowlength)

        for col in range(len(board[0])):

            if col != 0 :
                output_str += "|"

            if col == (len(board[0]) - 1):
                output_str += str(board[row][col])
            else:
                output_str += str(board[row][col]) + " "

        if rowlength is None:
            rowlength = len(output_str) - output_str.count("\n")

        print(output_str)

        pass




def solution(map):
    """
    Solves a maze starting from top left node to bottom right node using BFS with recursion
    :param map: maze map in the form of list of lists, where 0 is a free path and 1 is an obstacle
    :return: Count of nodes to traverse to reach desination
    """
    width = len(map[0])
    height = len(map)
    # Update x, y here to change starting point
    x = 0
    y = 0
    SolveMaze.count = 0
    SolveMaze().findnumnodes(map, width, height, x, y)
    return SolveMaze.count

class SolveMaze:
    count = 0


    def findnumnodes(self, map, width, height, x, y):
        """
        Finds solution for the given maze using recursion
        :param map: maze board to solve
        :return: Returns step count if a valid solution was found.
        Returns -1 if no solution was found.
        """

        # Update this condition to change destination node
        if y == width - 1 and x == height - 1:
            return True

        if map[x][y] == 2:
            return False


        else:
            map[x][y] = 2

            # check south
            if x < height - 1 and map[x + 1][y] == 0 :
                    SolveMaze.count += 1
                    if self.findnumnodes(map, width, height, x + 1, y):
                        return True
            # check east
            if y < width - 1 and map[x][y + 1] == 0 :
                    SolveMaze.count += 1
                    if self.findnumnodes(map, width, height, x, y+1):
                        return True
            # check west
            if y >= 1 and map[x][y - 1] == 0 :
                    SolveMaze.count += 1
                    if self.findnumnodes(map, width, height, x, y-1):
                        return True
            # check north
            if x >= 1 and map[x - 1][y] == 0 :
                    SolveMaze.count += 1
                    if self.findnumnodes(map, width, height, x - 1, y):
                        return True


            map[x][y] = 1
            return False





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
    print_board(map)
    # print(solutionmine(map))

    print(solution(map))




