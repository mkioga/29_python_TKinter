
# =================
# 29_TKinter.py
# =================


# "tkinter" module


# "tkinter" module provides access to the "tkwidget" toolkit and allow GUI programs to be created.
# tkinter was developed to work with scripting language called TCL
# tkinter binding works by sending TCL code to a TCL interpretor that is embedded in python interpreter
# There are other graphic programs available but tkinter is part of python language

# Here are links for documentation for tkinter
# https://docs.python.org/2/library/tkinter.html
# http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/index.html
# http://www.tkdocs.com/
# https://en.wikipedia.org/wiki/Tk_(software)

# Now we will check to see if tkinter is installed properly with this python

import tkinter

print(tkinter.TkVersion)    # To check the version installed
print(tkinter.TclVersion)   # Also to check version

tkinter._test()   # To test tkinter is installed well. It pulls a GUI

print("="*40)

# importing tkinter in python 2 syntax

import tkinter # in python 3
# import Tkinter # in python 2. has a capital T

# if you don't know which python code you are running, you can use this command below
# to check and download tkinter in the correct syntax


try:
    import tkinter   # Try to see if you can import with tkinter (python 3 syntax)
except ImportError:  # if there is an ImportError (meaning you're running python 2 and it expects Tkinter (with cap T)
    import Tkinter as tkinter  # you import Tkinter and assign it to tkinter

print(tkinter.TkVersion)    # To check the version installed
print(tkinter.TclVersion)   # Also to check version

tkinter._test()   # To test tkinter is installed well. It pulls a GUI

print("="*40)

# ==========================================
# Another way to pull up the GUI is by using "mainWindow" and giving it parameters


try:
    import tkinter   # Try to see if you can import with tkinter (python 3 syntax)
except ImportError:  # if there is an ImportError (meaning you're running python 2 and it expects Tkinter (with cap T)
    import Tkinter as tkinter  # you import Tkinter and assign it to tkinter

print(tkinter.TkVersion)    # To check the version installed
print(tkinter.TclVersion)   # Also to check version

# Now we use mainWindow to make a GUI

mainWindow = tkinter.Tk()

mainWindow.title("Hello World")   # Defines the title of the GUI
mainWindow.geometry('640x480')    # Defines the dimensions of the GUI in pixels. You pass it as a string.
# you can define distance from edges using ('640x480+50+100') which means same GUI dimensions, but 50 pixels from left and 100 pixels from Top

mainWindow.mainloop()  # Now pass control to Tk by calling the mainloop method which handles all event processes that GUI needs to function

print("="*40)

# Note that the program closes when you close the GUI


# ==========================================


# Pack Geometry Manager

# Once you've got a window, the application widget (or what you want to appear in the window)
# can be placed on that window using one of three different geometry managers
# "grid" manager is the most useful
# "pack" manager is the most commonly used and easiest to use, so we will start with it

# Note that everything in tkinter is a window and objects are placed in a hierarchy
# For example in this code, "mainWindow" is the "root" window and everything else must either
# be placed within "mainWindow" or within one of the child windows

# Not every window can have children. But every window except the root must have a master window

# To see the effects of positioning widgets in the window, we will use "pack" and we be placing a "canvas" widget
# "canvas" widget is used for displaying graphics


# we first import tkinter

try:
    import tkinter   # Try to see if you can import with tkinter (python 3 syntax)
except ImportError:  # if there is an ImportError (meaning you're running python 2 and it expects Tkinter (with cap T)
    import Tkinter as tkinter  # you import Tkinter and assign it to tkinter

# ====================================
# Now we use mainWindow to make a GUI
# ====================================

mainWindow = tkinter.Tk()

mainWindow.title("This is the Title")   # Defines the title of the GUI
mainWindow.geometry('540x380')    # Defines the dimensions of the GUI in pixels. You pass it as a string.
# you can define distance from edges using ('640x480+50+100') which means same GUI dimensions, but 50 pixels from left and 100 pixels from Top

# Then we make a label. Note Label starts with Capital L
# We specify the window (mainWindow) and then specify the text

label = tkinter.Label(mainWindow, text="This is the label")
label.pack(side='top')  # Use pack geometry manager to place the label text within the window. options are top, bottom, left, right

# Then we add the Canvas (Capital C) and specify mainWindow,
# relief=raised gives it the raised appearance. Options are flat, groove, raised, ridge, solid, or sunken
# borderwidth = 10 gives border width of 10 pixels

