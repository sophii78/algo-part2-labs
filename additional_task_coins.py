from zigzag import zigzag


def main():
    m = int(input("Введіть кількість рядків (m): "))
    n = int(input("Введіть кількість стовпців (n): "))

    print("Введіть матрицю:")

    matrix = []
    for i in range(m):
        row = list(map(int, input().split()))
        matrix.append(row)

    k = int(input("Введіть кількість кроків (k): "))

    path = zigzag(matrix)

    k = min(k, len(path))

    coins = sum(path[:k])

    print("Зібрано монет:", coins)


if __name__ == "__main__":
    main()
