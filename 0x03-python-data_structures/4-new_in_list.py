#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """new_in_list: replaces an element in a list at a specific
                    position without modifying the original list
                    (like in C).

    Args:
        my_list:
        idx:
        element:

    Returns:
        the element at the index(idx), otherwise None.
    """
    new_list = my_list[:]
    if (idx >= (len(my_list)) or idx < 0):
        return new_list
    new_list[idx] = element
    return new_list