canvas = tkinter.Canvas(mainWindow, relief='raised', borderwidth=10)
canvas.pack(side='top')  # Then we use pack geometry manager place the widget within the window. options are top, bottom, left, right

# Use mainloop() Now pass control to Tk by calling the mainloop method which handles all event processes that GUI needs to function

mainWindow.mainloop()

print("="*40)


# =======================================================================
# using "fill" to make the canvas fill the height or width of the window
# =======================================================================

try:
    import tkinter   # Try to see if you can import with tkinter (python 3 syntax)
except ImportError:  # if there is an ImportError (meaning you're running python 2 and it expects Tkinter (with cap T)
    import Tkinter as tkinter  # you import Tkinter and assign it to tkinter

# Now we use mainWindow to make a GUI

mainWindow = tkinter.Tk()

mainWindow.title("This is the Title")   # Defines the title of the GUI
mainWindow.geometry('500x500')    # Defines the dimensions of the GUI in pixels. You pass it as a string.
# you can define distance from edges using ('640x480+50+100') which means same GUI dimensions, but 50 pixels from left and 100 pixels from Top

# Then we make a label. Note Label starts with Capital L
# We specify the window (mainWindow) and then specify the text

label = tkinter.Label(mainWindow, text="This is the label")
label.pack(side='top')  # Use pack geometry manager to place the label text within the window. options are top, bottom, left, right

# Then we add the Canvas (Capital C) and specify mainWindow,
# relief=raised gives it the raised appearance. Options are flat, groove, raised, ridge, solid, or sunken
# borderwidth = 10 gives border width of 10 pixels

# We used the fill parameter above. options are X, Y, or both
# This will fill the widget on X, or Y or both X and Y directions
# you will notice if you have side='top' and fill=Y, or side=bottom and fill=X
# it does not expand the widget as expected. That is why we added expand=True

canvas = tkinter.Canvas(mainWindow, relief='raised', borderwidth=10)
canvas.pack(side='top', fill=tkinter.Y, expand=True)  # Use pack geometry manager place the widget within the window. options are top, bottom, left, right

# Use mainloop() Now pass control to Tk by calling the mainloop method which handles all event processes that GUI needs to function

mainWindow.mainloop()

print("="*40)


# =====================
# Adding "buttons"
# =====================

try:
    import tkinter
except ImportError:
    import Tkinter as tkinter


mainWindow = tkinter.Tk()

mainWindow.title("This is the Title")
mainWindow.geometry('700x500')

label = tkinter.Label(mainWindow, text="This is the label")
label.pack(side='top')

canvas = tkinter.Canvas(mainWindow, relief='raised', borderwidth=10)
canvas.pack(side='left')

# We will add three buttons
# When we run it, we see that when widgets share the same side, they are placed adjacent to each other
# in the order they were packed


button1 = tkinter.Button(mainWindow, text='Button1')
button2 = tkinter.Button(mainWindow, text='Button2')
button3 = tkinter.Button(mainWindow, text='Button3')

button1.pack(side='left')
button2.pack(side='left')
button3.pack(side='left')

mainWindow.mainloop()

print("="*40)


# ================================================================================
# using "anchor" to place buttons either North (n), South (s), East(e) or West(w)
# ================================================================================

try:
    import tkinter
except ImportError:
    import Tkinter as tkinter


mainWindow = tkinter.Tk()

mainWindow.title("This is the Title")
mainWindow.geometry('700x500')

label = tkinter.Label(mainWindow, text="This is the label")
label.pack(side='top')

canvas = tkinter.Canvas(mainWindow, relief='raised', borderwidth=10)
canvas.pack(side='left')

# We will add three buttons
# When we run it, we see that when widgets share the same side, they are placed adjacent to each other
# in the order they were packed


button1 = tkinter.Button(mainWindow, text='Button1')
button2 = tkinter.Button(mainWindow, text='Button2')
button3 = tkinter.Button(mainWindow, text='Button3')

# We are going to add anchor here and we see the buttons are placed North, South and East
# you should play with sides and anchor to see how they behave
# if you pack left or right, you can only have vertical position altered by anchor
# if you pack top or bottom, you can only have horizonatal position altered by anchor

button1.pack(side='left', anchor='n')
button2.pack(side='left', anchor='s')
button3.pack(side='left', anchor='e')

mainWindow.mainloop()

print("="*40)


# ==============================
# using "Frame" in pack
# ==============================


try:
    import tkinter
