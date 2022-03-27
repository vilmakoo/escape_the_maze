"""Algorithm for escaping a given maze"""

import sys

def starting_node():
    """Get starting node"""
    for i, row in enumerate(maze):
        for j, char in enumerate(row):
            if char == "^":
                start = [i, j]

    return start


def get_neighbours(node):
    """Get adjacent nodes to a given node"""
    neighbours = []

    def in_maze(node):
        """Check that node is inside the maze and not a block"""
        if node[0] in range(len(maze)) and node[1] in range(len(maze[0])):
            if maze[node[0]][node[1]] != "#":
                return True
        return False

    neighbours.append([node[0] - 1, node[1]])
    neighbours.append([node[0] + 1, node[1]])
    neighbours.append([node[0], node[1] - 1])
    neighbours.append([node[0], node[1] + 1])

    return list(filter(in_maze, neighbours))


def print_path(path_found, escape_path):
    """Print found escape path or a message if a path cannot be found
    to file 'result.txt'"""

    with open("result.txt", "w") as result_file:
        if not path_found:
            result_file.write("No route shorter than given length available for maze '{}'."
            .format(sys.argv[1]))
        else:
            result_file.write("Path of length {} found for maze '{}':\n\n"
            .format(len(escape_path), sys.argv[1]))

            def node_in_path(node):
                if node in escape_path:
                    return True
                return False

            for i, line in enumerate(maze):
                for j, char in enumerate(line):
                    if char == "^":
                        result_file.write("^") # print starting node
                    elif node_in_path([i ,j]):
                        result_file.write(".") # print '.' if node is in escape path
                    else:
                        result_file.write(char) # else print node as it is in the original maze
                result_file.write("\n")


def find_path(max_steps):
    """Find a path out of the maze using breadth first search"""

    visited = []
    queue = []
    start_node = starting_node()

    visited.append(start_node)
    queue.append([start_node])

    while queue:
        path = queue.pop(0) # path until this node
        node = path[-1] # node that is going to be examined now

        if len(path) > max_steps:
            print_path(False, [])
            break

        if maze[node[0]][node[1]] == "E":
            # exit found
            print_path(True, path)
            break

        # add neighbours to queue if they're not yet visited
        for neighbour in get_neighbours(node):
            if neighbour not in visited:
                visited.append(neighbour)
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)


if __name__ == "__main__":
    maze = list(map(list, open(sys.argv[1]).read().split("\n")))
    find_path(int(sys.argv[2]))
