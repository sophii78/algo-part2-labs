import csv
import sys


def prim_mst(matrix, n):
    selected_node = [False] * n
    selected_node[0] = True

    total_weight = 0
    edges_count = 0

    print("\nпроцес вибору маршрутів:")

    while edges_count < n - 1:
        minimum = sys.maxsize
        u = 0
        v = 0

        for i in range(n):
            if selected_node[i]:
                for j in range(n):
                    if not selected_node[j] and matrix[i][j] > 0:
                        if minimum > matrix[i][j]:
                            minimum = matrix[i][j]
                            u = i
                            v = j

        if minimum == sys.maxsize:
            break

        selected_node[v] = True
        total_weight += minimum
        edges_count += 1
        print(f"з'єднано острів {u} та {v} (відстань: {minimum})")

    return total_weight


def main():
    filename = input("введіть назву файлу: ")

    try:
        matrix = []
        with open(filename, newline="", encoding="utf-8") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                matrix.append([float(x) for x in row])

        n = len(matrix)
        if n == 0:
            print("файл порожній")
            return

        if any(len(row) != n for row in matrix):
            print("матриця має бути квадратною (N x N)")
            return

        result = prim_mst(matrix, n)

        print("\n" + "=" * 40)
        print(f"мінімальна довжина кабелів для прокладання: {result}")
        print("=" * 40)

    except FileNotFoundError:
        print(f"помилка, файл '{filename}' не знайдено")
    except ValueError:
        print("помилка, файл містить некоректні дані (можуть бути тільки числа)")


if __name__ == "__main__":
    main()
