from trees.trees import BinaryTree
from trees.node import Node
from trees.trees import BinarySearchTree
import pytest

def test_bt_empty_tree():
    bt = BinaryTree()
    actual = bt.root
    expected = None
    assert actual == expected
def test_bt_single_root():
    bt = BinaryTree(Node())
    assert isinstance(bt.root, Node)
    assert bt.root.value is None
# The isinstance() function returns True if the specified object is of the specified type, otherwise False
def test_bt_add_left():
    apple = Node('apple')
    pear = Node('pear')
    orange = Node('orange')
    # created instances of fruits to be used to create the tree
    bt = BinaryTree(apple)
    # instance of binary tree class and setting apple as the root
    apple.left = pear
    # the left of apple in the tree is pear
    apple.right = orange
    # the right of apple in the tree is orange
    assert apple.left == bt.root.left
    # assert that the left of apple (pear) is equal to the instance of BinaryTree(apple).left = pear
    assert apple.right == bt.root.right
     # assert that the right of apple (orange) is equal to the instance of BinaryTree(apple).right = orange
#         apple
#        /    \
#     pear     orange
def test_bt_pre_order():
    apple = Node('apple')
    pear = Node('pear')
    orange = Node('orange')
    bt = BinaryTree(apple)
    apple.left = pear
    apple.right = orange
    assert apple.left == bt.root.left
    assert apple.right == orange
    order_list = bt.pre_order()
    # creating a variable that is an instance of our preorder method
    assert order_list == ['apple', 'pear', 'orange']
    # asserting that the preorder method is equal to the array of fruits in that same order.
def test_bt_in_order():
    apple = Node('apple')
    pear = Node('pear')
    orange = Node('orange')
    bt = BinaryTree(pear)
    pear.left = orange
    pear.right = apple
    assert pear.left == bt.root.left
    assert pear.right == apple
    order_list = bt.in_order()
    assert order_list == ['orange', 'pear', 'apple']
def test_bt_post_order():
    apple = Node('apple')
    pear = Node('pear')
    orange = Node('orange')
    bt = BinaryTree(pear)
    pear.left = orange
    pear.right = apple
    assert pear.left == bt.root.left
    assert pear.right == apple
    order_list = bt.post_order()
    assert order_list == ['orange', 'apple', 'pear']
def test_bt_search_tree_left():
    root = Node('orange')
    bt = BinarySearchTree(root)
    bt.add('apple')
    actual = bt.pre_order()
    expected = ['orange', 'apple']
    assert actual == expected
def test_bt_search_tree_left_and_right():
    root = Node('orange')
    bt = BinarySearchTree(root)
    bt.add('apple')
    bt.add('pear')
    actual = bt.pre_order()
    expected = ['orange', 'apple', 'pear']
    assert actual == expected
def test_bt_search_tree_contains_true():
    root = Node('orange')
    bt = BinarySearchTree(root)
    bt.add('apple')
    bt.add('pear')
    bt.add('banana')
    actual = bt.contains('pear')
    expected = True
    assert actual == expected
def test_bt_search_tree_contains_false():
    root = Node('orange')
    bt = BinarySearchTree(root)
    bt.add('apple')
    bt.add('pear')
    bt.add('orange')
    actual = bt.contains('strawberry')
    expected = False
    assert actual == expected
def test_bt_search_tree_empty_false():
    bt = BinarySearchTree()
    actual = bt.contains('orange')
    expected = False
    assert actual == expected