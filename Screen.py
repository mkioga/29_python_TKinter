
# =============
# Screen.py
# =============


# We are going to create a more complex screen with 5 columns and 5 rows


try:
    import tkinter
except ImportError:
    import Tkinter as tkinter

# "Import os" means import operating system. Will be used on the code to populate list.

import os

mainWindow = tkinter.Tk()

mainWindow.title("Screen Demo - Title")
mainWindow.geometry('700x500-8-200')  # we use -8-200 to change positioning relative to your screen
mainWindow['padx'] = 10  # This is to pad main window so things are not very close to the edge

# We will make the label, put it in the mainWindow
# put it in column 0, row 0 and let it span 3 columns

label = tkinter.Label(mainWindow, text="Tkinter grid demo - Label")
label.grid(row=0, column=0, columnspan=3)

# if we run above command without the weights below, you see the "Tkinter grid demo - Label"
# is on the left side and does not look like it spanning the columns even if default for sticky is center

# We need to add weights to columns and rows to make the "Label" centered on the columns
# When you run config with the weights below, you see the label more centered and spanning 3 columns
# Weights are relative. A window with weight of 3 increases in size 3 times faster than one with weight of 1 if the main window increases in size
# But also weight of 3 decreases faster than 1 if window decreases in size.
# play with the weights to see how they make the label placement change
# NOTE that you can run python program multiple times without closing the original window. This is important for comparisons
# If you want a window like scrollbar not to shrink when size of window decreases, give it a low weight relative to others


# Configure weights for columns
mainWindow.columnconfigure(0, weight=100)  # we make the weight here to 100
mainWindow.columnconfigure(1, weight=1)    # Scrollbar column given less relative weight so it does not shrink with decrease in window size.
mainWindow.columnconfigure(2, weight=300)  # We make the weight here to 300
mainWindow.columnconfigure(3, weight=300)
mainWindow.columnconfigure(4, weight=300)

# Configure weights for rows
mainWindow.rowconfigure(0, weight=1)  # make weight here to 1
mainWindow.rowconfigure(1, weight=10)  # Make weight here to 10
mainWindow.rowconfigure(2, weight=1)
mainWindow.rowconfigure(3, weight=3)  # Make weight here to 3
mainWindow.rowconfigure(4, weight=3)


# Now we are going to add the listbox i.e. box where we put the lists
# we put the listbox in the mainWindow
# Then we put the listbox to start in row 1, column 0, make it sticky on NSEW, and let it span two rows (row 1 and 2)
# NSEW interpreted. We place grid on west, let it span to East, and then from South to North

fileList = tkinter.Listbox(mainWindow)
fileList.grid(row=1, column=0, sticky='nsew', rowspan=2)

# Now we configure the list. Note "config" is just short form for "configure". Can be used interchangeably
# we add border size to 2 and relief to sunken.

fileList.config(border=2, relief='sunken',)

# Now we are going to run a code to populate the list instead of adding it manually
# os.listdir stands for "Operating System" and "List Directory"
# Note that we imported OS at the beginning of the program
# we use os.listdir('/usr/bin') for MAC and Linux machine and os.listdir('C:\Windows\System32')
# This gives you a list of files in your windows OS folder (or MAC/Linux)
# tkinter.END - when you are inserting an argument in a listbox, you need to specify the insertion point.
# so we are using tkinter constant called END, which puts the list at the end of the entry as they are added.
# if you specify a number e.g. tkinter.END=0, the list will appear in reverse because each item will inserted at the
# start of the list instead of at the end.
# When you run this, it will display files in C:\Windows\System32

for zone in os.listdir('C:\Windows\System32'):
    fileList.insert(tkinter.END, zone)  # This adds filename.

