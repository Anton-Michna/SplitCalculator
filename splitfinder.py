#Anton Michna
from tkinter import *

root = Tk() #defining the window that everything goes into
root.title("Runner.net")#defining the title of the window

windowWidth = root.winfo_reqwidth()#gets height and width of screen
windowHeight = root.winfo_reqheight()

positionRight = int(root.winfo_screenwidth()/2 - windowWidth/2)# Gets both half the screen width/height and window width/height
positionDown = int(root.winfo_screenheight()/2 - windowHeight/2)
 
root.geometry("+{}+{}".format(positionRight, positionDown))# Positions the window in the center of the page

openLabel = Label(root, text = "Calculate: ")#opening prompt
openLabel.grid(row = 0, column = 0, columnspan = 2)
#openLabel.place(relx = 0.5, rely = 0.5, anchor = CENTER)

def callback(input):
	if input.isdigit():
		return True
	elif input == "":
		return True
	else:
		return False


def splitClick():#runs when user wants to find splits required for a certain pace
	splitWindow = Tk()
	splitWindow.title("Split Finder")

	windowWidth = splitWindow.winfo_reqwidth()#gets height and width of screen
	windowHeight = splitWindow.winfo_reqheight()

	positionRight = int(splitWindow.winfo_screenwidth()/2 - windowWidth/2)# Gets both half the screen width/height and window width/height
	positionDown = int(splitWindow.winfo_screenheight()/2 - windowHeight/2)
 
	splitWindow.geometry("+{}+{}".format(positionRight, positionDown))# Positions the window in the center of the page


	label_1 = Label(splitWindow, text = "I want to run: ")#creating labels for user's prompt
	label_2 = Label(splitWindow, text = " minutes and:")
	label_3 = Label(splitWindow, text = " second pace per: ")
	label_4 = Label(splitWindow, text = " for: ")

	entry_1 = Entry(splitWindow, validate = "key", width = 5)#creating user input spaces
	entry_2 = Entry(splitWindow, validate = "key", width = 5)
	entry_3 = Entry(splitWindow, validate = "key", width = 5)

	entry_1['validatecommand'] = (entry_1.register(callback), '%P')#only allowing user to enter numbers in text boxes
	entry_2['validatecommand'] = (entry_2.register(callback), '%P')
	entry_3['validatecommand'] = (entry_3.register(callback), '%P')

	distance = StringVar(splitWindow)#creating dropdown box for use to choose unit of distance
	distance.set("Meters")
	drop = OptionMenu(splitWindow, distance, "Meters", "Miles")

	distance2 = StringVar(splitWindow)#creating dropdown box for use to choose unit of distance
	distance2.set("Mile")
	drop2 = OptionMenu(splitWindow, distance2, "Kilometer", "Mile")


	label_1.grid(row = 0, column = 0)#placing widgets on screen for user prompt
	entry_1.grid(row = 0, column = 1)
	label_2.grid(row = 0, column = 2)
	entry_2.grid(row = 0, column = 3)
	label_3.grid(row = 0, column = 4)
	drop2.grid(row = 0, column = 5)
	label_4.grid(row = 0, column = 6)
	entry_3.grid(row = 0, column = 7)
	drop.grid(row = 0, column = 8)

	
	def calculate():#function to calculate the splits user asks for
		minutes = int(entry_1.get())#getting user input values
		seconds = int(entry_2.get())
		finalDistance = int(entry_3.get())
		givenPace = distance2.get()#given pace, per kilometer or mile
		desiredDistanceType = distance.get()#distance that user desires to go


		minToSec = minutes * 60
		totalSec = minToSec + seconds#converting time to seconds

		if givenPace == "Mile":#determing if given pace is per mile or kilometer
			p400 = totalSec / 4  #assigning time each quarter mile takes from given user pace

		if givenPace == "Kilometer":
			p400 = totalSec / 2.5   #assigning quarter mile pace if user gave kilometer pace

		if desiredDistanceType == "Meters":#if the user wants to travel a certain amount of meters
			multiplier = finalDistance / 400 #finding the value to multiply the quarter mile split by
			totalTime = multiplier * p400 #finding the totalTime the user will take to cover specified distance
		
		if desiredDistanceType == "Miles":
			mileTime = p400 * 4 #multiplying the calculated quarter mile time in order to get mile time
			totalTime = mileTime * finalDistance #calculating total time it will take
		
		finalMinutesSplit = int(totalTime / 60)#splitting total time into minutes and seconds
		finalSecondsSplit = totalTime % 60


		label_5 = Label(splitWindow, text = "You will have to run: " + str(finalDistance) + " " + str(desiredDistanceType) + " in: " + str(finalMinutesSplit))
		#creating a label to display splits
		label_6 = Label(splitWindow, text = "minute(s) and: " + str(finalSecondsSplit) + " second(s).")
		label_5.grid(row = 2, column = 3)#printing split that was calculated
		label_6.grid(row = 2, column = 4)
	
	button_enter = Button(splitWindow, text = "Enter", bg = "blue", padx = 50, command = calculate)#button for user to click when input is ready
	button_enter.grid(row = 1, column = 0, columnspan = 9)#adding button to grid

	splitWindow.mainloop()

