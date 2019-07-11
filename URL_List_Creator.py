import datetime

#Sets beginning of observing run
start = datetime.date(2019,4,1)

#Gets current day
now = datetime.datetime.now()

#Gets date object of current day for easier maniuplation
curr = datetime.date(now.year, now.month, now.day)

#Finds number of days' worth of images to grab
daysIncludingStart = (curr-start).days + 1

#Strings for URL creation
str1 = "https://www.gw-openscience.org/s/summary_pages/"
str2 = "detector_status/cache/day/"
str3 = "/H1L1V1-OBSERVING_BNS_INSPIRAL_RANGE-"
secondsSince1980 = 1238112018
str4 = "-86400.png"

#Allows for start date to be updated by one day at a time
oneDay = datetime.timedelta(days = 1)

#Creates URL file
URLs = open("URLs.txt", "w")

#Creates and writes all URLs
for x in range(daysIncludingStart):
	
	#Finds values of the next day
	year = str(start.year)
	month = str(start.month).zfill(2)
	day = str(start.day).zfill(2)

	#Concatenates URL string
	out = str1 + str2 + year + month + day
	out += str3 + str(secondsSince1980) + str4 + "\n"

	#Writes the URL to the file
	URLs.write(out)

	#Updates the day for the URL string
	start += oneDay
	secondsSince1980 += 86400

#Closes file
URLs.close()