except ImportError:
    import Tkinter as tkinter


mainWindow = tkinter.Tk()

mainWindow.title("This is the Title")
mainWindow.geometry('700x500')

label = tkinter.Label(mainWindow, text="This is the label")
label.pack(side='top')

# we will add a leftFrame here

leftFrame = tkinter.Frame(mainWindow)
leftFrame.pack(side='left', anchor='n', fill=tkinter.Y, expand=False)

# we will use leftFrame on Canvas instead of the original mainWindow
# we will put canvas on left side and anchor of north

canvas = tkinter.Canvas(leftFrame, relief='raised', borderwidth=10)
canvas.pack(side='left', anchor='n')

# Then we will add a rightFrame and put the buttons in rightFrame
# we put rightFrame on the right side, anchor it to north

rightFrame = tkinter.Frame(mainWindow)
rightFrame.pack(side='right', anchor='n', expand=True)

# The buttons will use rightFrame because they will now be in rightFrame

button1 = tkinter.Button(rightFrame, text='Button1')
button2 = tkinter.Button(rightFrame, text='Button2')
button3 = tkinter.Button(rightFrame, text='Button3')

# we remove the anchor in pack because it is using rightFrame which already has anchor

button1.pack(side='top')
button2.pack(side='top')
button3.pack(side='top')

mainWindow.mainloop()

print("="*40)

# Note that "pack" is only suitable for very simple layouts and is the simplest of the three available geometry managers.


# ===============================================================================
# "Place" Geometry manager

# "place" geometry manager is simpler than "pack" and can be useful in certain situations
# However it works by specifying absolute positions for at least one window and then other windows
# can be positioned relative to the first window.

# Unless you know the screen size that your program will be running, the use of absolute positioning is not recommended.
# For more complicated layouts, we get much better results using the "grid" geometry manager


# ============================
# "grid" geometry manager
# ============================

# "grid" geometry manager works by positioning widgets in a grid.
# The grid does not exist until you start adding things to it and then its dimensions are calculated automatically
# This is the way to go because you can run it in different screen sizes.

# Note that widgets in the same column can be lined up below or above each other.
# And widgets in the same row can be lined up next to each other

# We can make a screen similar to one above but using a "grid"


try:
    import tkinter
except ImportError:
    import Tkinter as tkinter


mainWindow = tkinter.Tk()

mainWindow.title("This is the Title")
mainWindow.geometry('700x500-8-200')  # we use -8-200 to change positioning relative to your screen

label = tkinter.Label(mainWindow, text="This is the label")
label.grid(row=0, column=0)  # We use grid instead of pack and specify row and column

# we will add a leftFrame here

leftFrame = tkinter.Frame(mainWindow)
leftFrame.grid(row=1, column=1)  # for leftFrame, we use grid and specify row and column

# we will use leftFrame on Canvas instead of the original mainWindow
# we will put canvas on left side and anchor of north

canvas = tkinter.Canvas(leftFrame, relief='raised', borderwidth=10)
canvas.grid(row=1, column=0)  # We use grid for canvas and specify row and column

# Then we will add a rightFrame and put the buttons in rightFrame
# we put rightFrame on the right side, anchor it to north

rightFrame = tkinter.Frame(mainWindow)
rightFrame.grid(row=1, column=2)  # we use grid for rightFrame and specify row and column

# The buttons will use rightFrame because they will now be in rightFrame

button1 = tkinter.Button(rightFrame, text='Button1')
button2 = tkinter.Button(rightFrame, text='Button2')
button3 = tkinter.Button(rightFrame, text='Button3')

# we remove the anchor in pack because it is using rightFrame which already has anchor

button1.grid(row=0, column=0)  # Use grid for buttonw and specify rows and columns
button2.grid(row=1, column=0)  # Note these are relative positions inside rightFrame because buttons are in rightFrame
button3.grid(row=2, column=0)

mainWindow.mainloop()

print("="*40)


# =================================
# using "sticky" property
# =================================

# in result above, we can see the buttons are all at the same place.
# we can use the "sticky" property to position them accurately
# "sticky" in "grid" takes same compass points as "anchor" when using "pack"
# http://effbot.org/tkinterbook/grid.htm  (for some info on sticky)
# Sticky has options N, S, E, W to position the button within the grid

# in this case, we will add "sticky" to rightFrame because that is where the buttons are


try:
    import tkinter
except ImportError:
    import Tkinter as tkinter


mainWindow = tkinter.Tk()

