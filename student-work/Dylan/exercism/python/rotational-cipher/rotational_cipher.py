lower_case_letters = [chr(x) for x in list(range(97, 123))]
upper_case_letters = [chr(x) for x in list(range(65, 91))]

lc_number_list = [122] + list(range(97, 122))
uc_number_list = [90] + list(range(65, 90))

def rotate(s, n):
	l = list(s)
	
	# first deal with lower case letters
	f1 = lambda x: ord(x) if x in lower_case_letters else x
	l = [f1(x) for x in l]
	f2 = lambda x: lc_number_list[((x - 96 + n) % 26)] if type(x)==int else x
	l = [f2(x) for x in l]
	f3 = lambda x: chr(x) if type(x)==int else x
	l = [f3(x) for x in l]
	
	# then deal with upper case letters
	f4 = lambda x: ord(x) if x in upper_case_letters else x
	l = [f4(x) for x in l]
	f5 = lambda x: uc_number_list[((x - 64 + n) % 26)] if type(x)==int else x
	l = [f5(x) for x in l]
	f6 = lambda x: chr(x) if type(x)==int else x
	l = [f6(x) for x in l]

	# now we're done!
	return ''.join(l)

