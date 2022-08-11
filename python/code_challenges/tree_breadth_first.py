def breadth_first(tree):
  # we first create two separate arrays: one for our queue, and one that we are storing and saving our values into so that we can return that array of values that follow the breadth first traversal
    queue_list = []
    values = []

# if the root is not none
    if tree.root:
# insert the root at the index of 0
        queue_list.insert(0, tree.root)

  #enter the while loop so long as the queue list is populated
    while queue_list:
  # create a variable that uses the pop method to pop off the value in the queue.
        node = queue_list.pop()
  # append that value in the queue to the values array
        values.append(node.value)
  # we passed in the tree, so the next sequence will check to see if there are children of the current node.
        if node.left:
            queue_list.insert(0, node.left)
  # if there is a left node, insert it into the queue
        if node.right:
  # if there is a right node, insert it into the queue
            queue_list.insert(0, node.right)
  # when all the queues have been inserted and appended to the values array, we return the array. The expected ouptut would be an array of values implementing the breadth first traversal.
    return values

# queue_list = []
# values = ['A', 'B','C','D','E','F']
#         [A]
#        /   \
#     [B]    [C]
#    /  \     /
#  [D]  [E]  [F]
