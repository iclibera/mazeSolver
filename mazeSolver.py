# maze_solver.py
# A* Maze Solver
# This script loads a maze description and configuration, applies the A* search algorithm
# to find the shortest path from the start ('B') to the end ('E'), and prints the solved maze.

import yaml
import heapq
import argparse
import sys
import os


def load_config(config_path):
    """
    Load maze parameters from a YAML configuration file.
    The YAML maps maze filenames (or keys) to their start/end and wall/passage characters.
    Returns the dictionary of configurations.
    """
    with open(config_path, 'r') as f:
        config = yaml.safe_load(f)
    return config


class Maze:
    """
    Represents a maze loaded from a text file using given parameters.
    Provides methods to parse the maze and query neighbors.
    """

    def __init__(self, maze_path, params):
        self.grid = []           # 2D list of characters
        self.start = None        # (row, col) coordinate of 'B'
        self.end = None          # (row, col) coordinate of 'E'
        self.params = params     # dictionary with 'begin', 'end', 'wall', 'passage'
        self.load_maze(maze_path)

    def load_maze(self, path):
        """
        Read the maze file into grid, identify start and end positions.
        """
        with open(path, 'r') as f:
            for r, line in enumerate(f):
                row = list(line.rstrip('\n'))
                for c, ch in enumerate(row):
                    if ch == self.params['begin']:
                        self.start = (r, c)
                    elif ch == self.params['end']:
                        self.end = (r, c)
                self.grid.append(row)
        if self.start is None or self.end is None:
            raise ValueError(f"Maze must have start '{self.params['begin']}' and end '{self.params['end']}'")
        self.height = len(self.grid)
        self.width = len(self.grid[0])

    def in_bounds(self, pos):
        """
        Check if a position is within grid bounds.
        """
        r, c = pos
        return 0 <= r < self.height and 0 <= c < self.width

    def passable(self, pos):
        """
        Check if a position is not a wall.
        """
        r, c = pos
        return self.grid[r][c] != self.params['wall']

    def neighbors(self, pos):
        """
        Generate valid neighbor positions (4-directional).
        """
        r, c = pos
        for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
            nbr = (r + dr, c + dc)
            if self.in_bounds(nbr) and self.passable(nbr):
                yield nbr

    def mark_path(self, path):
        """
        Overlay the path on the grid using a marker (e.g., 'P'), except start/end.
        """
        for r, c in path:
            if (r, c) not in (self.start, self.end):
                self.grid[r][c] = 'P'

    def display(self):
        """
        Print the maze grid to stdout.
        """
        for row in self.grid:
            print(''.join(row))


def heuristic(a, b):
    """
    Heuristic function for A* (Manhattan distance).
    """
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def a_star_search(maze):
    """
    Perform A* search on the maze from start to end.
    Returns the path as a list of positions or None if no path.
    """
    start = maze.start
    goal = maze.end

    # The frontier is a priority queue of (f_score, count, position)
    frontier = []
    heapq.heappush(frontier, (0, 0, start))

    came_from = {start: None}   # track parent of each visited node
    g_score = {start: 0}        # cost from start to the node

    count = 0  # tie-breaker for heap entries

    while frontier:
        current_f, _, current = heapq.heappop(frontier)

        # If we reached the goal, reconstruct the path
        if current == goal:
            path = []
            while current is not None:
                path.append(current)
                current = came_from[current]
            path.reverse()
            return path

        # Explore neighbors
        for nbr in maze.neighbors(current):
            tentative_g = g_score[current] + 1
            if nbr not in g_score or tentative_g < g_score[nbr]:
                came_from[nbr] = current
                g_score[nbr] = tentative_g
                f_score = tentative_g + heuristic(nbr, goal)
                count += 1
                heapq.heappush(frontier, (f_score, count, nbr))

    # No path found
    return None


def main():
    """
    Main function to parse arguments, load config and maze, find path, and display result.
    """
    parser = argparse.ArgumentParser(description='Solve a maze using A* search.')
    parser.add_argument('maze_file', help='Path to the maze text file')
    parser.add_argument('--config', default='config/astar_config.yaml',
                        help='Path to the YAML config file for maze parameters')
    args = parser.parse_args()

    # Load configuration and select params for this maze
    config = load_config(args.config)
    key = os.path.splitext(os.path.basename(args.maze_file))[0]
    if key not in config:
        print(f"No configuration for '{key}' in {args.config}")
        sys.exit(1)
    params = config[key]

    # Initialize maze and solve
    maze = Maze(args.maze_file, params)
    path = a_star_search(maze)
    if path is None:
        print("No path found from start to end.")
        sys.exit(1)

    print(f"Found path of length {len(path)-1} steps.")
    maze.mark_path(path)
    maze.display()

if __name__ == '__main__':
    main()