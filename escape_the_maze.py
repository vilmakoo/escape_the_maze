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
            print("No route shorter than given length available")
            break

        if maze[node[0]][node[1]] == "E":
            # exit found
            print(path)
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
