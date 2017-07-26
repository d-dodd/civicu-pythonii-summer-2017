import requests
import json
import random
import collections

''' **************** CREATE A LIST (dicts) OF JSON RESPONSE OBJECTS ******************* '''
url = 'http://service.civicpdx.org/homeless/ethnicity/?'

dicts = []

for i in range(2008, 2017):
    response = requests.get(url+str(i))
    response_dict = response.json()
    dicts.append(response_dict)

'''
     ****  BELOW I INVESTIGATED THE 9 JSON RESPONSE OBJECTS IN dict  ***
     HERE'S WHAT I FOUND BELOW:
The first for-loop in this code shows that dict contains 9 lists, each of which contains 82 items. The for-loop embedded
in that loop, and the fact that v still has the value True at the end, shows that the 82 items are all dictionaries.

Also, the dictionaries appear to be giving information about individual people. I say this because one of their keys is 'ethnicity'.
(So they don't contain info on homeless shelters, but individual people.)

The code on lines 49-52 shows that there are 3 "sheltertypes": "unsheletered", "all", "transitionalHousing", and 
"emergencyShelter". So the individuals catalogued are either homeless or staying in some sort of transitional or emergency housing.

So dicts contains 9 lists, each of which contains 82 dictionaries that contain info about individuals. Also, it seems the 9
lists contain *exactly the same* 82 dictionaries! In other words, the 9 lists are identical to each other. (The 82 dictionaries
are not the same, as you can easily see by printing them out.)

The evidence that they're identical is the following. First, the code on lines 54-64 I compare the set of keys and values in the first
list of dictionaries with a randomly chosen dictionary from each of the other 8 dictionaries. Each time I ran the program, the keys 
and values of each randomly selected dictionary were identical to the keys and values of the dictionary from the first list that 
occurred at the same order in the list. Second, the code on lines 66-71 prints out the 18-21st 
dictionaries in all 9 sub-lists of dict. When they're printed out you can see that they're all identical.

That's what I found out on lines 41-71. I've commented them out now, but I did run them and found out what I mentioned.
'''

# v = True
# for item in dicts:
#     print(len(item), type(item))
#     for x in item:
#         if type(x) != dict:
#             v = False
# print("The lists contain only dictionaries: {}".format(v))
#
# shelter_types = set()
# for d in dicts[0]:
#     shelter_types.add(d['sheltertype'])
# print(shelter_types)

# dict_kvs = []
# for i in range(82):              # this loop returns a list of they keys and values of all 82 dictionaries in
#                                  # the first of the 9 sub-lists in dicts
#     keys, vals = set(dicts[0][i].keys()), set(dicts[0][i].values())
#     dict_kvs.append((keys, vals))
# for l in dicts[1:]:
#     i = random.randrange(0, 80)
#     keys, vals = set(l[i].keys()), set(l[i].values())
#     if (keys, vals) != dict_kvs[i]:
#         v = False
# print("The 9 lists are probably all identical: {}".format(v))

# for i in range(len(dicts)):
#     print("*"*20)
#     print(dicts[i][17])
#     print(dicts[i][18])
#     print(dicts[i][19])
#     print(dicts[i][20])

''' 
******* COLLECTING MORE DATA ************** 
This data doesn't actually contain information on homeless shelters. I don't know what "count" means, but it's not the
number of people staying at a particular homeless shelter. So I decided to do something different than the assignment.

First, I calculated the number of the 82 people who were in the different kinds of housing, and the number of people who
were in the different ethnic categories. Second, I counted ethnic distribution in the different housing categories.

In the commented out code I figured out what values were given for the keys in the data.

'''

the_data = dicts[0]             # Since the sublists of dicts are identical, this contains all the info there is in dicts
# year_vals = set()
# ethnicity_vals = set()
# sheltertype_vals = set()
# id_vals = set()
# count_vals = set()
# page_vals = set()
#
# for d in the_data:
#     year_vals.add(d['year'])
#     ethnicity_vals.add(d['ethnicity'])
#     sheltertype_vals.add(d['sheltertype'])
#     # id_vals.add(d['id'])
#     # count_vals.add(d['count'])
#     # page_vals.add(d['page'])
#
# print("year_vals: {}".format(year_vals))
# # set([2009, 2015, 2013, 2011, 15])
# print("ethnicity_vals: {}".format(ethnicity_vals))
# # set([u'latino', u'hawaiian', u'AI', u'infoNotProvided', u'multiRacial', u'black', u'popOfColor', u'white', u'white ', u'asian'])
# print("sheltertype_vals: {}".format(sheltertype_vals))
# # set([u'transitionalHousing', u'all', u'unsheltered', u'emergencyShelter'])

# print("id_vals: {}".format(id_vals))
# print("count_vals: {}".format(count_vals))
# print("page_vals: {}".format(page_vals))

ethnicity = []
ethnicity_transitional = []
ethnicity_unsheltered = []
ethnicity_all = []
ethnicity_emergency = []
shelter = []

for d in the_data:
    ethnicity.append(d['ethnicity'])
    shelter.append(d['sheltertype'])
    if d['sheltertype'] == 'transitionalHousing':
        ethnicity_transitional.append(d['ethnicity'])
    elif d['sheltertype'] == 'unsheltered':
        ethnicity_unsheltered.append(d['ethnicity'])
    elif d['sheltertype'] == 'all':
        ethnicity_all.append(d['ethnicity'])
    else:
        ethnicity_emergency.append(d['ethnicity'])



ethn_counter = collections.Counter(ethnicity)
shelt_counter = collections.Counter(shelter)
print("*"*50)
print("TOTAL DISTRIBUTIONS: ethnicity, shelter types")
print("*"*50)
print(ethn_counter)
print("\n", shelt_counter)


print("*"*50)
print("DISTRIBUTION OF ETHNICITIES BY SHELTER TYPE")
print("*"*50)


eth_trans_c = collections.Counter(ethnicity_transitional)
eth_unsh_c = collections.Counter(ethnicity_unsheltered)
eth_emerg_c = collections.Counter(ethnicity_emergency)
eth_all_c = collections.Counter(ethnicity_all)
print("Distr. of ethnicities in transitional housing: {}".format(eth_trans_c))
print("\nDistr. of ethnicities who are unsheltered: {}".format(eth_unsh_c))
print("\nDistr. of ethnicities in emergency housing: {}".format(eth_emerg_c))
print("\nDistr. of ethnicities who have been in ALL: {}".format(eth_all_c))
