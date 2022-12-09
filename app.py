import tkinter as tk
# Create the main window
root = tk.Tk()

# Set the title of the window
root.title("File Bird v0.0.1")

# Set the size of the window
root.geometry("800x600")



# Create a menu with some items
menu = tk.Menu(root)
menu.add_command(label="Open")
menu.add_command(label="Save")
menu.add_command(label="Edit")
menu.add_command(label="Quit", command=root.quit)

# Add the menu to the window
root.config(menu=menu)

# Start the event loop
root.mainloop()
