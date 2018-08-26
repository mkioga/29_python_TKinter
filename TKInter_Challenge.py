# ======================
# TKInter_Challenge.py
# ======================

# https://www.udemy.com/python-the-complete-python-developer-course/learn/v4/t/lecture/4570100?start=15

# Write a GUI program to create a simple calculator layout that looks like the screenshot
# Try to be as pythonic as possible. it is ok if you end up writing repeated buttons and grid statements
# but consider using lists and a for loop

# As an extra, refer to documentation to work out how to use minsize() to prevent your window from being
# shrunk so that the widgets vanish from view

# Hint: you may want to use the widgets .winfo_height() and .winfo_width () methods in which case you should
# know that they will not return the correct results unless the window has been forced to draw the widget
# by calling its .update() method first

# If you are using windows, you will probably find that the width is already constrained and cannot be resized
# too small. The height will still need to be constrained though.

# first we import tkinter

try:
    import tkinter
except ImportError:  # in case its python 2
    import Tkinter as tkinter

# Now we will create some keys which will contain the keys of the calculator
# We create keys using a nested list of list to represent the keypads
# Definitions:
# list =  ["Happy", "Very Happy"]: # A list of strings separated by commas
# Tuple = ("a", "b", "c") # Tuple enclosed in (). and is an ordered set of data similar to list but immutable


keys = [[('C', 1), ('CE', 1)],
        [('7', 1), ('8', 1), ('9', 1), ('+', 1)],
        [('4', 1), ('5', 1), ('6', 1), ('-', 1)],
        [('1', 1), ('2', 1), ('3', 1), ('*', 1)],
        [('0', 1), ('=', 1), ('/', 1)],
        ]

# Now we specify variable for padding of the mainWindow

mainWindowPadding = 8

# Now we define the mainWindow

# https://docs.python.org/2/library/tkinter.html
# class Tkinter.Tk(): The Tk class is instantiated without arguments.
# This creates a toplevel widget of Tk which usually is the main window of an application.

mainWindow = tkinter.Tk()  # instantiates mainWindow with Tk() class
mainWindow.title("Calculator")  # Sets the title of the window
mainWindow.geometry('640x480-100-200')  # defines dimensions of mainWindow
mainWindow['padx'] = mainWindowPadding  # Sets padding on mainWindow on horizontal sides

# This is the box where Entries will be displayed on the calculator.
# NOTE: Entry widget is used to enter text strings. This widget allows the user to enter one line of text, in a single font.
# We add it with .Entry method and then add it to grid

result = tkinter.Entry(mainWindow)
result.grid(row=0, column=0, sticky='nsew')

# Now we add keypad Frame using .Frame method and add it to mainWindow Then we add it to the grid.
# KeyPadFrame is where we will store the key buttons

# NOTE: A Frame is rectangular region on the screen. The frame widget is mainly used as
# a geometry master for other widgets, or to provide padding between other widgets

keyPadFrame = tkinter.Frame(mainWindow)  # We put the frame in mainWindow and will not give it a title
keyPadFrame.grid(row=1, column=0, sticky='nsew')  # Then add it to frame

# # Adding Calculator keys manually (my method)


# Now we add the keys Buttons manually into the keyPadFrame and add them to grid

# # Button "C"
# keyButtonC = tkinter.Button(keyPadFrame, text='C')
# keyButtonC.grid(row=1, column=0, sticky='nesw')
# # Button "CE"
# keyButtonCE = tkinter.Button(keyPadFrame, text='CE')
# keyButtonCE.grid(row=1, column=1, sticky='nesw')
# # Button "7"
# keyButton7 = tkinter.Button(keyPadFrame, text='7')
# keyButton7.grid(row=2, column=0, sticky='nesw')
# # Button "8"
# keyButton8 = tkinter.Button(keyPadFrame, text='8')
# keyButton8.grid(row=2, column=1, sticky='nesw')
# # Button "9"
# keyButton9 = tkinter.Button(keyPadFrame, text='9')
# keyButton9.grid(row=2, column=2, sticky='nesw')
# # Button "+"
# keyButtonplus = tkinter.Button(keyPadFrame, text='+')
# keyButtonplus.grid(row=2, column=3, sticky='nesw')
# # Button "4"
# keyButton4 = tkinter.Button(keyPadFrame, text='4')
# keyButton4.grid(row=3, column=0, sticky='nesw')
# # Button "5"
# keyButton5 = tkinter.Button(keyPadFrame, text='5')
# keyButton5.grid(row=3, column=1, sticky='nesw')
# # Button "6"
# keyButton6 = tkinter.Button(keyPadFrame, text='6')
# keyButton6.grid(row=3, column=2, sticky='nesw')
# # Button "-"
# keyButtonminus = tkinter.Button(keyPadFrame, text='-')
# keyButtonminus.grid(row=3, column=3, sticky='nesw')
#
# # Button "1"
# keyButton1 = tkinter.Button(keyPadFrame, text='1')
# keyButton1.grid(row=4, column=0, sticky='nesw')
# # Button "2"
# keyButton2 = tkinter.Button(keyPadFrame, text='2')
# keyButton2.grid(row=4, column=1, sticky='nesw')
# # Button "3"
# keyButton3 = tkinter.Button(keyPadFrame, text='3')
# keyButton3.grid(row=4, column=2, sticky='nesw')
# # Button "*"
# keyButtonMultiply = tkinter.Button(keyPadFrame, text='*')
# keyButtonMultiply.grid(row=4, column=3, sticky='nesw')
#
# # Button "0"
# keyButton0 = tkinter.Button(keyPadFrame, text='0')
# keyButton0.grid(row=5, column=0, sticky='nesw')
# # Button "="
# keyButtonEqual = tkinter.Button(keyPadFrame, text='=')
# keyButtonEqual.grid(row=5, column=1, sticky='nesw')
# # Button "/"
# keyButtonDivide = tkinter.Button(keyPadFrame, text='/')
# keyButtonDivide.grid(row=5, column=2, sticky='nesw')


