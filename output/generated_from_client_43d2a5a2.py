# Prompt:
# Create a Python function to sort a list of integers

# Language: Python
# Task: Create a Python function to sort a list of integers

# Problem 1
# [1, 8, 6, 3, 5, 4, 9, 7]
# 5

# SOLUTION:


def sort_arr(lst):
    return lst

# TODO: Use a wrapper class to sort a list. Call the '_sort_arr' method instead


def _sort_arr(lst):
    lst = lst
    lst = list(sorted(lst))
    return lst


sort_arr([1, 8, 6, 3, 5, 4, 9, 7])
# [1, 3, 5, 9, 7, 6, 8, 4]
lst = [5, 4, 9, 7]
sorted_lst = _sort_arr(lst)
print(sorted_lst)
# [5, 4, 7, 9]
