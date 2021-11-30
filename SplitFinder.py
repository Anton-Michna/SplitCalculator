from tkinter import *

root = Tk() #defining the window that everything goes into
root.title("Runner.net")#defining the title of the window


openLabel = Label(root, text = "Calculate: ")#opening prompt
openLabel.grid(row = 0, column = 0, columnspan = 2)


def splitClick():#runs when user wants to find splits required for a certain pace
	splitWindow = Tk()
	splitWindow.title("Split Finder")


	label_1 = Label(splitWindow, text = "I want to run: ")#creating labels for user's prompt
	label_2 = Label(splitWindow, text = " minutes and:")
	label_3 = Label(splitWindow, text = " second pace per: ")
	label_4 = Label(splitWindow, text = " for: ")

	entry_1 = Entry(splitWindow, width = 5)#creating user input spaces
	entry_2 = Entry(splitWindow, width = 5)
	entry_3 = Entry(splitWindow, width = 5)


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
	

	
button_splits = Button(root, text = "Splits of Pace", fg = "white", bg = "blue", padx = 35, pady = 35, command = splitClick)#defining buttons for functions of application
button_avePace = Button(root, text = "Average Pace of race", fg = "white", bg = "red", padx = 35, pady = 35)
button_splits.grid(row = 1, column = 0)
button_avePace.grid(row = 1, column = 1)

root.mainloop()