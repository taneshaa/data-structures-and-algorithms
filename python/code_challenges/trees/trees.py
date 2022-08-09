# from trees import Node

class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def pre_order(self):
        # root > left > right
        #           A
        #       /       \
        #      B         C
        #   /    \     /
        #  D     E    F
        # callstacks job is to find everything that needs to be operated on, operate on it, then delete it
        # call stack: A, C,
        # Expect A B D E C F

        # empty list for values
        tree_values = []
        # tree_values = [A, B]
        def walk(root, values):
            if root is None:
                return
            if root:
      # append the current root's value to the tree_values array
              tree_values.append(root.value)
        # then walk to the left of the root
              walk(root.left, values)
        # then if walk to the right of the tree
              walk(root.right, values)
      #walk back up to the root if all values have been inserted into the call stack
            walk(self.root, tree_values)
      # finally return the array to get the expected output
            return tree_values

    def in_order(self):
     # left > root > right
    # walking down to the most left node, then append that value to the array, then walk to the right of that node (if nothing, walk back to the root, if there is something, then walk all the way to the right and pass that current value into the array)
        #           A
        #       /       \
        #      B         C
        #   /    \     /
        #  D     E    F
        #         G
        # [      ]  -> D B E
# tree_values =[D,B,E,F,C]
      tree_values = []

      def walk(root, values):
        if root is None:
      
          return
      # if root is not none
        if root:
          walk(root.left, values)
        #walk all the way to the left of the root
          tree_values.append(root.value, values)
        # append the current root's value to the tree_values array
          walk(root.right, values)
        # then if walk to the right of the tree
      walk(self.root, tree_values)
      # finally return the array to get the expected output
      return tree_values

    def post_order(self):
      #[stack]
      #traversal stack[A.B,D]
      #[D,E]
      # left > right > root
            #           A
            #       /       \
            #      B         C
            #   /    \     /
            #  D     E    F
    
      # [D,E,B, F,C,A]
      tree_values = []
    
      def walk(root, values):
        if root is None:
          return
    
        if root:
          walk(root.left, values)
          walk(root.right, values)
          values.append(root.value)

        walk(self.root, tree_values)
        return tree_values

        #           30
        #       /       \
        #      15         35
        #   /    \     /
        #  14     16    33


    #       30
    #           35
    #       33     


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


# tried to create the Node class here instead of importing to resolve import errors
class Node:
  def __init__(self, value = None, left = None, right = None):
    self.value = value
    self.left = left
    self.right = right