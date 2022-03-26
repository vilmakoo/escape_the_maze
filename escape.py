"""Algorithm for ecaping a given maze"""

import sys

def starting_point():
    """Get starting point"""
    for i, row in enumerate(maze):
        for j, char in enumerate(row):
            if char == "^":
                start = [i, j]

    return start


if __name__ == "__main__":
    maze = list(map(list, open(sys.argv[1]).read().split("\n")))
    print(starting_point())
