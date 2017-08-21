def square_of_sum(n):
    l = list(range(1, n+1))
    return sum(l)**2


def sum_of_squares(n):
    l = list(range(1, n+1))
    return sum([x**2 for x in l])


def difference(n):
	return square_of_sum(n) - sum_of_squares(n)
