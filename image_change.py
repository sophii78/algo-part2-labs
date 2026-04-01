import os

def flood_fill_bmp(pixels, width, height, start_x, start_y, new_color):
    target_color = pixels[start_y][start_x]
    if target_color == new_color:
        return pixels

    queue = [(start_x, start_y)]

    while queue:
        x, y = queue.pop(0)

        if pixels[y][x] == target_color:
            pixels[y][x] = new_color

            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < width and 0 <= ny < height:
                    if pixels[ny][nx] == target_color:
                        queue.append((nx, ny))
    return pixels

def main():
    filename = input("введіть назву файлу зображення: ")
    
    if not os.path.exists(filename):
        print("файл не знайдено")
        return

    with open(filename, "rb") as f:
        header = f.read(54)
        
        width = int.from_bytes(header[18:22], byteorder='little')
        height = int.from_bytes(header[22:26], byteorder='little')

        padding = (4 - (width * 3) % 4) % 4
        
        pixels = []
        for y in range(height):
            row = []
            for x in range(width):
                bgr = list(f.read(3))
                row.append(bgr)
            f.read(padding)
            pixels.append(row)

    pixels.reverse()

    print(f"зображення розміром {width}x{height} завантажено")
    try:
        start_x = int(input(f"введіть X (0-{width-1}): "))
        start_y = int(input(f"введіть Y (0-{height-1}): "))
        
        print("введіть новий колір:")
        r = int(input("Red: "))
        g = int(input("Green: "))
        b = int(input("Blue: "))
        new_color = [b, g, r]

        flood_fill_bmp(pixels, width, height, start_x, start_y, new_color)

        pixels.reverse()

        with open("result.bmp", "wb") as f:
            f.write(header)
            for row in pixels:
                for p in row:
                    f.write(bytes(p))
                f.write(b'\x00' * padding)
                
        print("готово, результат у файлі result.bmp")
        
    except (ValueError, IndexError):
        print("помилка вводу або координати поза межами")

if __name__ == "__main__":
    main()