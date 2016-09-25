#newton's method 
def nth_root(a, n):
	return apporx_zero(lambda x : pow(x, n))

def improve(update, close, guess=1):
	while not close(guess):
		guess = update(guess)
	return guess

def apporx_zero(f):
	return find_zero(f, derive(f))


def find_zero(f, df):
	def near_zero(x):
		return approx_equal(x, 0)
	return improve(newton_update(f, df), near_zero)



#===================================help method======================================
def newton_update(f, df):
	def update(x):
		return x - f(x)/df(x)
	return update

def approx_equal(x, y, tolerance = 1e-15):
	return abs(x-y) < tolerance

def slope(f, x, a = 1e-10):
	return (f(a+x) - f(x))/a

def derive(f):
	def g(x):
		return slope(f, x)
	return g


