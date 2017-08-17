def distance(str1, str2):
	str1, str2 = str1.upper().strip(), str2.upper().strip()
	if len(str1) != len(str2):
		raise ValueError("Input strings are of unequal length")
	for item in str1+str2:
		if item not in 'GCTAU':
			raise ValueError("At least one input strings was invalid")
	diffs, i = 0, 0
	while i < len(str1):
		if str1[i] != str2[i]:
			diffs += 1
		i += 1
	return diffs
