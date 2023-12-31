#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    """delete_at: deletes the item at a specific position in a list.
    Args:
        my_list:

    Returns:
        a new list of bool
    """
    if ((idx < 0) or (idx >= len(my_list))):
        return my_list
    del (my_list[idx])
    return my_list
