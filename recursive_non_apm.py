#!/usr/bin/env python


def my_func(count=0):
    count += 1

    if count == 999 - 1:
        return count

    return my_func(count)

if __name__ == '__main__':
    my_func()