# (1) Now we will add a scrollbar to the listbox to be able to scroll down
# we add the scroller in mainWindow with VERTICAL orientation
# The command=fileList.yview is how actions are associated with widgets
# So here command is set to the yview method of the listbox.
# if you CRTL + click yview, you see it is used to "Query and change the vertical position of the view"
# if scrollbar was horizontal, we would use "xview" instead of "yview"
# (2) Then we add listScroll to the grid in row 1, column 1 and set sticky to "nsw" and span two rows
# (3) Then we link the listbox to the Scrollbox by using the 'yscrollcommand" option of listbox (fileList)
# and let the listbox (filelist) call the "set" method of the listScroll when it changes
# The reason we are changing is if more items are added or if its scrolled using mouse or keyboard
# if the scrollbar was horizontal, we would use "xscrollcommand"

listScroll = tkinter.Scrollbar(mainWindow, orient=tkinter.VERTICAL, command=fileList.yview)
listScroll.grid(row=1, column=1, sticky='nsw', rowspan=2)
fileList['yscrollcommand'] = listScroll.set

# Now we will add a label frame that will contain "file details" and radio buttons
# (1)we use tkinter.LabelFrame option and add frame to mainWindow
# LabelFrame function allows text to be added to the label. in this case "File Details". Then draws a border around the contents "File Details"
# (2) Then we add it to the grid to row 1, column 2 and sticky options 'ne'

optionFrame = tkinter.LabelFrame(mainWindow, text="File Details")
optionFrame.grid(row=1, column=2, sticky='ne')

# Now we define Radio button Variable (rbValue)
# we will create three radio buttons that share the same variable because only one can be selected at any one time
# So as you click on each one, the one that was previously selected is automatically unselected
# The mechanism to do this in python relies on tkinter control variables that can bound to one or more widgets.
# Here we are using tkinter.IntVar() variable (interface variable)
# we use the ".set" function to set the default value to rbValue. in this case it is 3

rbValue = tkinter.IntVar()
rbValue.set(3)

# We define the Radio Buttons
# we add radio buttons in optionFrame (the frame we created and added in mainWindow above)
# Then we add text to come after the button, Filename, Path & Timestamp in this case.
# Value defines the value of the button. in this case, button 1 is the filename, button 2 is Path etc
# Then we assign the variable to rbValue which we defined above. This will be the same for all three buttons.
# if you click first button, the value 1 is added to variable rbValue, indicating the button that was clicked.
# Then we will query rbValue to see what button was clicked.

radio1 = tkinter.Radiobutton(optionFrame, text="Filename", value=1, variable=rbValue)
radio2 = tkinter.Radiobutton(optionFrame, text="Path", value=2, variable=rbValue)
radio3 = tkinter.Radiobutton(optionFrame, text="TimeStamp", value=3, variable=rbValue)

# Then add the radio buttons to the grid.
# When you run this, you will see the radio buttons in the grid.

radio1.grid(row=0, column=0, sticky='w')
radio2.grid(row=1, column=0, sticky='w')
radio3.grid(row=2, column=0, sticky='w')

# This program will display the filename and timestamp of whatever is selected in the listbox
# we will add an entry widget to show that result. The entry label and widget will be placed in the same cell of the grid
# We will then use the "sticky" option so  label appears in top left and widget in bottom left of the cell
# As long as the row is high enough, both of them should fit in there.
# We will also look at how the window will not be too small for the widget to cover the label

# This is code for label.
resultLabel = tkinter.Label(mainWindow, text="Results")
resultLabel.grid(row=2, column=2, sticky='nw')

# This is code for Entry or widget
# The entry widget is used to enter text strings. This widget allows the user to enter one line of text, in a single font.

result = tkinter.Entry(mainWindow)
result.grid(row=2, column=2, sticky='sw')


# we will now add Frame for the timespinners (timeFrame) using "LabelFrame" function of tkinter
# Then add timeFrame for to grid in row 3, column 0, and sticky on NEW

timeFrame = tkinter.LabelFrame(mainWindow, text="Time")
timeFrame.grid(row=3, column=0, sticky='new')

# Now we define timespinners themselves
# hourSpinner will be placed in "timeFrame" defined above with width of 2 and values from 0 to 24 (for 24 hour clock)
# we can define range using range(0, 24) to return 0 to 23
# another way to define range is use from_=0 and to=59 (not from_ has underscore because from is a reserved word. so we use _ to differentiate it.

