import tkinter as tk

# Create the main window
window = tk.Tk()

# Create a menu bar
menu_bar = tk.Menu(window)

# Create a File menu and add it to the menu bar
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Exit", command=window.quit)
menu_bar.add_cascade(label="File", menu=file_menu)

# Add the menu bar to the window
window.config(menu=menu_bar)

# Start the main event loop
window.mainloop()