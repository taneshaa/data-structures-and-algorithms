# Trees
From the reading and the lecture, I gained somewhat of an understanding of the depth first traversals within Binary Trees. Pre-order, In-Order, and Post-order were the three methods. We also were given knowledge about Binary Search Trees, where values that are smaller than the root are placed to the left whereas the larger values are implemented to the right.

Vocab for reference:
Depth first- going through the height of the tree, iterates through all of the trees, first and on-queuing an call stack to return an array of the tree traversal (three types, pre-order (root, left, right), in order(left, root, right), post order(left, right,root)

Breadth first- iterated through the entire tree until theres no more nodes (level to level)

Leaf- node that does not have any children (bottom of the tree)

K-aray- refers to max number of children that each Node can have. Doesn’t strictly have a left or right node, it just moves down levels and will read the node children.

Binary- numbers on the left have to be smaller, and based on the right the numbers have to be bigger. It will always check the root to see if the number you’re searching for is greater or smaller than the root, smaller is left, greater is right, will check the root again..etc

## Challenge
The first part of the challenge was create three functions that implemented the methods of the depth first traversal. the second part was to create a BinarySearchTree class that contained an "add" and a "contains" method. The add method adds a value into the tree, whereas the contains method returns a boolean of true or false if the value is in the tree.

## Approach & Efficiency
I worked with Brandon Mizutani via tutoring session

## API
**pre_order** - root >> left >> right
**in_order** - left >> root >> right
**post-order** - left >> right >> root (returns an array of the values, ordered appropriately.)

**add** - Adds a new node with that value in the correct location in the binary search tree.
**contains** - Returns: boolean indicating whether or not the value is in the tree at least once.
