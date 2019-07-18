from PIL import Image
import os

Livingston = []
Hanford = []
Virgo = []

numFiles = 0

for file in os.listdir("Images"):
	numFiles += 1


for x in range(numFiles):

	image = Image.open("Images/Day" + str(x + 1) + ".png")

	pix = image.load()

	LDay = []
	HDay = []
	VDay = []

	hour = 0

	while(hour < 24):

		isLOn = 0
		isHOn = 0
		isVOn = 0

		for y in range(image.size[1]):

			p = pix[125+40*hour, y]

			red = p[0]
			green = p[1]
			blue = p[2]

			if(55 < red < 95 and 146 < green < 186 and 235 < blue):
				isLOn = 1

			elif(211 < red and green < 27 and blue < 27):
				isHOn = 1

			elif(135 < red < 175 and 69 < green < 109 and 162 < blue < 202):
				isVOn = 1

		LDay.append(isLOn)
		HDay.append(isHOn)
		VDay.append(isVOn)

		hour += 1

	Livingston.append(LDay)
	Hanford.append(HDay)
	Virgo.append(VDay)

outputFile = open("Uptime.txt", "w")

outputFile.write("Hours Since Start of Run\t Livingston\t Hanford\t Virgo\n\n")

hours = 0

for day in range(len(Livingston)):
	for hour in range(24):
		outputFile.write(str(hours) + "\t" + str(Livingston[day][hour]) + "\t" + str(Hanford[day][hour]) + "\t" + str(Virgo[day][hour]) + "\n")
		hours += 1
	outputFile.write("\n")