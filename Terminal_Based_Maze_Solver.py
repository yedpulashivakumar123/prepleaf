import random
import os
import heapq

# ANSI color codes (same as in your code)
# ...

# Maze class (unchanged)

# A* pathfinding algorithm
def heuristic(node, goal):
    x1, y1 = node
    x2, y2 = goal
    return abs(x1 - x2) + abs(y1 - y2)

def find_path_a_star(maze, start, end):
    open_list = [(0, start)]
    came_from = {}
    g_score = {cell: float('inf') for row in maze for cell in row}
    g_score[start] = 0

    while open_list:
        current_cost, current = heapq.heappop(open_list)

        if current == end:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            return path[::-1]

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            x, y = current
            neighbor = (x + dx, y + dy)

            if 0 <= neighbor[0] < len(maze) and 0 <= neighbor[1] < len(maze[0]) and maze[neighbor[0]][neighbor[1]] == OPEN_SPACE:
                tentative_g_score = g_score[current] + 1

                if tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score = tentative_g_score + heuristic(neighbor, end)
                    heapq.heappush(open_list, (f_score, neighbor))

    return None

# Main function
def main():
    print("Welcome to the Terminal-Based Maze Solver!")

    while True:
        size = int(input("Enter the size of the maze (n x n): "))
        wall_percentage = 0.25  # Adjust this to change the percentage of walls

        maze = Maze(size, wall_percentage)
        maze.print_maze()

        choice = input("Options:\n1. Print Path (A*)\n2. Generate Another Maze\n3. Exit\nEnter your choice: ")

        if choice == '1':
            start = (0, 0)
            end = (size - 1, size - 1)
            path = find_path_a_star(maze.maze, start, end)
            if path:
                for x, y in path:
                    maze.maze[x][y] = PATH
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
