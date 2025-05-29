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
   - Wall char:    as configured (e.g. `o`, `+`)
   - Passage char: as configured (e.g. `.`, space)

3. **Configure**
   Edit `config/astar_config.yaml` to include entries for your maze files. Example:
   ```yaml
   41x41.txt:
     begin: 'B'
     end:   'E'
     wall:  '+'
     passage: ' '

   61x31.txt:
     begin: 'B'
     end:   'E'
     wall:  'o'
     passage: '*'

   81x81.txt:
     begin: 'B'
     end:   'E'
     wall:  '.'
     passage: 'x'
   ```

4. **Run**
   ```bash
   python3 maze_solver.py <maze_file> [--config config/astar_config.yaml]
   ```
   Example:
   ```bash
   python3 maze_solver.py maze/41x41.txt
   ```

## Provided Mazes

- `41x41.txt` — 41×41 maze using `+` walls and ` ` passages
- `61x31.txt` — 61×31 maze using `o` walls and `*` passages
- `81x81.txt` — 81×81 maze using `.` walls and `x` passages

## Example Solution (41x41.txt)
<img width="364" alt="Screenshot 2025-05-29 at 23 58 54" src="https://github.com/user-attachments/assets/370ad560-c00d-466c-91fe-3292e2be55bb" />

Feel free to add your own maze files and update the YAML accordingly!
