def add_fns(f_and_df, g_and_dg):
    """Return the sum of two polynomials."""
    def add(n, derived):
        return f_and_df(n, derived) + g_and_dg(n, derived)
    return add

def mul_fns(f_and_df, g_and_dg):
    """Return the product of two polynomials."""
    def mul(n, derived):
        f, df = lambda x: f_and_df(x, False), lambda x: f_and_df(x, True)
        g, dg = lambda x: g_and_dg(x, False), lambda x: g_and_dg(x, True)
        if derive:
            return f(x) * dg(x) + df(x) * g(x)
        else:
            return f(x) * g(x)
    return mul

def poly_zero(f_and_df):
    """Return a zero of polynomial f_and_df, which returns:
        f(x)  for f_and_df(x, False)
        df(x) for f_and_df(x, True)

    >>> q = quadratic(1, 6, 8)
    >>> round(poly_zero(q), 5) # Round to 5 decimal places
    -2.0
    >>> round(poly_zero(quadratic(-1, -6, -9)), 5)
    -3.0
    """
    return find_zero(lambda x: f_and_df(x, False), lambda x: f_and_df(x, True))
    