def paceClick():#runs when user wants to find average pace of race that they ran
	paceWindow = Tk()
	paceWindow.title("Pace Calculator")

	windowWidth = paceWindow.winfo_reqwidth()#gets height and width of screen
	windowHeight = paceWindow.winfo_reqheight()

	positionRight = int(paceWindow.winfo_screenwidth()/2 - windowWidth/2)# Gets both half the screen width/height and window width/height
	positionDown = int(paceWindow.winfo_screenheight()/2 - windowHeight/2)
 
	paceWindow.geometry("+{}+{}".format(positionRight, positionDown))# Positions the window in the center of the page

	label_1 = Label(paceWindow, text = "I ran: ")#creating labels for user's prompt #1
	label_2 = Label(paceWindow, text = "in: ")#4
	label_3 = Label(paceWindow, text = "minutes and: ")#6
	label_4 = Label(paceWindow, text = "seconds ")#8

	entry_1 = Entry(paceWindow, validate = "key", width = 7)#2
	entry_2 = Entry(paceWindow, validate = "key", width = 5)#5
	entry_3 = Entry(paceWindow, validate = "key", width = 5)#7

	entry_1['validatecommand'] = (entry_1.register(callback), '%P')#only allowing user to enter numbers in text boxes
	entry_2['validatecommand'] = (entry_2.register(callback), '%P')
	entry_3['validatecommand'] = (entry_3.register(callback), '%P')

	
	raceDistance = StringVar(paceWindow)#dropdown for the distance of users race
	raceDistance.set("Meters")
	drop = OptionMenu(paceWindow, raceDistance, "Meters", "Miles")#3


	label_1.grid(row = 0, column = 0)#creating string of widgets for user prompt
	entry_1.grid(row = 0, column = 1)
	drop.grid(row = 0, column = 2)
	label_2.grid(row = 0, column = 3)
	entry_2.grid(row = 0, column = 4)
	label_3.grid(row = 0, column = 5)
	entry_3.grid(row = 0, column = 6)
	label_4.grid(row = 0, column = 7)


	def paceFind():#runs when user has input the first three values to calculate average pace
		raceLength = int(entry_1.get())#amount of selected distance
		raceMinutes = int(entry_2.get())#minutes race took
		raceSeconds = int(entry_3.get())#seconds race took
		perSplit = 0

		distanceType = raceDistance.get()#miles or meters

		minToSec = raceMinutes * 60
		totalSec = minToSec + raceSeconds#converting time to seconds

		label_5 = Label(paceWindow, text = "I want to know the pace of this race per: ")#creating new pop up after user continues

		desrireType = StringVar(paceWindow)#dropdown box for new popup
		desrireType.set("Kilometer")
		drop2 = OptionMenu(paceWindow, desrireType, "Kilometer", "Mile")

		label_5.grid(row = 2, column = 0, columnspan = 5)#adding new popup to the grid
		drop2.grid(row = 2, column = 5, columnspan = 2)


		def calculate2():#runs after user has input final data, kilometer or mile pace, then average pace is calculated
			desType = desrireType.get()

			if distanceType == "Meters":#runs if user's pace was in meters
				ratio = raceLength / 400 #ratio of raceLength compared to a quarter mile
				quarterSplit = totalSec / ratio #finding how long quarter mile split is
				
				if desType == "Kilometer":#runs based on if user wants per kilometer or mile pace
					perSplit = quarterSplit * 2.5#converting to a kilometer
				if desType == "Mile":
					perSplit = quarterSplit * 4#converting to a mile
				
			if distanceType == "Miles":#runs if user's race was in miles
				base = raceLength * 4 #converting number of miles ran to quarter miles ran
				quarterSplit = totalSec / base #finding how quick each quarter mile was

				if desType == "Kilometer":
					perSplit = quarterSplit * 2.5
				if desType == "Mile":
					perSplit = quarterSplit * 4

			minutesPer = int(perSplit / 60)#converting seconds total into minutes and seconds break down
			secondsPer = perSplit % 60
			
			label_7 = Label(paceWindow, text = "That is an average of: " + str(minutesPer) + " minutes and: " + str(secondsPer) + " seconds per " + str(desType))
			label_7.grid(row = 4, column = 0, columnspan = 8)#displaying calculated pace

		button_enter = Button(paceWindow, text = "Enter", bg = "red", padx = 50, command = calculate2)#creating button once user has completed input
		button_enter.grid(row = 3, column = 0, columnspan = 8)


	button_continue = Button(paceWindow, text = "Continue", bg = "red", padx = 50, command = paceFind)#button for user to click when input is ready
	button_continue.grid(row = 1, column = 0, columnspan = 8)#adding button to grid


	paceWindow.mainloop()#closing paceWindow loop



	
button_splits = Button(root, text = "Splits of Pace", fg = "white", bg = "blue", padx = 35, pady = 35, command = splitClick)#defining buttons for functions of application
button_avePace = Button(root, text = "Average Pace of race", fg = "white", bg = "red", padx = 35, pady = 35, command = paceClick)
button_splits.grid(row = 1, column = 0)
button_avePace.grid(row = 1, column = 1)

root.mainloop()#runs until program is closed