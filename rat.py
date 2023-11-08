import random
import os

# ANSI color codes
RED = '\033[91m'
BLUE = '\033[94m'
GREEN = '\033[92m'
ENDC = '\033[0m'

# Constants
WALL = RED + '▓' + ENDC
OPEN_SPACE = BLUE + '◌' + ENDC
START = GREEN + 'S' + ENDC
END = GREEN + 'E' + ENDC
PATH = GREEN + '◍' + ENDC

# Maze class
class Maze:
    def __init__(self, size, wall_percentage):
        self.size = size
        self.wall_percentage = wall_percentage
        self.maze = self.generate_maze()

    def generate_maze(self):
        maze = [[WALL if random.random() < self.wall_percentage else OPEN_SPACE for _ in range(self.size)] for _ in range(self.size)]
        maze[0][0] = START
        maze[self.size - 1][self.size - 1] = END
        return maze

    def print_maze(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        for row in self.maze:
            print(' '.join(row))

# DFS pathfinding algorithm
def find_path(maze, x, y):
    if x < 0 or x >= len(maze) or y < 0 or y >= len(maze):
        return False

    if maze[x][y] == END:
        return True

    if maze[x][y] != OPEN_SPACE:
        return False

    maze[x][y] = PATH

    if find_path(maze, x + 1, y) or find_path(maze, x - 1, y) or find_path(maze, x, y + 1) or find_path(maze, x, y - 1):
        return True

    maze[x][y] = OPEN_SPACE
    return False

# Main function
def main():
    print("Welcome to the Terminal-Based Maze Solver!")

    while True:
        size = int(input("Enter the size of the maze (n x n): "))
        wall_percentage = 0.25  # Adjust this to change the percentage of walls

        maze = Maze(size, wall_percentage)
        maze.print_maze()

        choice = input("Options:\n1. Print Path\n2. Generate Another Maze\n3. Exit\nEnter your choice: ")

        if choice == '1':
            maze_copy = [row[:] for row in maze.maze]  # Create a copy of the maze
            if find_path(maze_copy, 0, 0):
                maze.print_maze()
            else:
                print("No path found.")
        elif choice == '2':
            continue
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
