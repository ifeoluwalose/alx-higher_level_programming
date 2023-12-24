#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    """simple_delete: deletes a key in a dictionary.

    Args:
        a_dictionary:
        key:

    Returns:
        nothing
    """
    if key in a_dictionary:
        del (a_dictionary[key])
    return (a_dictionary)
