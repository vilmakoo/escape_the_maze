"""Algorithm for escaping a given maze"""

import sys

def starting_node():
    """Get starting node"""
    for i, row in enumerate(MAZE):
        for j, char in enumerate(row):
            if char == "^":
                start = [i, j]

    return start


def get_neighbours(node):
    """Get adjacent nodes to a given node"""
    neighbours = []

    def in_maze(node):
        """Check that node is inside the maze and not a block"""
        if node[0] in range(len(MAZE)) and node[1] in range(len(MAZE[0])):
            if MAZE[node[0]][node[1]] != "#":
                return True
        return False

    neighbours.append([node[0] - 1, node[1]])
    neighbours.append([node[0] + 1, node[1]])
    neighbours.append([node[0], node[1] - 1])
    neighbours.append([node[0], node[1] + 1])

    return list(filter(in_maze, neighbours))


def print_path_not_available():
    """Print a message if path shorter than the given length is not found to file 'result.txt'"""
    with open("result.txt", "w") as result_file:
        result_file.write("No path shorter than given length available for '{}'."
                          .format(INPUT_FILE))



def print_path(escape_path):
    """Print found escape path to file 'result.txt'"""

    with open("result.txt", "w") as result_file:
        result_file.write("Path of length {} found for maze '{}' \
('|' visualizes the path):\n\n".format(len(escape_path), INPUT_FILE))

        for i, line in enumerate(MAZE):
            for j, char in enumerate(line):
                if char == "^":
                    result_file.write("^") # print starting node
                elif [i, j] in escape_path:
                    result_file.write("|") # print '|' if node is in escape path
                else:
                    result_file.write(char) # else print node as it is in the original maze
            result_file.write("\n")


def find_path(max_steps):
    """Find a path out of the maze using a breadth-first search algorithm"""

    visited = []
    queue = []
    start_node = starting_node()

    visited.append(start_node)
    queue.append([start_node])

    while queue:
        path = queue.pop(0) # path until this node
        node = path[-1] # node that is going to be examined now

        if len(path) > max_steps:
            print_path_not_available()
            break

        if MAZE[node[0]][node[1]] == "E":
            # exit found
            print_path(path)
            break

        # add neighbours to queue if they're not yet visited
        for neighbour in get_neighbours(node):
            if neighbour not in visited:
                visited.append(neighbour)
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)


if __name__ == "__main__":
    # the three variables under here shouldn't maybe be globals but are for now
    INPUT_FILE = sys.argv[1]
    MAZE = list(map(list, open(INPUT_FILE).read().split("\n")))
    MAX_LENGTH = int(sys.argv[2])
    find_path(MAX_LENGTH)
