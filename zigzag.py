def zigzag(matrix):
    if not matrix or not matrix[0]:
        return []

    m = len(matrix)
    n = len(matrix[0])

    row, column = 0, 0
    result = []

    for _ in range(m * n):
        result.append(matrix[row][column])

        if (row + column) % 2 == 0:
            if column == n - 1:
                row += 1
            elif row == 0:
                column += 1
            else:
                row -= 1
                column += 1
        else:
            if row == m - 1:
                column += 1
            elif column == 0:
                row += 1
            else:
                row += 1
                column -= 1

    return result