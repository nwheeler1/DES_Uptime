import matplotlib.pyplot as plt

def getUserInput(text, validInputs):
	userInput = input(text).lower()
	while(not (userInput in validInputs)):
		print("Invalid input, please try again.")
		userInput = input(text).lower()
	return userInput


uptimeValues = []

with open("Uptime.txt") as f:
	f.readline()
	f.readline()

	nextLine = "\n"
	while(nextLine != ""):
		nextLine = f.readline()
		if(nextLine != "\n" and nextLine != ""):
			ints = nextLine.split()
			uptimeValues.append([ints[1], ints[2], ints[3]])


hourOne = 0
hourTwo = 0

graphType = getUserInput("Please enter the graph type: hour, day\n", ["hour", "day"])

if(graphType == "hour"):
	hourOne = int(getUserInput("Please enter the first hour\n", list(str(x) for x in range(len(uptimeValues)))))
	hourTwo = int(getUserInput("Please enter the second hour (larger than or equal to the first)\n", list(str(x) for x in range(hourOne, len(uptimeValues)))))

elif(graphType == "day"):
	singleDay = getUserInput("Please enter the day graph type: single, range\n", ["single", "range"])
	
	if(singleDay == "single"):
		day = int(getUserInput("Please enter the day number (starting from 0):\n", list(range(int((len(uptimeValues) + 1)/24)))))
		hourOne = (day - 1) * 24
		hourTwo = hourOne + 23

	else:
		dayOne = int(getUserInput("Please enter the first day number (starting from 0):\n", list(range(int((len(uptimeValues) + 1)/24)))))
		dayTwo = int(getUserInput("Please enter the second day number (starting from 0, larger or equal to the first):\n", list(range(dayOne, int((len(uptimeValues) + 1)/24)))))
		hourOne = (dayOne - 1) * 24
		hourTwo = (dayTwo - 1) * 24 + 23

time = list(range(hourOne, hourTwo + 1))
Livingston = [int(x[0])+0.1 if x[0] == '1' else None for x in uptimeValues[hourOne:hourTwo+1]]
Hanford = [int(x[1]) if x[1] == '1' else None for x in uptimeValues[hourOne:hourTwo+1]]
Virgo = [int(x[2])-0.1 if x[2] == '1' else None for x in uptimeValues[hourOne:hourTwo+1]]

fig = plt.figure()
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])


ax1 = plt.axes()
ax1.get_xaxis().tick_bottom()
ax1.axes.get_yaxis().set_visible(False)
plt.xlabel("Hours since Start of Run")

plt.title("Detector Uptime")
plt.plot(time, Livingston, label="Livingston")
plt.plot(time, Hanford, label="Hanford")
plt.plot(time, Virgo, label="Virgo")

plt.xlim(hourOne, hourTwo)

plt.legend(bbox_to_anchor=(1, 0.32), fancybox=True, shadow=True)
plt.show()