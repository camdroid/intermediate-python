#This program creates a window using tkinter and allows the user to dynamically update
# the size of that window by adjusting width and height inputs

# tkinter is a library for creating simple GUIs (Graphical User Interfaces AKA windows)
# http://effbot.org/tkinterbook/
# http://usingpython.com/using-tkinter/
import tkinter

# Define the starting size of the window, we will use this in a couple places
STARTING_WIDTH = 400
STARTING_HEIGHT = 400

# Set the dimensions of the GUI window.
def setWindowSize(window, width, height):
    # The geometry method takes a string in the format of "widthxheight".
    # For example window.geometry("300x200") would make the window 300 pixels wide
    # and 200 pixels tall
    window.geometry(str(width) + "x" + str(height))

# Display the area of the GUI window
def setAreaText(label, area):
    label.configure(text="The area of this window is " + str(area) + " pixels")

# Calculate an area
def calculateArea(width, height):
    return width * height

# Create a GUI window with tkinter
window = tkinter.Tk()

# Set the initial title and dimensions of the GUI window
window.title("My Cool GUI App")
setWindowSize(window, STARTING_WIDTH, STARTING_HEIGHT)

# Create a label and input for the width property
widthLabel = tkinter.Label(window, text="Width:")
widthLabel.grid(row=0, column=0)
widthText = tkinter.Entry(window)
widthText.grid(row=0, column=1, columnspan=2)
widthText.insert(0, STARTING_WIDTH)

# Create a label and input for the height property
heightLabel = tkinter.Label(window, text="Height:")
heightLabel.grid(row=1, column=0)
heightText = tkinter.Entry(window)
heightText.grid(row=1, column=1, columnspan=2)
heightText.insert(0, STARTING_HEIGHT)

# Create a label for displaying the area of the window
areaLabel = tkinter.Label(window)
areaLabel.grid(row=2, column=0, columnspan=3)
setAreaText(areaLabel, calculateArea(STARTING_WIDTH, STARTING_HEIGHT))

# A function that is executed when the button is pressed
# Updates the window size from the width and height values entered in the window
def updateWindowSize():
    width = int(widthText.get())
    height = int(heightText.get())
    setWindowSize(window, width, height)
    setAreaText(areaLabel, calculateArea(width, height))

# Create a button that will apply the updated width and height.
# When the button is pressed, the command to execute is the updateWindowSize function
changeWindowSizeButton = tkinter.Button(window, text="RESIZE!", command=updateWindowSize)
changeWindowSizeButton.grid(row=3, column=1)

#Start the GUI window
window.mainloop()