mainWindow.title("This is the Title")
mainWindow.geometry('700x500-8-200')  # we use -8-200 to change positioning relative to your screen

label = tkinter.Label(mainWindow, text="This is the label")
label.grid(row=0, column=0)  # We use grid instead of pack and specify row and column

# we will add a leftFrame here

leftFrame = tkinter.Frame(mainWindow)
leftFrame.grid(row=1, column=1)  # for leftFrame, we use grid and specify row and column

# we will use leftFrame on Canvas instead of the original mainWindow
# we will put canvas on left side and anchor of north

canvas = tkinter.Canvas(leftFrame, relief='raised', borderwidth=10)
canvas.grid(row=1, column=0)  # We use grid for canvas and specify row and column

# Then we will add a rightFrame and put the buttons in rightFrame
# we put rightFrame on the right side, anchor it to north

rightFrame = tkinter.Frame(mainWindow)
rightFrame.grid(row=1, column=2, sticky='n')  # we add sticky here. We see all buttons goes north of rightFrame
# Note that using W or E may not have an effect. see explanation above when using pack

# The buttons will use rightFrame because they will now be in rightFrame

button1 = tkinter.Button(rightFrame, text='Button1')
button2 = tkinter.Button(rightFrame, text='Button2')
button3 = tkinter.Button(rightFrame, text='Button3')

# we remove the anchor in pack because it is using rightFrame which already has anchor

button1.grid(row=0, column=0)  # Use grid for buttonw and specify rows and columns
button2.grid(row=1, column=0)  # Note these are relative positions inside rightFrame because buttons are in rightFrame
button3.grid(row=2, column=0)

mainWindow.mainloop()

print("="*40)


# ==========================================

# using "columnconfigure" or "grid_columnconfigure"
# Note that these two are actually the same thing because "columnconfigure" calls "grid_columnconfigure"

# in above results, we see that the buttons are too close to the frame (rightFrame)
# To correct that, we can configure the individual columns using the "columnconfigure" method to give "weight"
# to the each column. We will discuss "weight" more later.
# But Note that until a weight has been set, then the column is not sized to fit a window but it just has the minimum
# width it needs to display its content. "columnconfigure" is a way to override that.


try:
    import tkinter
except ImportError:
    import Tkinter as tkinter


mainWindow = tkinter.Tk()

mainWindow.title("This is the Title")
mainWindow.geometry('700x500-8-200')  # we use -8-200 to change positioning relative to your screen

label = tkinter.Label(mainWindow, text="This is the label")
label.grid(row=0, column=0)  # We use grid instead of pack and specify row and column

# we will add a leftFrame here

leftFrame = tkinter.Frame(mainWindow)
leftFrame.grid(row=1, column=1)  # for leftFrame, we use grid and specify row and column

# we will use leftFrame on Canvas instead of the original mainWindow
# we will put canvas on left side and anchor of north

canvas = tkinter.Canvas(leftFrame, relief='raised', borderwidth=10)
canvas.grid(row=1, column=0)  # We use grid for canvas and specify row and column

# Then we will add a rightFrame and put the buttons in rightFrame
# we put rightFrame on the right side, anchor it to north

rightFrame = tkinter.Frame(mainWindow)
rightFrame.grid(row=1, column=2, sticky='n')  # we add sticky here. We see all buttons goes north of rightFrame
# Note that using W or E may not have an effect. see explanation above when using pack

# The buttons will use rightFrame because they will now be in rightFrame

button1 = tkinter.Button(rightFrame, text='Button1')
button2 = tkinter.Button(rightFrame, text='Button2')
button3 = tkinter.Button(rightFrame, text='Button3')

# we remove the anchor in pack because it is using rightFrame which already has anchor

button1.grid(row=0, column=0)  # Use grid for buttonw and specify rows and columns
button2.grid(row=1, column=0)  # Note these are relative positions inside rightFrame because buttons are in rightFrame
button3.grid(row=2, column=0)

# We will use "columnconfigure" and "grid_columnconfigure" here to give the columns weight
# NOTE that we have only three columns. Column 0 has label and canvas, column 1 has leftFrame, Column 3 has rightFrame
# To see that colunmconfigure is same as grid_columnconfigure, do CTRL + click columnconfigure. it will take you to
# source code which shows columnconfigure = grid_columnconfigure
# you can use columnconfigure because it needs less typing

