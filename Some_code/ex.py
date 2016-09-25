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
    if n <= 3 :
        return n
    else :
        return g(n-1) + 2* g(n-2) + 3 * g(n-3)
        
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
    if n <= 3:
        return n
    else:
        i = 2
        pre, curr, next = 1, 2, 3
        while i < n :
            pre, curr, next = curr, next, next + 2*curr + 3*pre
            i += 1
        return curr        

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
    if k==7 :
        return True
    elif k % 10 == 7 :
        return True
    elif k > 10:
        return has_seven(k // 10)
    return False

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
    def up(k,i):
        k, i = k + 1, i + 1
        if i % 7== 0 or has_seven(i):
            return down(k,i)
        elif i != n:
            return up(k, i)
        else:
            return k
    
    def down(k,i):
        k, i = k - 1, i + 1
        if i % 7== 0 or has_seven(i):
            return up(k,i)
        elif i != n: 
            return down(k,i)
        else: 
            return k

    return up(1,1)
        