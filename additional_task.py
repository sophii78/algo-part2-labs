import os

class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

def find_successor(tree: BinaryTree, node: BinaryTree) -> BinaryTree:
    if node is None:
        return None

    if node.right:
        current = node.right
        while current.left:
            current = current.left
        return current

    current = node
    while current.parent and current.parent.right == current:
        current = current.parent

    return current.parent

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def print_special_tree(root):
    if not root: 
        print("Дерево порожнє")
        return
    grid = {}

    def build(node, y, x, direction):
        if not node: return
        val_str = str(node.value)
        grid[(y, x)] = val_str
        v_gap = 2

        if node.left:
            if direction == "root":
                grid[(y, x - 3)] = "-"
                build(node.left, y, x - 7, "left_axis")
            elif direction == "left_axis" or direction == "down":
                grid[(y + 1, x - 1)] = "/"
                build(node.left, y + v_gap, x - 2, "down")
            elif direction == "up_axis":
                grid[(y, x - 3)] = "-"
                build(node.left, y, x - 6, "up_axis")

        if node.right:
            if direction == "root":
                grid[(y, x + 3)] = "-"
                build(node.right, y, x + 7, "right_axis")
            elif direction == "left_axis":
                grid[(y - 1, x - 1)] = "\\"
                build(node.right, y - v_gap, x - 2, "up_axis")
            elif direction == "right_axis" or direction == "up":
                grid[(y - 1, x + 1)] = "/"
                build(node.right, y - v_gap, x + 2, "up")

    build(root, 10, 50, "root")
    
    unique_rows = quick_sort(list(set(r for r, _ in grid.keys())))

    min_c = min(c for _, c in grid.keys())
    max_c = max(c + len(v) for (_, c), v in grid.items())

    for r in unique_rows:
        line_length = int(max_c - min_c + 10)
        line = [" "] * line_length
        for (row, col), val in grid.items():
            if row == r:
                for i, char in enumerate(val):
                    pos = int(col - min_c + i)
                    if 0 <= pos < line_length:
                        line[pos] = char
        print("".join(line).rstrip())

def build_tree_from_list(values):
    if not values:
        return None, []

    nodes = []
    for v in values:
        if v.lower() == "none":
            nodes.append(None)
        else:
            nodes.append(BinaryTree(int(v)))
            
    child_index = 1
    for i in range(len(nodes)):
        if nodes[i] is not None:
            if child_index < len(nodes):
                nodes[i].left = nodes[child_index]
                if nodes[child_index]:
                    nodes[child_index].parent = nodes[i]
                child_index += 1

            if child_index < len(nodes):
                nodes[i].right = nodes[child_index]
                if nodes[child_index]:
                    nodes[child_index].parent = nodes[i]
                child_index += 1
    return nodes[0], [n for n in nodes if n is not None]


print("1. Зчитати з файлу\n2. Ввести значення вручну")
choice = input("Ваш вибір: ")

values = []
if choice == "1":
    filename = input("Файл: ")
    if os.path.exists(filename):
        with open(filename, "r") as f: values = f.read().split()
elif choice == "2":
    values = input("Введіть вузли через пробіл: ").split()

if values:
    root, all_nodes = build_tree_from_list(values)
    print("\nВаше дерево:")
    print_special_tree(root)
    
    try:
        val_to_find = int(input("\nВведіть значення вузла для пошуку наступника: "))
        target_node = next((n for n in all_nodes if n.value == val_to_find), None)
        
        if target_node:
            successor = find_successor(root, target_node)
            if successor:
                print(f"Наступник для {val_to_find} це {successor.value}")
            else:
                print(f"у вузла {val_to_find} нема наступника")
        else:
            print("Помилка: вузол не знайдено")
    except ValueError:
        print("Помилка: введіть число")