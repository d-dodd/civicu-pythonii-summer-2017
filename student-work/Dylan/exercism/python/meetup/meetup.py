from datetime import date


dayths = [None, "first", "second", "third", "fourth", "fifth"]
weekdays = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

'''    MAIN FUNCTION     '''
def meetup_day(yr, m, wkdy, info):
	wkdy = weekdays.index(wkdy.lower().strip())   # "monday" = 0; "sunday" = 6
	info = info.lower().strip()
	dt_first = date(yr, m, 1)
	dt_sixth = date(yr, m, 6)
	dayth = find_dayth(dt_first, dt_sixth, wkdy, info)    #dayth == 1 <=> it's the first of that weekday in its month
	day = find_day(dt_first, wkdy, dayth)
	return date(yr, m, day)

'''      HELPER FUNCTIONS       '''
def find_dayth(dt_first, dt_sixth, wkdy, info):
	if info == "teenth":
		if dt_sixth.weekday() == wkdy:
			return 2
		else:
			return 3
	else:
		# the poss dayths besides teenth's are 1st, 2nd, 3rd, 4th, and last (fifth?)
		# gotta calculate the dayth based on that
		if info in ["1st", "2nd", "3rd", "4th", "5th"]:
			return int(info[0])
		else: 					# deals with case where info == "last"
			m = dt_first.month
			wd1 = dt_first.weekday()
			if m == 2:
				if _is_leap_year(dt_first.year) and dt_first.weekday() == wkdy:
					return 5
				else:
					return 4
			elif m in [9, 4, 6, 11]:
				if wkdy in [wd1, wd1 + 1] or (wkdy == 0 and wd1 == 6):
					return 5
				else:
					return 4
			else:
				if wkdy in [wd1, wd1 + 1, wd1 + 2]:
					return 5
				elif (wd1 == 5 and wkdy in [6, 0]) or (wd1 == 6 and wkdy in [0, 1]):
					return 5
				else:
					return 4 

def _is_leap_year(y):
	return y % 4 == 0 and (y % 100 != 0 or y % 400 == 0)


def find_day(dt1, wd, dyth):
	wd1 = dt1.weekday()
	if wd >= wd1:
		first_wd = wd - wd1 + 1		# first_wd = the day of the month of the 
	else:							# first instance of wd
		first_wd = (wd + 7) - wd1 + 1
	return first_wd + ((dyth - 1) * 7)
