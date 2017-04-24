#! /usr/bin/env python

dictionary = {0: 0, 1: 1}

def fibonacci(n):
    if n in dictionary:
        return dictionary[n]
    else:
        dictionary[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return dictionary[n]

def test():

    assert 0 == fibonacci(0)
    assert 1 == fibonacci(1)

    assert 1 == fibonacci(2)
    assert 2 == fibonacci(3)
    assert 3 == fibonacci(4)
    assert 5 == fibonacci(5)
    assert 8 == fibonacci(6)

    print "success"

if __name__ == "__main__":
    test()
