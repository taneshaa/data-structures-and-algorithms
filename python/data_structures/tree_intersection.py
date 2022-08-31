from hashtable.py import hashtable

def tree_intersection(tree1, tree2)
  storage_array = []
  tree1 = tree1.pre_order()
  tree2 = tree2.pre_order()
  new_hashtable = hashtable()
  for value in tree1:
    new_hashtable.add(key=str(value), value=value)
  for value in tree2:
    if new_hashtable.contains(str(value)):
      storage_array.append(value)
  return storage_array