caps = list(range(65, 91))
lower = list(range(97, 123))
everything = list(range(33, 127))

def hey(str):
	str = str.strip()
	if says_nothing(str):
		return "Fine. Be that way!"
	elif question(str):
		return "Sure."
	elif yell(str):
		return "Whoa, chill out!"
	else:
		return "Whatever."

def question(str):
	ord_list = [ord(s) for s in str]
	symb_list = [n for n in ord_list if n in everything and n != 63]     # ord("?") == 63
	return str[-1] == "?" and len(symb_list) > 0 and not all(n in caps for n in symb_list)   

def yell(str):
	return not any(ord(s) in lower for s in str) and any(ord(s) in caps for s in str)

def says_nothing(str):
	return len(str) == 0 or not any(ord(s) in everything for s in str)
