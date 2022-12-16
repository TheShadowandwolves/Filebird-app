# import tkinter as tk

# # Create the main window
# window = tk.Tk()

# # Create a menu bar
# menu_bar = tk.Menu(window)

# # Create a File menu and add it to the menu bar
# file_menu = tk.Menu(menu_bar, tearoff=0)
# file_menu.add_command(label="Exit", command=window.quit)
# menu_bar.add_cascade(label="File", menu=file_menu)

# # Add the menu bar to the window
# window.config(menu=menu_bar)

# # Start the main event loop
# window.mainloop()
import tkinter as tk
from tkinter import ttk as ttk

root = tk.Tk()

# Create a treeview widget
treeview = ttk.Treeview(root, columns=['Task', 'Status'])
treeview.pack(fill='both', expand=True)

# Add a checkbox to the last column for each row
for i in range(5):
    treeview.insert('', 'end', text='Task {}'.format(i), values=('', tk.IntVar()))
    ttk.Checkbutton(treeview, variable=treeview.set(i, 'Status')).grid(column=1, row=i, in_=treeview)

# Add the checkbox column to the treeview
treeview.column('Status', width=50, anchor='center')

root.mainloop()
