# I'm following the tutorial from https://realpython.com/python-gui-tkinter/, which called "Python GUI Programming: Your Tkinter Tutorial".

# tkinter is the standard Python interface to the Tk GUI toolkit shipped with Python.
# ttk stands for Themed Tk. It’s a submodule of tkinter that provides modern, themed widgets (buttons, labels, comboboxes, progress bars, etc.).

# tkinter → provides the window & basic widgets
# ttk → provides fancier, modern-looking widgets to use inside that window

import tkinter as tk
import tkinter.ttk as ttk

# Using ttk (Themed Tk) instead of basic Tkinter widgets
import tkinter as tk
from tkinter import ttk

# Create the root window
root = tk.Tk()
root.title("The TTK Window")
root.geometry("300x500")  # optional window size

# Set a ttk theme (optional, modern look)
style = ttk.Style()
style.theme_use("clam")  # common themes: 'clam', 'default', 'alt', 'classic'

# Labels
greeting = ttk.Label(root, text="Hello, this is the first label!")
greeting.pack(pady=10)  # padding around the label

label2 = ttk.Label(root, text="Yes, this is the second label!")
label2.pack(pady=10)

# Note: ttk.Label ignores bg/fg colors on macOS; to style, use ttk.Style().

# Button
def on_click():
    print("Button clicked!")

button = ttk.Button(root, text="Click me!", command=on_click)
button.pack(pady=10)

# Single-line text entry
ttk.Label(root, text="Name").pack()
entry = ttk.Entry(root)
entry.pack(pady=5)

# Get text from entry (you must call .get() inside an event, not immediately)
def read_entry():
    print("Entered name:", entry.get())

ttk.Button(root, text="Submit", command=read_entry).pack(pady=5)

# Multi-line text input
ttk.Label(root, text="Comments").pack()
text_box = tk.Text(root, height=5, width=30)  # Text is not themed, still tk
text_box.pack(pady=5)

def read_text():
    print("Text content:", text_box.get("1.0", tk.END).strip())

ttk.Button(root, text="Print Text", command=read_text).pack(pady=5)

# Start the event loop
root.mainloop()