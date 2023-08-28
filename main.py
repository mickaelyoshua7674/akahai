from tkinter import *

# INIT WINDOW
window = Tk()

# CONFIG WINDOW
window.title("AKAHAI")
window.minsize(width=500, height=300)

# LABELS
my_label = Label(text="Label", font=("Arial", 24, "bold"))
my_label.pack(side="left")

# BUTTONS
def print_click():
    print("Clicked")
    new_text = input.get()
    my_label.config(text="Button got clicked " + new_text)
my_button = Button(text="Click Me", command=print_click)
my_button.pack()

# ENTRY
input = Entry()
input.pack()






















window.mainloop()