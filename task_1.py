class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def insert(root: Node | None, key: int) -> Node:
    if root is None:
        return Node(key)
    else:
        if key < root.val:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)

    return root


def search_min(root: Node) -> int | None:
    if root is None:
        return root

    current = root
    while current.left is not None:
        current = current.left

    return current.val
    # or we can use recursion if we don't care to RAM
    # if root.left is None:
    #     return root.val
    # return search_min(root.left)


if __name__ == "__main__":
    root = Node(5)
    for i in [3, 2, 4, 7, 6, 8]:
        root = insert(root, i)

    result_min = search_min(root)
    print(f"RESULT: {result_min}")
