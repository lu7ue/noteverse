# I'm following the tutorial from https://realpython.com/python-gui-tkinter/, which called "Python GUI Programming: Your Tkinter Tutorial".

# tkinter is the standard Python interface to the Tk GUI toolkit shipped with Python.
# ttk stands for Themed Tk. It’s a submodule of tkinter that provides modern, themed widgets (buttons, labels, comboboxes, progress bars, etc.).

# tkinter → provides the window & basic widgets
# ttk → provides fancier, modern-looking widgets to use inside that window

import tkinter as tk
import tkinter.ttk as ttk

# [Widgets] are the elements that users interact with your program. 
# Each [widget] in Tkinter is defined by a class:
# Label - A widget used to display text on the screen
# Button - A button that can contain text and can perform an action when clicked
# Entry - A text entry widget that allows only a single line of text
# Text - A text entry widget that allows multiline text entry
# Frame - A rectangular region used to group related widgets or provide padding between widgets

window = tk.Tk()
window.title("The Tkinter Window")
window.geometry("300x500")  # optional: set window size

greeting = tk.Label(text="Hello, this is the first label!")
greeting.pack(pady=10)  # <- this is required to place the label in the window

label = tk.Label(
    text="Yes, this is the second label",
    fg="white",  # Set the text color to white; fg stands for 'foreground'
    bg="black",  # Set the background color to black; bg stands for 'background'
    width=20,
    height=5
)
label.pack(pady=10)
# note: 
# There are numerous valid color names, including: "red", "orange", "yellow", "green", "blue", "purple"; 
# Many of the HTML color names work with Tkinter， check: https://htmlcolorcodes.com/color-names/.
# or specify a color using hexadecimal RGB values: #RRGGBB, e.g., "#ff0000" for red.
#
# tkinter uses text units, instead of pixels, which ensures the text fits properly in labels and buttons, no matter where the application is running.

def on_click():
    print("Button clicked!")

button = tk.Button(
    window,
    text="Click me!",
    fg="white",
    bg="black", # macOS enforces system-native button rendering, so simple bg color changes often won’t work.
    width=10,
    height=5
)
button.pack(pady=10)  # <-- this makes it appear in the window

# using Entry widget to get user input
tk.Label(window, text="Name").pack(pady=5)
entry = tk.Entry(window)
entry.pack(pady=5)

def read_entry():
    print("Entered name:", entry.get())

tk.Button(window, text="Submit", command=read_entry).pack(pady=5)

# usig Text widget for multiline text input
tk.Label(window, text="Comments").pack(pady=5)
text_box = tk.Text(window, height=5, width=30)
text_box.pack(pady=5)

def read_text():
    print("Text content:", text_box.get("1.0", tk.END).strip())  # get all text from line 1, character 0 to the end

tk.Button(window, text="Print Text", command=read_text).pack(pady=5)

window.mainloop()  # <- this is required to display and keep the window running