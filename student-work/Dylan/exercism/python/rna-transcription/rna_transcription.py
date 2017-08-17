def to_rna(s):
	s = s.upper().strip()
	for item in s:
		if item not in 'GCTA':
			return ''
	l = [ch(x) for x in s]
	return ''.join(l)
	

def ch(x):
	if x == 'G':
		return 'C'
	elif x == 'C':
		return 'G'
	elif x == 'T':
		return 'A'
	elif x == 'A':
		return 'U'
	
	