hourSpinner = tkinter.Spinbox(timeFrame, width=2, values=tuple(range(0, 24)))  # use range to define 0 to 23 (hours in a day)
minuteSpinner = tkinter.Spinbox(timeFrame, width=2, from_=0, to=59)   # use from and to to define from 0 to 59 (minutes in an hour)
secondSpinner = tkinter.Spinbox(timeFrame, width=2, from_=0, to=59)  # use from and to to define 0 to 59 (seconds in a minute)

# then we add the spinners to the grid
# Then we add label to the Spinner, inserting it in timeframe, with text ':' and assign label into the grid in the same line

hourSpinner.grid(row=0, column=0)
tkinter.Label(timeFrame, text=':').grid(row=0, column=1)  # this is to put ":" between hour and minute
minuteSpinner.grid(row=0, column=2)
tkinter.Label(timeFrame, text=':').grid(row=0, column=3)  # This is to put ":" between minute and second
secondSpinner.grid(row=0, column=4)  # No separator here because it is the last one

# if you run above code, you will get the time spinner but it is not formatted well.
# we will no add some padding inside the timeFrame
# we can use "padx" to pad left and right side with defined pixels
# and use "pady" to pad top and bottom with defined pixels
# Here we are padding timeFrame, left and right with 36 pixels

timeFrame['padx'] = 36


# we will now add Frame for Date Spinners
# we add the dateFrame in mainWindow
# A frame is rectangular region on the screen. The frame widget is mainly used as
# a geometry master for other widgets, or to provide padding between other widgets
# Then add dateFrame to grid to row 4, column0 and sticky on NEW direction

dateFrame = tkinter.Frame(mainWindow)
dateFrame.grid(row=4, column=0, sticky='new')

# then we create the actual date labels
# we add them to dateFrame

dayLabel = tkinter.Label(dateFrame, text="Day")
monthLabel = tkinter.Label(dateFrame, text="Month")
yearLabel = tkinter.Label(dateFrame, text="Year")

# Then we add the labels to the grid. and stick them to the west (left)

dayLabel.grid(row=0, column=0, sticky='w')
monthLabel.grid(row=0, column=1, sticky='w')
yearLabel.grid(row=0, column=2, sticky='w')


# Now we add Date spinners
# for day, we give from 1 to 31
# For months, we add values from Jan to Dec
# For year, we give range from 2000 to 2099

daySpin = tkinter.Spinbox(dateFrame, width=5, from_=1, to=31)
monthSpin = tkinter.Spinbox(dateFrame, width=5, values=("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"))
yearSpin = tkinter.Spinbox(dateFrame, width=5, from_=2000, to=2099)

# Then we add the Date Spinners to the grid

daySpin.grid(row=1, column=0)
monthSpin.grid(row=1, column=1)
yearSpin.grid(row=1, column=2)


# Now we will add the "Ok" and "Cancel buttons
# We define the Ok button in mainWindow and assign it a text of "Ok"
# We define the "Cancel" button in mainWindow and assign it text of "Cancel"
# we also use command=mainWindow.quit to make it quit the program when you click Cancel button
# The quit method stops tkinter in the interpreter, so you may have problems if you run it in IDLE because IDLE is written in tkinter
# When we run code with function mainWindow.quit(), it does not work because it calls the function and the result is assigned to "command"
# In this case it returns None. so we need to use "quit" or "destroy" with no ()
# We can also use command-mainWindow.destroy, which stops the main loop and deletes the widget

okButton = tkinter.Button(mainWindow, text='Ok')
cancelButton = tkinter.Button(mainWindow, text='Cancel', command=mainWindow.quit)  # can use quit or destroy

# Now we add the buttons to the grid.

okButton.grid(row=4, column=3, sticky='e')
cancelButton.grid(row=4, column=4, sticky='w')




# Now we add mainWindow.mainloop() to run it and see what it looks like
mainWindow.mainloop()

# just to test to see what line we choose in the radio button, we add this code to print
# the number of the radio button we choose. This queries the rbValue with method "get" to see what value it has i.e. button we clicked.
# Note this will print after you close the GUI and let the mainloop() release control

print(rbValue.get())