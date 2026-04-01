import re

def flood_fill(grid, start_r, start_c, replacement_color):
    rows = len(grid)
    cols = len(grid[0])
    target_color = grid[start_r][start_c]

    if target_color == replacement_color:
        return grid

    queue = [(start_r, start_c)]
    head = 0

    grid[start_r][start_c] = replacement_color

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while head < len(queue):
        r, c = queue[head]
        head += 1

        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            if 0 <= nr < rows and 0 <= nc < cols:
                if grid[nr][nc] == target_color:
                    grid[nr][nc] = replacement_color
                    queue.append((nr, nc))

    return grid


def main():
    try:
        with open('input.txt', 'r', encoding='utf-8') as f:
            lines = f.readlines()

        if len(lines) < 4:
            return

        height, width = map(int, lines[0].strip().split(','))
        start_r, start_c = map(int, lines[1].strip().split(','))
        replacement_color = re.sub(r"['\"‘’]", "", lines[2].strip())

        grid = []
        for line in lines[3:]:
            row = re.findall(r'[A-Za-z]', line)
            if row:
                grid.append(row)

        if len(grid) != height or any(len(row) != width for row in grid):
            return

        result = flood_fill(grid, start_r, start_c, replacement_color)

        with open('output.txt', 'w', encoding='utf-8') as f:
            for row in result:
                f.write("[" + ", ".join(f"'{c}'" for c in row) + "]\n")

    except (FileNotFoundError, ValueError, IndexError):
        pass


if __name__ == "__main__":
    main()