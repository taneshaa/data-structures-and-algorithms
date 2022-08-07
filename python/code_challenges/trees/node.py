# class method that enables you to create nodes to be used in your tree file
class Node:
    def __init__(self, value = None, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right