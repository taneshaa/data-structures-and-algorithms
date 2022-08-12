from data_structures.binary_tree import BinaryTree


# creating a class called BinarySearch Tree
class BinarySearchTree(BinaryTree):
    # create a function called add that uses recursion (function within a function)
    # Python saves the state of the executing instance on a stack so the recursive call can run.
    def add(self, value):
        new_node = Node(value)

        # create function call add that takes in a value (also passes in self to refer to the dunder init we used in the Binary Tree class)
        def walk(root):
            if root is None:
                self.root = new_node
                return
            # create a function called walk within add that takes in a root as a parameter.
            if new_node.value < root.value:
                # if the targeted value is less than the current root, walk to the left. If you have a targeted value, but there isn't a root.left, you would just return the current Node.
                if root.left is None:
                    root.left = new_node
                else:
                    walk(root.left)
            # if the targeted value is greater than the current root, walk to the right. If you have a targeted value, but there isn't a root.right, you would just return the current Node (which would be None).
            elif new_node.value > root.value:
                if root.right is None:
                    root.right = new_node
                else:
                    walk(root.right)

        walk(self.root)

    def contains(self):
        def walk(root):
            if root is None:
                return False
            elif root.value == value:
                return False
            elif value < root.value:
                return walk(root.left)
            else:
                return walk(root.right)

        return walk(self.root)
