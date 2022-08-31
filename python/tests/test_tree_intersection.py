@pytest.fixture
def binary_tree():
    tree = BinaryTree()
    tree.root = Node(2)
    tree.root.left = Node(4)
    tree.root.right = Node(9)
    tree.root.left.right = Node(24)
    tree.root.left.right.left = Node(12)
    tree.root.left.right.right = Node(14)
    tree.root.right.right = Node(8)
    tree.root.right.right.left = Node(3)
    return tree

@pytest.fixture
def binary_tree2():
    tree2= BinaryTree()
    tree2.root = Node(2)
    tree2.root.left = Node(16)
    tree2.root.right = Node(13)
    tree2.root.left.right = Node(24)
    tree2.root.left.right.left = Node(4)
    tree2.root.left.right.right = Node(56)
    tree2.root.right.right = Node(20)
    tree2.root.right.right.left = Node(35)

    return tree2