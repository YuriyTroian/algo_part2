def read_input(file_path):
    with open(file_path, 'r') as f:
        height, width = map(int, f.readline().strip().split(','))
        start_x, start_y = map(int, f.readline().strip().split(','))
        replacement_color = f.readline().strip().strip("'\"")
        grid = []
        for _ in range(height):
            row = f.readline().strip()
            row = row.strip("[],").replace("'", "").replace('"', '').split(',')
            row = [cell.strip() for cell in row]
            grid.append(row)
    return grid, (start_x, start_y), replacement_color

def write_output(file_path, grid):
    with open(file_path, 'w') as f:
        for row in grid:
            f.write(str(row) + '\n')

def flood_fill(grid, start, replacement_color):
    rows, cols = len(grid), len(grid[0])
    x, y = start
    target_color = grid[x][y]

    if target_color == replacement_color:
        return grid

    def dfs(i, j):
        if 0 <= i < rows and 0 <= j < cols and grid[i][j] == target_color:
            grid[i][j] = replacement_color
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

    dfs(x, y)
    return grid

def main():
    grid, start, replacement_color = read_input('input.txt')
    result = flood_fill(grid, start, replacement_color)
    write_output('output.txt', result)

if __name__ == '__main__':
    main()
