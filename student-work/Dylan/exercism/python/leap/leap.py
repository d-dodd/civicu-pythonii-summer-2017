def is_leap_year(n):
	x = not (n % 4)
	if not (n % 100 == 0) or (n % 400 == 0):
		return x
	else:
		return False
	
