#!/usr/bin/env python
from ddtrace import tracer

@tracer.wrap()
def my_func(count=0):
    count += 1

    if count == 492 - 1:
        return count

    return my_func(count)

if __name__ == '__main__':
    my_func()
