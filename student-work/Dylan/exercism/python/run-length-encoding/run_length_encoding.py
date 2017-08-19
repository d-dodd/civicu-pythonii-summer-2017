nums = '1234567890'

def decode(s):
	if len(s) < 2:
		return s
	decoded_str = ''
	str_num = ''
	for item in s:
		if item in nums:
			str_num += item
		else:
			if str_num != '':
				decoded_str += item * int(str_num)
				str_num = ''
			else:
				decoded_str += item
	return decoded_str

def encode(s):
	if len(s) < 2:
		return s
	list_of_patterns = []
	temp_storage = s[0]
	for item in s[1:]:
		if item in temp_storage:
			temp_storage += item
		else:
			list_of_patterns.append(temp_storage)
			temp_storage = item
	list_of_patterns.append(temp_storage)
	encoded_str = ''
	for item in list_of_patterns:
		if len(item) == 1:
			encoded_str += item
		else:
			encoded_str += str(len(item))+item[0]
	return encoded_str
