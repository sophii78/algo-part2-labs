class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority
        self.left = None
        self.right = None
        self.height = 1

class AVLPriorityQueue:
    def __init__(self):
        self.root = None

    def height(self, node):
        return node.height if node else 0

    def get_balance(self, node):
        return self.height(node.left) - self.height(node.right) if node else 0

    def right_rotate(self, y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        y.height = 1 + max(self.height(y.left), self.height(y.right))
        x.height = 1 + max(self.height(x.left), self.height(x.right))
        return x

    def left_rotate(self, x):
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        x.height = 1 + max(self.height(x.left), self.height(x.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))
        return y

    def insert_node(self, node, value, priority):
        if not node:
            return Node(value, priority)

        if priority >= node.priority:
            node.left = self.insert_node(node.left, value, priority)
        else:
            node.right = self.insert_node(node.right, value, priority)

        node.height = 1 + max(self.height(node.left), self.height(node.right))
        balance = self.get_balance(node)

        if balance > 1 and priority >= node.left.priority:
            return self.right_rotate(node)

        if balance < -1 and priority < node.right.priority:
            return self.left_rotate(node)

        if balance > 1 and priority < node.left.priority:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)

        if balance < -1 and priority >= node.right.priority:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return node

    def insert(self, value, priority):
        self.root = self.insert_node(self.root, value, priority)

    def get_max_node(self, node):
        current = node
        while current and current.left:
            current = current.left
        return current

    def delete_node(self, node, priority):
        if not node:
            return node

        if priority > node.priority:
            node.left = self.delete_node(node.left, priority)
        elif priority < node.priority:
            node.right = self.delete_node(node.right, priority)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left

            temp = self.get_max_node(node.left)
            node.value = temp.value
            node.priority = temp.priority
            node.left = self.delete_node(node.left, temp.priority)

        if not node:
            return node

        node.height = 1 + max(self.height(node.left), self.height(node.right))
        balance = self.get_balance(node)

        if balance > 1 and self.get_balance(node.left) >= 0:
            return self.right_rotate(node)

        if balance > 1 and self.get_balance(node.left) < 0:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)

        if balance < -1 and self.get_balance(node.right) <= 0:
            return self.left_rotate(node)

        if balance < -1 and self.get_balance(node.right) > 0:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return node

    def pop(self):
        if not self.root:
            return None

        max_node = self.get_max_node(self.root)
        value, priority = max_node.value, max_node.priority
        self.root = self.delete_node(self.root, priority)
        return value, priority

    def peek(self):
        if not self.root:
            return None
        max_node = self.get_max_node(self.root)
        return max_node.value, max_node.priority

    def inorder(self, node):
        if not node:
            return
        self.inorder(node.left)
        print(f"Значення: {node.value}, Пріоритет: {node.priority}")
        self.inorder(node.right)

    def display(self):
        if not self.root:
            print("Черга порожня")
        else:
            self.inorder(self.root)

def input_from_keyboard(queue):
    try:
        n = int(input("Скільки елементів додати: "))
        for _ in range(n):
            value = input("Введіть значення: ")
            priority = int(input("Введіть пріоритет: "))
            queue.insert(value, priority)
    except ValueError:
        print("Помилка введення")

def input_from_file(queue, filename):
    try:
        with open(filename, "r") as f:
            for line in f:
                parts = line.split()
                if len(parts) >= 2:
                    queue.insert(parts[0], int(parts[1]))
    except (FileNotFoundError, ValueError):
        print("Помилка зчитування файлу")

def menu(queue):
    while True:
        print("\n1. Вставка елемента")
        print("2. Видалення елемента з найвищим пріоритетом")
        print("3. Перегляд черги")
        print("4. Вихід")

        choice = input("Оберіть дію: ")

        if choice == "1":
            value = input("Введіть значення: ")
            try:
                priority = int(input("Введіть пріоритет: "))
                queue.insert(value, priority)
                print("Елемент додано")
            except ValueError:
                print("Пріоритет має бути числом")

        elif choice == "2":
            result = queue.pop()
            if result:
                print("Видалено:", result)
            else:
                print("Черга порожня")

        elif choice == "3":
            print("\nПоточна черга:")
            queue.display()
            max_elem = queue.peek()
            if max_elem:
                print("Найвищий пріоритет:", max_elem)
        
        elif choice == "4":
            break
        else:
            print("Неправильний вибір")

if __name__ == "__main__":
    pq = AVLPriorityQueue()

    print("Виберіть спосіб введення:")
    print("1 - клавіатурою")
    print("2 - з файлу")

    choice = input("Ваш вибір: ")

    if choice == "1":
        input_from_keyboard(pq)
    elif choice == "2":
        filename = input("Введіть назву файлу: ")
        input_from_file(pq, filename)
    
    menu(pq)