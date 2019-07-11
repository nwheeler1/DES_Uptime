import datetime

start = datetime.date(2019,4,1)

now = datetime.datetime.now()
curr = datetime.date(now.year, now.month, now.day)

daysIncludingStart = (curr-start).days + 1

str1 = "https://www.gw-openscience.org/s/summary_pages/"
str2 = "detector_status/cache/day/"
str3 = "/H1L1V1-OBSERVING_BNS_INSPIRAL_RANGE-"
secondsSince1980 = 1238112018
str4 = "-86400.png"

oneDay = datetime.timedelta(days = 1)

URLs = open("URLs.txt", "w")

for x in range(daysIncludingStart):
	
	year = str(start.year)
	month = str(start.month).zfill(2)
	day = str(start.day).zfill(2)

	out = str1 + str2 + year + month + day
	out += str3 + str(secondsSince1980) + str4 + "\n"
	URLs.write(out)
	start += oneDay
	secondsSince1980 += 86400