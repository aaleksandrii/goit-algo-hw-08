class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def insert(root: Node, key: int) -> Node:
    if root is None:
        return Node(key)
    else:
        if key < root.val:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)

    return root


def sum_tree(root: Node | None) -> int:
    if root is None:
        return 0
    return root.val + sum_tree(root.left) + sum_tree(root.right)


if __name__ == "__main__":
    root = Node(5)
    for i in [3, 2, 4, 7, 6, 8]:
        root = insert(root, i)

    sum_values = sum_tree(root)
    print(f"RESULT: {sum_values}")
