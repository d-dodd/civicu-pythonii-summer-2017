import requests
import csv

url = 'http://service.civicpdx.org/homeless/ethnicity/?'

dicts = []
for i in range(2008, 2017):
    response = requests.get(url+str(i))
    response_dict = response.json()
    dicts.append(response_dict)

#~ for item in dicts[5]:
	#~ print(str(item))

f = lambda d, s, y: d.get(s, 0) if d['year'] == y else 0

# TOTALS (all years)
nine_tot = sum([f(d, 'count', 2009) for d in dicts[5]])
eleven_tot = sum([f(d, 'count', 2011) for d in dicts[5]])
thirteen_tot = sum([f(d, 'count', 2013) for d in dicts[5]])
fifteen_tot = sum([f(d, 'count', 2015) for d in dicts[5]]) + sum([f(d, 'count', 15) for d in dicts[5]])

ff = lambda d, k, v, y: d.get('count', 0) if ( d['year'] == y and d[k] == v ) else 0

# 2009
print("-"*50)
print('2009 total = {}'.format(nine_tot))


# 2011
eleven_emergencyShelter = sum([ff(d, 'sheltertype', 'emergencyShelter', 2011) for d in dicts[5]])
eleven_transitionalHousing = sum([ff(d, 'sheltertype', 'transitionalHousing', 2011) for d in dicts[5]])
eleven_unsheltered = sum([ff(d, 'sheltertype', 'unsheltered', 2011) for d in dicts[5]])

print("-"*50)
print('2011 total = {}'.format(eleven_tot))
print('emergency shelter = {}'.format(eleven_transitionalHousing))
print('transitional housing = {}'.format(eleven_transitionalHousing))
print('unsheltered = {}'.format(eleven_unsheltered))

# 2013
thirteen_emergencyShelter = sum([ff(d, 'sheltertype', 'emergencyShelter', 2013) for d in dicts[5]])
thirteen_transitionalHousing = sum([ff(d, 'sheltertype', 'transitionalHousing', 2013) for d in dicts[5]])
thirteen_unsheltered = sum([ff(d, 'sheltertype', 'unsheltered', 2013) for d in dicts[5]])
print("-"*50)
print('2013 total = {}'.format(thirteen_tot))
print('emergency shelter = {}'.format(thirteen_transitionalHousing))
print('transitional housing = {}'.format(thirteen_transitionalHousing))
print('unsheltered = {}'.format(thirteen_unsheltered))

# 2015
fifteen_emergencyShelter = sum([ff(d, 'sheltertype', 'emergencyShelter', 2015) for d in dicts[5]]) + sum([ff(d, 'sheltertype', 'emergencyShelter', 15) for d in dicts[5]])
fifteen_transitionalHousing = sum([ff(d, 'sheltertype', 'transitionalHousing', 2015) for d in dicts[5]]) + sum([ff(d, 'sheltertype', 'transitionalHousing', 15) for d in dicts[5]])
fifteen_unsheltered = sum([ff(d, 'sheltertype', 'unsheltered', 2015) for d in dicts[5]]) + sum([ff(d, 'sheltertype', 'transitionalHousing', 15) for d in dicts[5]])
print("-"*50)
print('2015 total = {}'.format(fifteen_tot))
print('2015 emergency shelter = {}'.format(fifteen_emergencyShelter))
print('2015 transitional housing = {}'.format(fifteen_transitionalHousing))
print('2015 unsheltered = {}'.format(fifteen_unsheltered))

info_nine = [2009, nine_tot, "NA", "NA", "NA"]
info_eleven = [2011, eleven_tot, eleven_emergencyShelter, eleven_transitionalHousing, eleven_unsheltered]
info_thirteen = [2013, thirteen_tot, thirteen_emergencyShelter, thirteen_transitionalHousing, thirteen_unsheltered]
info_fifteen = [2015, fifteen_tot, fifteen_emergencyShelter, fifteen_transitionalHousing, fifteen_unsheltered]
info = [info_nine, info_eleven, info_thirteen, info_fifteen]

with open('homelessness_data.csv', 'w') as fout:
	r = csv.writer(fout)
	r.writerow(('year', 'total', 'emergency shelter', 'transitional housing', 'unsheltered'))
	for l in info:
		r.writerow((l[0], l[1], l[2], l[3], l[4]))
	
