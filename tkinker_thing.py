from tkinter import *
from tkinter import ttk
from tkinter import colorchooser
import random
import datetime



# Create the main window
root = Tk()
root.title("My thing")
# Create a frame widget
root.geometry("300x200")
frm = ttk.Frame(root, padding=10)
frm.grid()
#other stuff
label = ttk.Label(root, font=("Arial", 18))

#def commans for buttons
def change_color():
    root.configure(background= "#"+("%06x"%random.randint(0,16777215)))

def idk():
    e = colorchooser.askcolor(title="Choose background color")
    root.configure(bg=e[1])
#other def commans

def update_clock():
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    ttk.Label(root, text = str(current_time)).grid(column=0, row=1)
    root.after(1000, update_clock)

# Create a label widget
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Label()
# Create a button widget

quit_button = ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)

color_button = ttk.Button(frm, text="Change color", command=idk).grid(column=2, row=0)

random_color_button = ttk.Button(frm, text="Randomly change color", command=change_color).grid(column=1, row=1)

update_clock()

# Start the main event loop
root.mainloop()
