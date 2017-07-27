#please add any of the toy examples you build with comprehensions here
fish_tuple = ('blowfish', 'clownfish', 'catfish', 'octopus')

# make a list of all fish with a for loop
fish_list = []
for fish in fish_tuple:
    if fish != 'octopus':
        fish_list.append(fish)
        
# make a list of all fish using a list comp
fish_list = [fish for fish in fish_tuple if fish != 'octopus']

# nesting conditionals
number_list = [x for x in range(100) if x % 3 == 0 if x % 5 == 0]
# number_list = [0, 15, 30, 45, 60, 75, 90]

list_nums = [1, 2, 3]

# multiply each nummber in a list by 3
times_three = [(num * 3) for num in list_nums]

# building a set using a for loop
unique_letters = set()
for letter in word:
    unique_letters.add(letter)
    
# a set comprehension
unique_letters = {letter for letter in word}

my_dict = {"a": 1, "b": 2, "c": 3}

# using a for loop
flipped_dict = {}
for key, value in my_dict.items():
    flipped_dict[value] = key

# using a dict comp
flipped_dict = {value: key for key, value in my_dict.items()}



CONTEXT MANAGERS VS. JUST CALLING close()

# opening a file and then calling .close()
f = open('foo.txt', 'w')
f.close()

# opening a file using the `with` context manager
with open('foo.txt', 'w') as foo_file:
    # do something with foo, and the file will automatically close

