"""Algorithm for ecaping a given maze"""

import sys

def starting_point():
    """Get starting point"""
    for i, row in enumerate(maze):
        for j, char in enumerate(row):
            if char == "^":
                start = [i, j]

    return start


def get_neighbours(node):
    neighbours = []

    def in_maze(node):
        if node[0] in range(len(maze)) and node[1] in range(len(maze[0])):
            if maze[node[0]][node[1]] != "#":
                return True
        return False

    neighbours.append([node[0] - 1, node[1]])
    neighbours.append([node[0] + 1, node[1]])
    neighbours.append([node[0], node[1] - 1])
    neighbours.append([node[0], node[1] + 1])

    return list(filter(in_maze, neighbours))


visited = []
queue = []

def escape(visited, starting_point, max_steps):
    visited.append(starting_point)
    queue.append([starting_point])

    while queue:
        path = queue.pop(0)
        node = path[-1]

        if len(path) > max_steps:
            print("No possible route shorter than given length available")
            break

        if maze[node[0]][node[1]] == "E":
            print(path)
            break

        for neighbour in get_neighbours(node):
            if neighbour not in visited:
                visited.append(neighbour)
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)



if __name__ == "__main__":
    maze = list(map(list, open(sys.argv[1]).read().split("\n")))
    escape(visited, starting_point(), int(sys.argv[2]))



# TODO:
# refaktoroi
# kommentoi
