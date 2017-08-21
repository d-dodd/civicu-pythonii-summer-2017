import math

allerg_names = ['eggs', 'peanuts', 'shellfish', 'strawberries', 'tomatoes', 'chocolate', 'pollen', 'cats']

class Allergies(object):
	def __init__(self, n):
		self.score = n
		self.lst = []
		if n > 0:
			l1 = [1, 2, 4, 8, 16, 32, 64, 128]
			l2 = []
			x = n
			j = 8
			while x > 255:
				x -= 2**j
				j += 1
			while x > 0 and len(l1) > 0:
				l1 = [y for y in l1 if y <= x]
				y = l1.pop()
				l2.append(y)
				x -= y
			for item in l2:
				i = int(math.log(item, 2))
				self.lst.append(allerg_names[i])

		
	def is_allergic_to(self, s):
		return (s.lower() in self.lst)
		
	#def lst(self):
		return self.allergy_list
		
