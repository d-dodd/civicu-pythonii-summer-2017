def detect_anagrams(w, l):
	w_lst = list(w.lower())
	w_lst.sort()
	l_lst = []
	l = [word for word in l if word.lower() != w.lower()]
	for item in l:
		i, l = item, list(item.lower())
		l.sort()
		l_lst.append((i, l)) 
	anagrams = [t[0] for t in l_lst if t[1] == w_lst]
	return anagrams

