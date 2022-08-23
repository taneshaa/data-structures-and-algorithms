import pytest
from python/data_structures/blog_post/insertion.py import insertion_sort

# one for positive
def test_sort():
   int_list = [45,67,3,27,13,8]
   insertion_sort(int_list)
   expected = [3, 8, 13, 27, 45, 67]
   assert int_list == expected

# one for negative
def test_sort1():
   int_list = [-43,-66,-2,-26,-12,-7]
   insertion_sort(int_list)
   expected = [-2, -7, -12, -26, -44, -66]
   assert int_list == expected

  #  one of decimal

  # one expected to fair