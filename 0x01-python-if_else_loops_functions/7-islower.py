#!/usr/bin/env python3

# islower - function to test if input is lower case
# Return - True or False
def islower(c):
    if ord(c) > 96 and ord(c) < 123:
        return True
    else:
        return False
