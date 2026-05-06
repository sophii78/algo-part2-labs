def execute_traversal():
    with open("ijones.in", "r") as in_file:
        raw_data = in_file.read().split()

    if not raw_data:
        return

    width_dim = int(raw_data[0])
    height_dim = int(raw_data[1])
    symbol_grid = raw_data[2:]

    prev_routes = [1] * height_dim
    global_letter_sum = [0] * 26

    for y_pos in range(height_dim):
        global_letter_sum[ord(symbol_grid[y_pos][0]) - 97] += 1

    for x_pos in range(1, width_dim):
        curr_routes = [0] * height_dim
        local_letter_sum = [0] * 26

        for y_pos in range(height_dim):
            curr_char = symbol_grid[y_pos][x_pos]
            past_char = symbol_grid[y_pos][x_pos - 1]
            char_id = ord(curr_char) - 97

            ways_to_current = global_letter_sum[char_id]
            if curr_char != past_char:
                ways_to_current += prev_routes[y_pos]

            curr_routes[y_pos] = ways_to_current
            local_letter_sum[char_id] += ways_to_current

        for i in range(26):
            global_letter_sum[i] += local_letter_sum[i]

        prev_routes = curr_routes

    if height_dim == 1:
        final_result = prev_routes[0]
    else:
        final_result = prev_routes[0] + prev_routes[height_dim - 1]

    with open("ijones.out", "w") as out_file:
        out_file.write(str(final_result))


if __name__ == "__main__":
    execute_traversal()