mainWindow.columnconfigure(0, weight=1)  # use columnconfigure to add weight=1 to column 0
mainWindow.columnconfigure(1, weight=1)  # use colunmconfigure to add weight=1 to column 1
mainWindow.grid_columnconfigure(2, weight=1)  # use grid_colunmconfigure to add weight=1 to column 2

# if you CTRL+ click on columnconfigure, you will see these definitions of resources, weight and pad

# Valid resources are minsize (minimum size of the column),
# weight (how much does additional space propagate to this column)
# and pad (how much space to let additionally).

mainWindow.mainloop()

print("="*40)


# ==========================================

# we will use "sticky" to expand leftFrame so that it is full height of its row
# and rightFrame to be full width of its column



try:
    import tkinter
except ImportError:
    import Tkinter as tkinter


mainWindow = tkinter.Tk()

mainWindow.title("This is the Title")
mainWindow.geometry('700x500-8-200')  # we use -8-200 to change positioning relative to your screen

label = tkinter.Label(mainWindow, text="This is the label")
label.grid(row=0, column=0)  # We use grid instead of pack and specify row and column

# we will add a leftFrame here

leftFrame = tkinter.Frame(mainWindow)
leftFrame.grid(row=1, column=1)  # for leftFrame, we use grid and specify row and column

# we will use leftFrame on Canvas instead of the original mainWindow
# we will put canvas on left side and anchor of north

canvas = tkinter.Canvas(leftFrame, relief='raised', borderwidth=10)
canvas.grid(row=1, column=0)  # We use grid for canvas and specify row and column

# Then we will add a rightFrame and put the buttons in rightFrame
# we put rightFrame on the right side, anchor it to north

rightFrame = tkinter.Frame(mainWindow)
rightFrame.grid(row=1, column=2, sticky='n')  # we add sticky here. We see all buttons goes north of rightFrame
# Note that using W or E may not have an effect. see explanation above when using pack
# note that you can add sticky='news' for north, east, west, south in any order.

# The buttons will use rightFrame because they will now be in rightFrame

button1 = tkinter.Button(rightFrame, text='Button1')
button2 = tkinter.Button(rightFrame, text='Button2')
button3 = tkinter.Button(rightFrame, text='Button3')

# we remove the anchor in pack because it is using rightFrame which already has anchor

button1.grid(row=0, column=0)  # Use grid for buttonw and specify rows and columns
button2.grid(row=1, column=0)  # Note these are relative positions inside rightFrame because buttons are in rightFrame
button3.grid(row=2, column=0)

# We will use "columnconfigure" and "grid_columnconfigure" here to give the columns weight
# NOTE that we have only three columns. Column 0 has label and canvas, column 1 has leftFrame, Column 3 has rightFrame
# To see that colunmconfigure is same as grid_columnconfigure, do CTRL + click columnconfigure. it will take you to
# source code which shows columnconfigure = grid_columnconfigure
# you can use columnconfigure because it needs less typing

mainWindow.columnconfigure(0, weight=1)  # use columnconfigure to add weight=1 to column 0
mainWindow.columnconfigure(1, weight=1)  # use colunmconfigure to add weight=1 to column 1
mainWindow.grid_columnconfigure(2, weight=1)  # use grid_colunmconfigure to add weight=1 to column 2

# if you CTRL+ click on columnconfigure, you will see these definitions of resources, weight and pad

# Valid resources are minsize (minimum size of the column),
# weight (how much does additional space propagate to this column)
# and pad (how much space to let additionally).


# we will use "sticky" to expand leftFrame so that it is full height of its row
# and rightFrame to be full width of its column

leftFrame.config(relief='sunken', borderwidth=2)  # use .config to specify relief and borderwidth so we see them
rightFrame.config(relief='sunken', borderwidth=2)

leftFrame.grid(sticky='ns')  # Add leftFrame to span from north to south i.e. full height of its row
rightFrame.grid(sticky='new')  # rightFrame to span from north, to east, to west i.e. full width of its column

# we also want button2 to occupy the full width of rightFrame. we use sticky and assign it from east to west
# We first have to give weight to rightFrame where button2 exists. otherwise sticky='ew' for button2 will not work
# also note that default for sticky is centered, and we see that the buttons are centered within rightFrame

rightFrame.columnconfigure(0, weight=1)
button2.grid(sticky='ew')

# mainloop() should always be at the end to give control to tkinter to create graphic

mainWindow.mainloop()

print("="*40)

# NOTE: it is always a good idea to draw a sketch of the GUI you want to create on paper



