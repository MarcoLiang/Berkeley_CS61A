def g(n):
    """Return the value of G(n), computed recursively.

    >>> g(1)
    1
    >>> g(2)
    2
    >>> g(3)
    3
    >>> g(4)
    10
    >>> g(5)
    22
    """
    if n <= 3:
        return n
    else:
        return g(n-1) + 2*g(n-2) + 3*g(n-3)

def g_iter(n):
    """Return the value of G(n), computed iteratively.

    >>> g_iter(1)
    1
    >>> g_iter(2)
    2
    >>> g_iter(3)
    3
    >>> g_iter(4)
    10
    >>> g_iter(5)
    22
    """
    if n in (1, 2, 3):
        return n
    a, b, c = 1, 2, 3
    while n > 3:
        a, b, c = b, c, c + 2*b + 3*a
        n -= 1
    return c

    


def has_seven(k):
    """Returns True if at least one of the digits of k is a 7, False otherwise.

    >>> has_seven(3)
    False
    >>> has_seven(7)
    True
    >>> has_seven(2734)
    True
    >>> has_seven(2634)
    False
    >>> has_seven(734)
    True
    >>> has_seven(7777)
    True
    """
    if k % 10 == 7:
        return True
    elif k < 10:
        return False
    else:
        return has_seven(k//10)


def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(7)
    7
    >>> pingpong(8)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    0
    >>> pingpong(30)
    6
    >>> pingpong(68)
    2
    >>> pingpong(69)
    1
    >>> pingpong(70)
    0
    >>> pingpong(71)
    1
    >>> pingpong(72)
    0
    >>> pingpong(100)
    2
    """
 
    def countup(i, x):
        if i == n:
            return x
        if i % 7 == 0 or has_seven(i):
            return countdown(i+1, x-1)
        else:
            return countup(i+1, x+1)

    def countdown(i, x):
        if i == n:
            return x
        if i % 7 == 0 or has_seven(i):
            return countup(i+1, x+1)
        else:
            return countdown(i+1, x-1)
    return countup(1, 1)



def count_change(amount):
    """Return the number of ways to make change for amount.

    >>> count_change(7)
    6
    >>> count_change(10)
    14
    >>> count_change(20)
    60
    >>> count_change(100)
    9828
    """
    def count(min, a):
        if a < 0:
            return 0
        if a == 0:
            return 1
        if min > a:
            return 0
        with_min = count(min, a-min)
        without_min = count(min*2, a)
        return with_min+without_min
    return count(1, amount)


def towers_of_hanoi(n, start, end):
    """Print the moves required to solve the towers of hanoi game, starting
    with n disks on the start pole and finishing on the end pole.

    The game is to assumed to have 3 poles.

    >>> towers_of_hanoi(1, 1, 3)
    Move the top disk from rod 1 to rod 3
    >>> towers_of_hanoi(2, 1, 3)
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 3
    >>> towers_of_hanoi(3, 1, 3)
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 3 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 1
    Move the top disk from rod 2 to rod 3
    Move the top disk from rod 1 to rod 3
    """
    assert 0 < start <= 3 and 0 < end <= 3 and start != end, "Bad start/end"
    if n == 1:
        print("Move the top disk from rod", start, "to rod", end)
    else:
        rest = 6-start-end
        towers_of_hanoi(n-1, start, rest)
        towers_of_hanoi(1, start, end)
        towers_of_hanoi(n-1, rest, end)
    
    


from operator import sub, mul

def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

    >>> make_anonymous_factorial()(5)
    120
    """
    return 'YOUR_EXPRESSION_HERE'
