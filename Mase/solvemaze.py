# Program for building and solving a maze.
from maze import Maze


# The main routine.
def main():
    maze = build_maze("mazefile5.txt")
    if maze.find_path():
        print("Path found....")
    else:
        print("Path not found....")
    print(maze)


def build_maze(filename):
    """Builds a maze based on a text format in the given file."""
    infile = open(filename, "r")

    # Read the size of the maze.
    nrows, ncols = read_value_pair(infile)
    maze = Maze(nrows, ncols)

    # Read the starting and exit positions.
    row, col = read_value_pair(infile)
    maze.set_start(row, col)
    row, col = read_value_pair(infile)
    maze.set_exit(row, col)

    # Read the maze itself.
    for row in range(nrows):
        line = infile.readline()
        for col in range(len(line)):
            if line[col] == "*":
                maze.set_wall(row, col)

    # Close the maze file and return the newly constructed maze.
    infile.close()

    return maze


def read_value_pair(infile):
    """Extracts an integer value pair from the given input file."""
    line = infile.readline()
    valA, valB = line.split()
    return int(valA), int(valB)


# Call the main routine to execute the program.
main()
