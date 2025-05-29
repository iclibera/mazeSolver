# README.md
# A* Maze Solver

This repository provides a simple A* search–based maze solver in Python.

## Usage

1. **Install dependencies**
   ```bash
   pip install pyyaml
   ```

2. **Prepare a maze text file**
   - Start marker: `B`
   - End marker:   `E`
   - Wall char:    as configured (e.g. `#`, `+`)
   - Passage char: as configured (e.g. `.`, space)

3. **Configure**
   Edit `astar_config.yaml` to include entries for your maze files. Example:
   ```yaml
   41x41.txt:
     begin: 'B'
     end:   'E'
     wall:  '#'
     passage: '.'

   61x31.txt:
     begin: 'B'
     end:   'E'
     wall:  '#'
     passage: '.'

   81x81.txt:
     begin: 'B'
     end:   'E'
     wall:  '#'
     passage: '.'
   ```

4. **Run**
   ```bash
   python maze_solver.py <maze_file> [--config astar_config.yaml]
   ```
   Example:
   ```bash
   python maze_solver.py 41x41.txt
   ```

## Provided Mazes

- `41x41.txt` — 41×41 maze using `#` walls and `.` passages
- `61x31.txt` — 61×31 maze using `#` walls and `.` passages
- `81x81.txt` — 81×81 maze using `#` walls and `.` passages
- `plus_50x50_maze.txt` — 50×50 maze using `+` walls and spaces

Feel free to add your own maze files and update the YAML accordingly!