# Adding calculator keys using for loop (Trainers Method)(less code)


row = 0
# print(keys[0])

for keyRow in keys:  # iterates through the rows in keys above
    # print(keyRow) # Can print the results with this

    col = 0  # For each row in keys, initialize column to 0
    # print(keyRow[0])  # Can use this to print columns. e.g. it will print ('C', 1) for row 0

    for key in keyRow:  # This iterates through each row to get the values. e.g. it gets ('C', 1) & ('CE', 1) for row 0
        # print(key)  # you can use this print to see the values per row

        # for each value e.g. ('C', 1), we create button, add it to "keyPad" frame we defined above
        # and give it text in key[0]. In ('C', 1), key[0] is 'C'
        # Then we add to grid using row=row and column=col (for first iteration, row=0 & col=0)
        # We use columnspan=key[1] to make it span number of columns defined in key[1]. for ('C', 1), key[1] is 1 hence it spans 1 column
        # "sticky=tkinter.E + tkinter.W" is another way or writing sticky='ew'. We are able to use + (concantenate) because
        # "sticky=tkinter.E + tkinter.W" returns a string. So it becomes sticky from east to west.

        tkinter.Button(keyPadFrame, text=key[0]).grid(row=row, column=col, columnspan=key[1], sticky=tkinter.E + tkinter.W)

        # After we print above for first entry ('C', 1)
        # we increment col using col = col + key[1] where initial key[1] from ('C', 1) is 1
        # so col becomes 0 + 1 = 1 and then we iterate to next column, which is ('CE', 1) for row 0.

        col += key[1]

        # After we go through all the columns in the row
        # we then increment the row by 1 (row = row + 1) and go to next row. row 1 is ('7', 1), ('8', 1), ('9', 1), ('+', 1)
    row += 1


# in above code, we can expand or shrink the GUI to whatever size we want.
# But we may want to define the sizes.
# For the extra point use minsize() to prevent your window from being shrunk so that the widgets vanish from view
# and use maxsize() to prevent window from being expanded too much.

# here is link for .update()
# http://effbot.org/tkinterbook/widget.htm
# we need to call the .update() method so we can use its values (minsize, maxsize, winfo_width and winfo_height)

mainWindow.update()

# We set minimum size of mainWindow. We use "minsize" method
# Minimum mainWindow Width = keyPadFrame's width + mainWindowPadding <<== Use .winfo_width to get width
# Minimum mainWindow Height = height of "result" (box where result is displayed. defined above) + height of keyPadFrame
# we use .winfo_height to get height
# Now when you run the code, there is a minimum window size which you cannot go below

mainWindow.minsize(keyPadFrame.winfo_width() + mainWindowPadding, result.winfo_height() + keyPadFrame.winfo_height())

# We set maximum size of mainWindow. We use "maxsize" method.
# Here we are setting maximum size to be equal to minimum size.
# Maximum mainWindow Width = keyPadFrame's width + mainWindowPadding. <<== Use .winfo.width to get width
# Maximum mainWindow Height = height of "result" box + height of keyPadFrame
# When you run this code, Max and Min sizes are same. So you will not be able to expand or shrink the window.

# mainWindow.maxsize(keyPadFrame.winfo_width() + mainWindowPadding, result.winfo_height() + keyPadFrame.winfo_height())

# Say we want Maximum Size to be bigger than Minimum sizes
# We do that by adding a number of pixels to height and width
# In this case, we are making Max size to be 50 pixels more than Min size (both width and height).
# If you run the code, it starts with Max size, then you can shrink it to Min size.

mainWindow.maxsize(keyPadFrame.winfo_width() + mainWindowPadding + 50, result.winfo_height() + keyPadFrame.winfo_height() + 50)


# Now we add mainWindow.mainloop() to run it and see what it looks like
mainWindow.mainloop()
