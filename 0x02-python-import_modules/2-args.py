#!/usr/bin/python3
import sys

if __name__ == '__main__':
    argv = sys.argv
    print('{} arguments.'.format(len(argv) - 1))
    for i in range(len(argv) - 1):
        print('{}: {}'.format(i + 1, argv[i + 1]))
